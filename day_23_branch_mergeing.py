import json
import os

File_Name = "tasks.json"

"""load task from file!"""
def load_tasks():
    if os.path.exists(File_Name):
        with open(File_Name, 'r') as f:
            return json.load(f)
    return []

"""save tasks to file"""
def save_tasks(tasks):
    with open(File_Name, 'w') as f:
        json.dump(tasks, f, indent= 4)

"""Add a new task"""
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})  
    save_tasks(tasks)
    print(f"Task Added: {task}")

"""view all the tasks"""
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found')
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{idx}. {task['task']} - {status}")
        
"""Main"""
def main():
    while True:
        print("\n---- To-Do List Manager ----")
        print("1. Add Task")
        print("2. View Task")
        print("3. Exit")

        choice = input("Enter the Choice: ")

        if choice == "1":
            task = input('Enter The Task: ')
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting To-Do List Manager...")
            break
        else:
            print("Invalid Choice try again")

if __name__ == "__main__":
    main()