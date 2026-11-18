# Student Task Manager: User Guide

This guide explains how to use the Student Task Manager console app.

## Starting the app

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu appears:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
0. Exit
```

Type the number of an option and press **Enter**.

## 1. Add a task

1. Choose `1`.
2. Type the task title, for example `Math homework`, and press Enter.

```
Enter task title: Math homework
Task added: [1] Math homework (Pending)
```

Each task gets a number (its **id**), shown in square brackets. You use this id to complete or delete the task.

If you press Enter without typing a title, the app shows `Error: Task title cannot be empty.`
and asks `Try again? (y/n)`. Type `y` to try again or `n` to cancel.

## 2. Display tasks

Choose `2` to see all tasks and their status:

```
Your tasks:
  [1] Math homework (Done)
  [2] Lab report (Pending)
```

## 3. Complete tasks

1. Choose `3`. Your tasks are listed.
2. Type the id of the task to complete. To complete several tasks at once, separate the ids with commas, for example `1,3`.

```
Enter the id(s) of the task(s) to complete, separated by commas (e.g. 1,3): 1,3
Marked as completed: [1, 3]
```

The app also tells you about ids that were already completed or that do not exist.
If you type something that is not a number, nothing is changed and an error is shown.

## 4. Delete a task

1. Choose `4`. Your tasks are listed.
2. Type the id of the task to delete.
3. Confirm with `y` (or type `n` to cancel).

```
Enter the id of the task to delete: 2
Delete [2] Lab report (Pending)? (y/n): y
Task deleted.
```

Invalid ids (letters, or a number that matches no task) show an error and nothing is deleted.

## 0. Exit

Choose `0` to close the app. Your tasks are saved automatically in `tasks.json`
and are loaded again the next time you start the app.

## Tips

- To start with an empty list, close the app and delete `tasks.json`.
- `tasks.json` is listed in `.gitignore`, so your personal tasks are never committed to Git.
