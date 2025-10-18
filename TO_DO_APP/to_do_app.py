# to_do_app.py
# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n==== To-Do List Menu ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task name: ")
        tasks.append(task)
        print(f"✅ '{task}' added to your To-Do list.")
        
    elif choice == '2':
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
    elif choice == '3':
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"❌ '{removed}' removed from the list.")
        else:
            print("Invalid task number.")
            
    elif choice == '4':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Try again.")
