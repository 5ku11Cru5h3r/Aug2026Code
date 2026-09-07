import json

jsonfile = __file__+"student.json"
students = [
    {"id": 1, "name": "Aarav Sharma",
     "course": "Python Core", "marks": 88.5, "grade": "A"},
    {"id": 2, "name": "Diya Patel",
     "course": "Data Science", "marks": 74.0, "grade": "B"}
]

# id_ = max([x["id"] for x in students], default=0) + 1
id = 3


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


def student_enrollment():
    global id
    while True:
        id += 1
        _id = id
        try:
            name = input("Enter student name:")
            while name.strip() == "":
                print("Enter valid Name")
                name = input("Enter student name:")
        except ValueError:
            print("Value must be a String")
             
        try:
            course = input("Enter student course:")
            while course.strip() == "":
                print("Enter valid Course Name")
                course = input("Enter student course:")    
        except ValueError:
            print("Value must be a String")

        while True:
            try:
                marks = float(input("Enter Marks:   "))
                if marks <= 0 or marks > 100:
                    print("Marks must be valid")
                    continue
                break
            except ValueError:
                print("MArks must be an Number")

        grade = grade_generation(marks)
        students.append(dict(id=_id, name=name, course=course,
                    marks=marks, grade=grade))
        print(f"\nProduct Added with id: {_id}")
        choice = input("Do you want to to add more book [y/n]: ")
        if choice != 'y':
            break

def print_many_student(students):
    print("-"*80)
    print(f"{'ID':^5} {'Candidate name':<25} {'Course':<25} {'Marks':<15} {'Grade':<15}")
    print("-"*80)
    
    for s in students:
        id, name, course, marks, grade = s.values()
        print(f"{id:^5} {name:<25} {course:<25} {marks:<15} {grade:<15}")
    print("-"*80)
    
def print_one_student(students):
    id, name, course, marks, grade = students.values()
    
    print(f"ID:       {id}")
    print(f"Name:       {name}")
    print(f"Course:       {course}")
    print(f"marks:       {marks}")
    print(f"Grade:       {grade}")
        
    
def cohort_student(students):
    if len(students) == 0:
        print("No Student Found")
    elif len(students) == 1:
        print_one_student(students[0])
    else:
        print_many_student(students)

def query_record():
    result = []
    search_item = input("Enter the item to search for:  ")
    
    if search_item.isdigit():
        search_term = int(search_item)
        
        student = [s for s in students if s['id'] == search_term]
    
        if not student:
            print("No Record Found")
    
        result.append(student)
        return result
    else:
        search_term = search_item.strip().lower()
        
        for s in students:
            if search_term in s['name']:
                result.append(s)
        return result

def revise_evaluation():
    edit_id = int(input("Enter the Id you want to edit:  "))
    
    student = [s for s in students if s['id'] == edit_id]
    
    if not student:
        print(f"Student with {edit_id} not found")
        
    student = student[0]

    try:
        _name = input(f"Enter new name [{student['name']}]: ")
        if _name.strip() != "":
            student['name'] = _name
    except ValueError:
        print("Value must be a String")
        
        try:
            _course = input("Enter student course:")
            if _course.strip() != "":
                student['course'] = _course 
        except ValueError:
            print("Value must be a String")
            
    while True:
        marks_input = input(f"Enter new marks [{student['marks']}]: ").strip()
        
        if marks_input == "":
            break
        
        try:
            marks = float(marks_input)

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100")
                continue

            student["marks"] = marks
            student["grade"] = grade_generation(marks)
            break

        except ValueError:
            print("Marks must be a number")
            
    print("Student record updated successfully.")
           
def purge_record():
    del_id = int(input("Enter the Id to be deleted:   "))
    
    student = [s for s in students if s['id'] == del_id]
    
    if not student:
        print("Student not found to be deleted")
        
    student = student[0]
    
    ans = input("Are you sure you want to delete the student: [y/n]:  ")
    
    if ans.strip().lower() == 'y':
        students.remove(student)
    else:
        print("Student Not deleted!!")
    
def save_to_json():
    with open('students.json', 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=4)
        
def load_from_json():
    with open('students.json', 'r', encoding='utf-8') as f:
        result = json.load(f)
    print(result)

def main():

    # print(id_)

    while True:
        choice = menu()
        match choice:
            case 1:
                student_enrollment()
            case 2:
                cohort_student(students)
            case 3: 
                result = query_record()
                if len(result) == 0:
                    print("No Record Found")
                else:
                    cohort_student(result)
            case 4:
                revise_evaluation()
            case 5:
                purge_record()
            case 6:
                save_to_json()
            case 7:
                load_from_json( )
            case 8:
                break
    print("Bye!")

    ...


if __name__ == "__main__":
    main()
