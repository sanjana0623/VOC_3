#!/usr/bin/env python
# coding: utf-8

# # WEEK 3-> TASK: Develop a basic to-do list application using functions and data structure

# This enhanced to-do list application will load tasks from a file when it starts and save tasks to the same file when you add, complete, or remove tasks. This user-friendly to-do list application provides clear prompts, error handling, and feedback for the user, making it easier to manage tasks.

# In[1]:


# Define the filename for storing tasks
task_file = "tasks.txt"

# Function to load tasks from a file
def load_tasks():
    try:
        with open(task_file, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list of tasks
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open(task_file, "w") as file:
        file.write("\n".join(tasks))

# Function to add a task to the to-do list
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

# Function to view all tasks in the to-do list
def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nThe to-do list is empty.")

# Function to mark a task as completed
def complete_task(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"\nTask '{completed_task}' marked as completed.")
    else:
        print("\nInvalid task index. Please enter a valid task index.")

# Function to remove a task from the to-do list
def remove_task(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"\nTask '{removed_task}' removed from the to-do list.")
    else:
        print("\nInvalid task index. Please enter a valid task index.")

# Main function to start the to-do list application
def main():
    print("Welcome to the To-Do List App!")
    tasks = load_tasks()  # Load tasks from the file when the application starts

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
            print(f"\nTask '{task}' added to the to-do list.")
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == '5':
            print("Saving tasks and quitting...")
            save_tasks(tasks)  # Save tasks to the file before quitting
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




