# studenttaskmanager

A Student Task Manager App made as a semester project.

A simple Python console application that helps students keep track of their tasks.

Project status: Testing

## Features

- Add a task
- Display all tasks with their status (Pending / Done)
- Mark a task as completed
- Delete a task
- Tasks are saved to `tasks.json` and reloaded when the app starts

## Requirements

- Python 3.8 or newer (no external packages needed)

## How to run

```bash
python main.py
```

On Windows you can also use `py main.py`.

## Project structure

| File | Purpose |
|------|---------|
| `task_manager.py` | `Task` and `TaskManager` classes (core logic) |
| `main.py` | Console menu |
