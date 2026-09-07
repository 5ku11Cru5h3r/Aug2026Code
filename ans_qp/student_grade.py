import json

jsonfile = __file__+"student.json"
students = [
    {"id": 1, "name": "Aarav Sharma",
     "course": "Python Core", "marks": 88.5, "grade": "A"},
    {"id": 2, "name": "Diya Patel",
     "course": "Data Science", "marks": 74.0, "grade": "B"}
]

id_ = max([x["id"] for x in students], default=0) + 1


def menu():
    menu_txt = '''
    1. Enroll Student
    2. Cohort Directory
    3. Query Record
    4. Revise Evaluation
    5. Purge Record
    6. Save to Json
    7. Load From Json
    8. Terminate'''

    print("="*80)
    print(f"{"STUDENT GRADE & ASSESSMENT MODULE":^80}")
    print("="*80)

    print(menu_txt)

    try:
        choice = int(input("Enter thr choice you want:   "))

        if choice < 0 or choice > 8:
            print("Choice must be between 1 and 8")
        return choice
    except ValueError:
        print("Choice must be an Number")


def grade_generation(marks):
    if marks >= 85:
        return "A"
    elif marks >= 75 and marks < 85:
        return "B"
    elif marks >= 50 and marks < 70:
        return "C"
    else:
        return "F"


def student_enrollment(catalog: list[dict]):

    name = input("Enter student name:")
    while name.strip() == "":
        print("Enter valid Name")
        name = input("Enter student name:")

    course = input("Enter student course:")
    while course.strip() == "":
        print("Enter valid Course Name")
        course = input("Enter student course:")

    try:
        while True:
            marks = float(input("Enter Marks:   "))
            if marks <= 0 or marks > 100:
                print("Marks must be valid")
                continue
            break
    except ValueError:
        print("MArks must be an Number")

    grade = grade_generation(marks)
    global _id
    catalog.append(dict(id=id_+1, name=name, course=course,
                   marks=marks, grade=grade))
    id_ += 1
    return catalog


# def cohort_student()


def main():

    # print(id_)

    while True:
        choice = menu()
        match choice:
            case 1:
                # global students
                student_enrollment(students)
            case 8:
                break
    print("Bye!")

    ...


if __name__ == "__main__":
    main()
