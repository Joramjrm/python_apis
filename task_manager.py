import os
from datetime import datetime

Tasks_file = "tasks.txt"
Users_file = "users.txt"

'''login to user with username and password'''

def login():
    print("Please login:")
    username = input("Username: ")
    password = input("Password: ")
    with open(Users_file, 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                return True
    print("Invalid username or password.")
    return False

'''shows leters that represent what the user wants to view'''

def display_main_menu():
    print("Main Menu:")
    print("r: Register a new user")
    print("a: Add a new task")
    print("va: View all tasks")
    print("vm: View tasks assigned to you")

'''add task to a certain user'''

def add_task():
    assigned_user = input("Enter assigned user's username: ")
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    assignment_date = datetime.now().strftime("%Y-%m-%d")
    completion_status = "No"
    with open(Tasks_file, 'a') as file:
        file.write(f"{assigned_user},{task_title},{task_description},{assignment_date},{due_date},{completion_status}")
    print("Task added successfully.")

'''display the task according to user'''

def view_tasks(username=None):
    print("Tasks:")
    with open(Tasks_file, 'r') as file:
        for line in file:
            task_info = line.strip().split(',')
            if not username or username == task_info[0]:
                print_task(task_info)

'''displays the task_infomation'''

def print_task(task_info):
    assigned_user, task_title, task_description, assignment_date, due_date, completion_status = task_info
    print(f"Assigned User: {assigned_user}")
    print(f"Title: {task_title}")
    print(f"Description: {task_description}")
    print(f"Assignment Date: {assignment_date}")
    print(f"Due Date: {due_date}")
    print(f"Completion Status: {'Completed' if completion_status == 'Yes' else 'Not Completed'}")

'''allows only admin to add a user'''

def register_user():
    if current_user != 'admin':
        print("You don't have permission to register a new user.")
        return

    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")
    if new_password == confirm_password:
        with open(Users_file, 'a') as file:
            file.write(f"{new_username},{new_password}")
        print("User registered successfully.")
    else:
        print("Passwords do not match.")

def display_statistics():
    if current_user != 'admin':
        print("You don't have permission to view statistics.")
        return

    task_count = sum(1 for line in open(Tasks_file))
    user_count = sum(1 for line in open(Users_file))
    print(f"Total number of tasks: {task_count}")
    print(f"Total number of users: {user_count}")

def save_changes():
    pass

if not os.path.exists(Tasks_file):
    with open(Tasks_file, 'w'): pass

if not os.path.exists(Users_file):
    with open(Users_file, 'w') as file:
        file.write("admin,adm1n")

login_success = False
while not login_success:
    login_success = login()

'''display according to your choice'''

current_user = None
if login_success:
    while True:
        display_main_menu()
        choice = input(f"Enter your choice: ")
        if choice == 'a':
            add_task()
        elif choice == 'va':
            view_tasks()
        elif choice == 'vm':
            view_tasks(current_user)
        elif choice == 'r':
            register_user()
        elif choice == 'stats':
            display_statistics()
        else:
            print("Invalid choice.")
            continue

        save_changes()

        exit_choice = input("Do you want to exit? (y/n): ")
        if exit_choice.lower() == 'y':
            break