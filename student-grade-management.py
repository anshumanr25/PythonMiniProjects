# Initialising Dictionary
student_grades = {}


# Add new Student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student {name} with grade {grade} is successfully added.")


# Update Student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student {name}'s marks are updated to {grade}.")

    else:
        print(f"{name} not found.\nPlease enter a valid name.")


# Delete Student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name}'s record successfully deleted.")
    else:
        print(f"{name} not found.\nPlease enter a valid name.")


# View all Students
def display_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No records found/added...")


def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View student")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            display_students()

        elif choice == 5:
            print("Thank you for visiting")
            break

        else:
            print("Invalid choice...")


main()
