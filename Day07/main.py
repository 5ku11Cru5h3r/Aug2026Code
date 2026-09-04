import os
import csv
import json
from pathlib import Path
# from pprint import pprint
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


def main():
    # print(os.getcwd())
    # process_student_records("students.csv", "summary.json")
    convert_log_file("server_access.log",
                     "access_records.csv", "access_records.json")
    ...


if __name__ == "__main__":
    main()
