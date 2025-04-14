''' Title:Task List Manager
    Name:Md. Zaid Mashooque Ansari
    Division:C
    UIN:241P057
    Roll no:51'''
tasks = []

while True:
    print("\n*** TASK LIST MANAGER ***")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"Deleted task: {removed}")

    elif choice == "4":
        print("Exiting Task List Manager. Goodbye!")
        break

    else:
        print("Invalid choice.")

'''Output:
*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 1
Enter the task: Buy groceries
Task added!

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 1
Enter the task: Finish math homework
Task added!

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 2

Your Tasks:
1. Buy groceries
2. Finish math homework

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 3
1. Buy groceries
2. Finish math homework
Enter task number to delete: 1
Deleted task: Buy groceries

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 2

Your Tasks:
1. Finish math homework

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 4
Exiting Task List Manager. Goodbye!
,,,
