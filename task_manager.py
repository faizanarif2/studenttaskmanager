"""Core logic for the Student Task Manager."""


class Task:
    """A single task with an id, a title and a completion status."""

    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} ({status})"


class TaskManager:
    """Stores tasks and provides operations on them."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """Create a new task and return it."""
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        """Return a copy of the task list."""
        return list(self.tasks)

    def find_task(self, task_id):
        """Return the task with the given id, or None if it does not exist."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """Mark a task as completed. Return True if the task was found."""
        task = self.find_task(task_id)
        if task is None:
            return False
        task.completed = True
        return True

    def delete_task(self, task_id):
        """Remove a task. Return True if the task was found."""
        task = self.find_task(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        return True
