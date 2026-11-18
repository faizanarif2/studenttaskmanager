"""Core logic for the Student Task Manager."""

import json
import os


class Task:
    """A single task with an id, a title and a completion status."""

    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data.get("completed", False))

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} ({status})"


class TaskManager:
    """Stores tasks and provides operations on them.

    If storage_file is given, tasks are loaded from and saved to that JSON
    file. If it is None, tasks are kept in memory only (useful for tests).
    """

    def __init__(self, storage_file=None):
        self.storage_file = storage_file
        self.tasks = []
        self.next_id = 1
        self.load()

    def load(self):
        """Load tasks from the storage file, if it exists."""
        if not self.storage_file or not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = [Task.from_dict(item) for item in data]
        if self.tasks:
            self.next_id = max(task.id for task in self.tasks) + 1

    def save(self):
        """Write all tasks to the storage file."""
        if not self.storage_file:
            return
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, title):
        """Create a new task and return it."""
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
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
        self.save()
        return True

    def delete_task(self, task_id):
        """Remove a task. Return True if the task was found."""
        # A valid identifier must be a positive whole number.
        if isinstance(task_id, bool) or not isinstance(task_id, int):
            raise ValueError("Task id must be a whole number.")
        if task_id < 1:
            raise ValueError("Task id must be a positive number.")

        task = self.find_task(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        self.save()
        return True
