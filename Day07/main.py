import csv
import json


in_path = "students.csv"
out_path = "summary.json"


def process_student_records(input_csv_path=in_path, output_json_path=out_path):

    with open(input_csv_path, "r") as csvfile:
        csvr = csv.DictReader(csvfile)
        dict_list = []
        with open(output_json_path, "w", encoding="utf-8") as jsonfile:
            for line in csvr:
                dict_list.append(line)
            json.dump(dict_list, jsonfile, indent=3)

    print(f"Data Saved in {output_json_path}")

    ...


def main():
    process_student_records("students.csv", "summary.json")
    ...


if __name__ == "__main__":
    main()
