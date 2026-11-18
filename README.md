# studenttaskmanager

![Tests](https://github.com/faizanarif2/studenttaskmanager/actions/workflows/tests.yml/badge.svg)

A Student Task Manager App made as a semester project.

A simple Python console application that helps students keep track of their tasks.

Project status: Released (v1.0.0)

## Features

- **Add tasks**: empty or blank titles are rejected, and extra spaces are trimmed
- **Display tasks** with their status (Pending / Done)
- **Complete tasks**: mark one or several selected tasks as completed (e.g. `1,3`)
- **Delete tasks**: only with a valid task id, with a confirmation prompt
- **Input validation**: invalid input shows an error instead of crashing the app
- **Saved automatically** to `tasks.json` and reloaded when the app starts
- **Automated tests** with `unittest`, run by GitHub Actions on every push and Pull Request to `main`

## Setup

1. Install Python 3.8 or newer (no external packages are needed).
2. Clone the repository:

   ```bash
   git clone https://github.com/faizanarif2/studenttaskmanager.git
   cd studenttaskmanager
   ```

## Usage

Start the app:

```bash
python main.py
```

On Windows you can also use `py main.py`.

Choose an option from the menu:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
0. Exit
```

See the [User Guide](docs/userguide.md) for step-by-step examples.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically in GitHub Actions (`.github/workflows/tests.yml`)
on every push to `main` and on every Pull Request to `main`.

## Project structure

| File | Purpose |
|------|---------|
| `task_manager.py` | `Task` and `TaskManager` classes (core logic) |
| `main.py` | Console menu |
| `tests/test_task_manager.py` | Unit tests |
| `.github/workflows/tests.yml` | GitHub Actions workflow |
| `docs/userguide.md` | User guide |

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
