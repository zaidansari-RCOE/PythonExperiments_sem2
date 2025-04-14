''' Title:Student Record Keeper
    Name:Md. Zaid Mashooque Ansari
    Division:C
    UIN:241P057
    Roll no:51'''
# Student Record Keeper Program

# Initialize an empty dictionary to store student records
students = {}

# Function to add a student record
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    attendance = int(input("Enter student attendance percentage: "))

    # Adding student record to the dictionary
    students[student_id] = {
        'name': name,
        'grade': grade,
        'attendance': attendance
    }
    print(f"Student {name} added successfully!")

# Function to update a student's record
def update_student():
    student_id = input("Enter student ID to update: ")
    
    if student_id in students:
        name = input(f"Enter new name for {students[student_id]['name']} (press enter to keep current): ")
        if name:
            students[student_id]['name'] = name
        
        grade = input(f"Enter new grade for {students[student_id]['grade']} (press enter to keep current): ")
        if grade:
            students[student_id]['grade'] = grade
        
        attendance = input(f"Enter new attendance for {students[student_id]['attendance']} (press enter to keep current): ")
        if attendance:
            students[student_id]['attendance'] = int(attendance)
        
        print(f"Student record for {student_id} updated successfully!")
    else:
        print("Student ID not found!")

# Function to view a student's record
def view_student():
    student_id = input("Enter student ID to view: ")
    
    if student_id in students:
        student = students[student_id]
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Grade: {student['grade']}")
        print(f"Attendance: {student['attendance']}%")
    else:
        print("Student ID not found!")

# Function to delete a student's record
def delete_student():
    student_id = input("Enter student ID to delete: ")
    
    if student_id in students:
        del students[student_id]
        print(f"Student record for {student_id} deleted successfully!")
    else:
        print("Student ID not found!")

# Function to display all students
def view_all_students():
    if students:
        print("\nAll Students Records:")
        for student_id, student in students.items():
            print(f"\nStudent ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Grade: {student['grade']}")
            print(f"Attendance: {student['attendance']}%")
    else:
        print("No student records available.")

# Main menu for user interaction
def main_menu():
    while True:
        print("\n*** STUDENT RECORD KEEPER ***")
        print("1. Add Student Record")
        print("2. Update Student Record")
        print("3. View Student Record")
        print("4. Delete Student Record")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            view_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            view_all_students()
        elif choice == "6":
            print("Exiting Student Record Keeper. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
main_menu()
'''Output:
*** STUDENT RECORD KEEPER ***
1. Add Student Record
2. Update Student Record
3. View Student Record
4. Delete Student Record
5. View All Students
6. Exit
Enter your choice (1-6): 1
Enter student ID: 101
Enter student name: John Doe
Enter student grade: A
Enter student attendance percentage: 90
Student John Doe added successfully!

*** STUDENT RECORD KEEPER ***
1. Add Student Record
2. Update Student Record
3. View Student Record
4. Delete Student Record
5. View All Students
6. Exit
Enter your choice (1-6): 3
Enter student ID to view: 101

Student ID: 101
Name: John Doe
Grade: A
Attendance: 90%

*** STUDENT RECORD KEEPER ***
1. Add Student Record
2. Update Student Record
3. View Student Record
4. Delete Student Record
5. View All Students
6. Exit
Enter your choice (1-6): 2
Enter student ID to update: 101
Enter new name for John Doe (press enter to keep current): Johnathan Doe
Enter new grade for A (press enter to keep current): A+
Enter new attendance for 90 (press enter to keep current): 95
Student record for 101 updated successfully!

*** STUDENT RECORD KEEPER ***
1. Add Student Record
2. Update Student Record
3. View Student Record
4. Delete Student Record
5. View All Students
6. Exit
Enter your choice (1-6): 3
Enter student ID to view: 101

Student ID: 101
Name: Johnathan Doe
Grade: A+
Attendance: 95%

*** STUDENT RECORD KEEPER ***
1. Add Student Record
2. Update Student Record
3. View Student Record
4. Delete Student Record
5. View All Students
6. Exit
Enter your choice (1-6): 4
Enter student ID to delete: 101
Student record for 101 deleted successfully!

*** STUDENT RECORD KEEPER ***
1. Add Student Record
2. Update Student Record
3. View Student Record
4. Delete Student Record
5. View All Students
6. Exit
Enter your choice (1-6): 6
Exiting Student Record Keeper. Goodbye!
'''
