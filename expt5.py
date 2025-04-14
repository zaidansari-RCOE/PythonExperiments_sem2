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
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Sort Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task_name = input("Enter the task: ")
        tasks.append((task_name,))
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task[0]}")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task[0]}")
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: {removed[0]}")

    elif choice == "4":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task[0]}")
        task_num = int(input("Enter task number to update: "))
        new_task = input("Enter the new task: ")
        tasks[task_num - 1] = (new_task,)
        print("Task updated!")

    elif choice == "5":
        tasks.sort()
        print("Tasks sorted alphabetically.")

    elif choice == "6":
        print("Exiting Task List Manager. Goodbye!")
        break

    else:
        print("Invalid choice.")

'''Output:
*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 1
Enter the task: Buy groceries
Task added!

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 1
Enter the task: Finish homework
Task added!

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 2

Your Tasks:
1. Buy groceries
2. Finish homework

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 4
1. Buy groceries
2. Finish homework
Enter task number to update: 2
Enter the new task: Finish math homework
Task updated!

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 2

Your Tasks:
1. Buy groceries
2. Finish math homework

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 5
Tasks sorted alphabetically.

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 2

Your Tasks:
1. Buy groceries
2. Finish math homework

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 3
1. Buy groceries
2. Finish math homework
Enter task number to remove: 1
Removed task: Buy groceries

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 2

Your Tasks:
1. Finish math homework

*** TASK LIST MANAGER ***
1. Add Task
2. View Tasks
3. Remove Task
4. Update Task
5. Sort Tasks
6. Exit
Enter your choice (1-6): 6
Exiting Task List Manager. Goodbye!
'''
