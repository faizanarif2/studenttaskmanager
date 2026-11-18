"""Console interface for the Student Task Manager."""

from task_manager import TaskManager

DATA_FILE = "tasks.json"

MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
0. Exit
"""


def add_task(manager):
    while True:
        title = input("Enter task title: ")
        try:
            task = manager.add_task(title)
        except ValueError as error:
            print(f"Error: {error}")
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != "y":
                print("Add task cancelled.")
                return
            continue
        print(f"Task added: {task}")
        return


def display_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour tasks:")
    for task in tasks:
        print(f"  {task}")


def complete_task(manager):
    display_tasks(manager)
    task_id = int(input("Enter the id of the task to complete: "))
    if manager.complete_task(task_id):
        print("Task marked as completed.")
    else:
        print("Task not found.")


def delete_task(manager):
    display_tasks(manager)
    task_id = int(input("Enter the id of the task to delete: "))
    if manager.delete_task(task_id):
        print("Task deleted.")
    else:
        print("Task not found.")


def main():
    manager = TaskManager(DATA_FILE)
    actions = {
        "1": add_task,
        "2": display_tasks,
        "3": complete_task,
        "4": delete_task,
    }

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
