import sqlite3
import os
import csv
import json
from pathlib import Path
# from pprint import pprint
import pickle
import re


in_path = "./Day07/students.csv"
out_path = "./Day07/summary.json"

# in_path = "students.csv"
# out_path = "summary.json"


def convert_log_file(input_log_path, output_csv_path, output_json_path):
    script_dir = Path(__file__).resolve().parent
    input_log_path = script_dir / input_log_path
    output_json_path = script_dir / output_json_path
    output_csv_path = script_dir / output_csv_path
    pattern = r"^(?P<TIMESTAMP>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| (?P<USER_ID>[A-Z0-9]+) \| (?P<ENDPOINT>\/[a-zA-Z0-9_\/.-]+) \| (?P<STATUS_CODE>\d{3})$"
    mtch_list = []
    with open(input_log_path, 'r') as log:
        for line in log:
            mtch = re.match(pattern=pattern, string=line)
            if mtch:
                mtch_list.append(mtch.groupdict())
    # print(mtch_list)
    with open(output_json_path, 'w') as json_file:
        json.dump(mtch_list, json_file, indent=3)
    with open(output_csv_path, 'w') as csv_file:
        csvw = csv.DictWriter(
            csv_file, fieldnames=mtch_list[0].keys(), lineterminator="\r")
        # pprint(help(csvw.writeheader()))
        csvw.writeheader()
        csvw.writerows(mtch_list)


def process_student_records(input_csv_path=in_path, output_json_path=out_path):
    script_dir = Path(__file__).resolve().parent
    input_csv_path = script_dir / input_csv_path
    output_json_path = script_dir / output_json_path
    with open(input_csv_path, "r") as csvfile:
        csvr = csv.DictReader(csvfile)
        course_set = {}
        total_students = 0
        top_scorer = {"name": "default", "score": -1.0}
        total_score = 0
        for line in csvr:
            total_students += 1
            total_score += float(line.get("score"))
            if float(top_scorer["score"]) < float(line["score"]):
                top_scorer.update(
                    {"name": line["name"], "score": line["score"]})
            x = 0 if course_set.get(
                line["course"]) is None else course_set.get(line["course"])
            course_set.update(
                {line["course"]: x + 1})
            # dict_list.append(line)

        ans_dict = {
            "total_students": total_students,
            "average_score": total_score/total_students,
            "top_scorer": top_scorer,
            "course_counts": course_set
        }
        with open(output_json_path, "w", encoding="utf-8") as jsonfile:
            json.dump(ans_dict, jsonfile, indent=3)

    print(f"Data Saved in {output_json_path}")

    ...
# Assignment 3: Object State Persistence with Pickle


class ExperimentSnapshot:
    def __init__(self, **kwargs):
        self.experiment_id = kwargs.get("experiment_id")
        self.model_type = kwargs.get("model_type")
        self.hyperparameters = kwargs.get("hyperparameters")
        self.metrics = kwargs.get("metrics")

    def get_best_metric(self, metric_name):
        return self.metrics.get(metric_name)

    # @classmethod


def save_experiment(snapshot: ExperimentSnapshot, file_path):
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / file_path
    if isinstance(snapshot, ExperimentSnapshot):
        # if not os.path.isfile(file_path):
        #     raise FileNotFoundError("Mili nhi file jao file banao")
        with open(file_path, 'wb') as file:
            pickle.dump(snapshot, file)
    else:
        raise TypeError(
            "save_experiment(snapshot, file_path)`: Serializes the `ExperimentSnapshot` object to `file_path` in binary mode using `pickle.dump()")


def load_experiment(file_path):
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / file_path

    if not os.path.isfile(file_path):
        raise FileNotFoundError("Mili nhi file jao file banao")

    with open(file_path, 'rb') as file:
        return pickle.load(file=file)


class UserDatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        with self.conn:
            curse = self.conn.cursor()
            curse.execute(
                '''
                CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                address TEXT,
                mobile TEXT,
                email TEXT
                );
                '''
            )
            self.conn.commit()

    def find_user(self, username):
        with self.conn:
            curse = self.conn.cursor()
            curse.execute(
                """SELECT username,address,mobile,email FROM user WHERE  username = ?""",
                (username,)
            )
            return curse.fetchone()

    def add_or_update_user(self, username, address, mobile, email):
        with self.conn:
            curse = self.conn.cursor()
            curse.execute(
                '''INSERT INTO user(username,address, mobile, email) VALUES (?,?,?,?)
                ON CONFLICT(username) DO UPDATE SET
                address = excluded.address,
                mobile = excluded.mobile,
                email = excluded.email;
                ''', (username, address, mobile, email)
            )
            self.conn.commit()
            return 'UPDATED'

    def list_all_users(self):
        sql = """SELECT username,address, mobile, email FROM user ORDER BY username"""
        dictionary = []
        with self.conn:
            curse = self.conn.cursor()
            curse.execute(sql)
            for row in curse.fetch():
                dictionary.append({
                    "username": row["username"],
                    "address": row["address"],
                    "mobile": row["mobile"],
                    "email": row["email"]
                })
        return dictionary

    def close(self):
        self.conn.close()


def main():
    # print(os.getcwd())
    # process_student_records("students.csv", "summary.json")
    # convert_log_file("server_access.log",
    #                  "access_records.csv", "access_records.json")

    # exp = ExperimentSnapshot(
    #     experiment_id="EXP-2026-001",
    #     model_type="RandomForest",
    #     hyperparameters={"n_estimators": 100, "max_depth": 10},
    #     metrics={"accuracy": 0.942, "f1_score": 0.938},
    #     timestamp="2026-09-01 10:00:00"
    # )
    # save_experiment(exp, "experiment_01.pkl")

    # restored_exp = load_experiment("experiment_01.pkl")
    # print(restored_exp.model_type)                    # Output: RandomForest
    # print(restored_exp.get_best_metric("accuracy"))   # Output: 0.942

    db = UserDatabaseManager("company.sqlite")
    status1 = db.add_or_update_user(
        "arham_k", "Pune, MH", "9876543210", "arham@cdac.in")

    print(status1)  # Output: INSERTED

    # Search user
    user_info = db.find_user("arham_k")
    print(user_info["email"])  # Output: arham@cdac.in

    # Update existing user
    status2 = db.add_or_update_user(
        "arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
    print(status2)  
    db.close()


if __name__ == "__main__":
    main()
