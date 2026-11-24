tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
            continue

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
