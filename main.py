"""Console interface for the Student Task Manager."""

from task_manager import TaskManager


MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
0. Exit
"""


def add_task(manager):
    title = input("Enter task title: ")
    task = manager.add_task(title)
    print(f"Task added: {task}")


def display_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour tasks:")
    for task in tasks:
        print(f"  {task}")


def main():
    manager = TaskManager()
    actions = {
        "1": add_task,
        "2": display_tasks,
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
