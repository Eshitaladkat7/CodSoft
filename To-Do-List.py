import os

# Function to display the menu
def display_menu():
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

# Function to view the current To-Do List
def view_todo_list():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            todo_list = file.readlines()
            if todo_list:
                for index, task in enumerate(todo_list, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("To-Do List is empty.")
    else:
        print("To-Do List is empty.")

# Function to add a task to the To-Do List
def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

# Function to mark a task as completed
def mark_completed():
    view_todo_list()
    choice = int(input("Enter the task number to mark as completed: "))
    with open("todo.txt", "r") as file:
        todo_list = file.readlines()
    if 1 <= choice <= len(todo_list):
        todo_list.pop(choice - 1)
        with open("todo.txt", "w") as file:
            file.writelines(todo_list)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task from the To-Do List
def delete_task():
    view_todo_list()
    choice = int(input("Enter the task number to delete: "))
    with open("todo.txt", "r") as file:
        todo_list = file.readlines()
    if 1 <= choice <= len(todo_list):
        todo_list.pop(choice - 1)
        with open("todo.txt", "w") as file:
            file.writelines(todo_list)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

# Main function to run the To-Do List application
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
