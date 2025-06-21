tasks = []

def show_menu():
    print("\nTo-Do List Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def todo_app():
    while True:
        show_menu()
        choice = input("Enter Your Choice (1-2-3-4): ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            print("Task is added...")

        elif choice == '2':
            if not tasks:
                print(" Your To-Do List is empty!!")
            else:
                print("\nTo-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == '3':
            if not tasks:
                print("Your To-Do List is empty, Nothing to remove!!")
            else:
                try:
                    task_num = int(input("Enter task number that you want to remove: "))
                    if 0 < task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed Task: {removed}")
                    else:
                        print("You entered invalid task number!!")
                except ValueError:
                    print("Please enter a valid number!!")

        elif choice == '4':
            print("Exit...")
            break

        else:
            print("Invalid choice!!")

todo_app()
