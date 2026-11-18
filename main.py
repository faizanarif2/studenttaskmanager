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
    if not manager.get_tasks():
        print("No tasks to complete.")
        return
    display_tasks(manager)
    text = input("Enter the id(s) of the task(s) to complete, separated by commas (e.g. 1,3): ")

    task_ids = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if not part.isdigit():
            print(f"Error: '{part}' is not a valid task id. Nothing was changed.")
            return
        task_ids.append(int(part))

    if not task_ids:
        print("Error: no task id entered.")
        return

    result = manager.complete_tasks(task_ids)
    if result["completed"]:
        print(f"Marked as completed: {result['completed']}")
    if result["already_done"]:
        print(f"Already completed: {result['already_done']}")
    if result["not_found"]:
        print(f"Not found: {result['not_found']}")


def delete_task(manager):
    if not manager.get_tasks():
        print("No tasks to delete.")
        return
    display_tasks(manager)
    text = input("Enter the id of the task to delete: ").strip()

    if not text.isdigit():
        print(f"Error: '{text}' is not a valid task id. Please enter a number.")
        return
    task_id = int(text)

    task = manager.find_task(task_id)
    if task is None:
        print(f"Error: no task with id {task_id}.")
        return

    confirm = input(f"Delete {task}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return

    try:
        manager.delete_task(task_id)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print("Task deleted.")


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
