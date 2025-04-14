''' Title:Student Enrollment Manager
    Name:Md. Zaid Mashooque Ansari
    Division:C
    UIN:241P057
    Roll no:51'''

cet_students = {"Ayaan", "Zara", "Vikram", "Priya", "Ravi", "Fatima", "Saanvi"}
jee_students = {"Fatima", "Zara", "Ali", "Ananya", "Ayaan", "Ravi", "Kartik"}
neet_students = {"Kartik", "Vikram", "Saanvi", "Fatima", "Ayaan", "Simran"}

while True:
    print("\n*** STUDENT ENROLLMENT MANAGER ***")
    print("1. View Students in CET")
    print("2. View Students in JEE")
    print("3. View Students in NEET")
    print("4. Union of Students (All Students Enrolled in any Exam)")
    print("5. Intersection of Students (Students Enrolled in All Exams)")
    print("6. Difference of Students (Students Enrolled in CET but not in JEE or NEET)")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        print("\nStudents enrolled in CET:", cet_students)
    
    elif choice == "2":
        print("\nStudents enrolled in JEE:", jee_students)
    
    elif choice == "3":
        print("\nStudents enrolled in NEET:", neet_students)
    
    elif choice == "4":
        # Union: All students who are enrolled in at least one of the exams
        all_students = cet_students.union(jee_students, neet_students)
        print("\nAll Students Enrolled in any Exam:", all_students)
    
    elif choice == "5":
        # Intersection: Students enrolled in all exams
        common_students = cet_students.intersection(jee_students, neet_students)
        print("\nStudents Enrolled in All Exams:", common_students)
    
    elif choice == "6":
        # Difference: Students enrolled in CET but not in JEE or NEET
        cet_only_students = cet_students.difference(jee_students, neet_students)
        print("\nStudents Enrolled in CET but not in JEE or NEET:", cet_only_students)
    
    elif choice == "7":
        print("Exiting Student Enrollment Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

'''
Sample Output:

*** STUDENT ENROLLMENT MANAGER ***
1. View Students in CET
2. View Students in JEE
3. View Students in NEET
4. Union of Students (All Students Enrolled in any Exam)
5. Intersection of Students (Students Enrolled in All Exams)
6. Difference of Students (Students Enrolled in CET but not in JEE or NEET)
7. Exit
Enter your choice (1-7): 1

Students enrolled in CET: {'Ravi', 'Saanvi', 'Zara', 'Vikram', 'Ayaan', 'Fatima', 'Priya'}

*** STUDENT ENROLLMENT MANAGER ***
1. View Students in CET
2. View Students in JEE
3. View Students in NEET
4. Union of Students (All Students Enrolled in any Exam)
5. Intersection of Students (Students Enrolled in All Exams)
6. Difference of Students (Students Enrolled in CET but not in JEE or NEET)
7. Exit
Enter your choice (1-7): 4

All Students Enrolled in any Exam: {'Vikram', 'Saanvi', 'Fatima', 'Priya', 'Ayaan', 'Zara', 'Ravi', 'Ali', 'Ananya', 'Kartik'}

*** STUDENT ENROLLMENT MANAGER ***
1. View Students in CET
2. View Students in JEE
3. View Students in NEET
4. Union of Students (All Students Enrolled in any Exam)
5. Intersection of Students (Students Enrolled in All Exams)
6. Difference of Students (Students Enrolled in CET but not in JEE or NEET)
7. Exit
Enter your choice (1-7): 5

Students Enrolled in All Exams: {'Fatima', 'Ayaan'}

*** STUDENT ENROLLMENT MANAGER ***
1. View Students in CET
2. View Students in JEE
3. View Students in NEET
4. Union of Students (All Students Enrolled in any Exam)
5. Intersection of Students (Students Enrolled in All Exams)
6. Difference of Students (Students Enrolled in CET but not in JEE or NEET)
7. Exit
Enter your choice (1-7): 6

Students Enrolled in CET but not in JEE or NEET: {'Priya', 'Zara', 'Vikram'}

*** STUDENT ENROLLMENT MANAGER ***
1. View Students in CET
2. View Students in JEE
3. View Students in NEET
4. Union of Students (All Students Enrolled in any Exam)
5. Intersection of Students (Students Enrolled in All Exams)
6. Difference of Students (Students Enrolled in CET but not in JEE or NEET)
7. Exit
Enter your choice (1-7): 7
Exiting Student Enrollment Manager. Goodbye!
'''
