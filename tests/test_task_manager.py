"""Unit tests for the Student Task Manager."""

import os
import tempfile
import unittest

from task_manager import TaskManager


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Math homework")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Math homework")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_task_trims_spaces(self):
        task = self.manager.add_task("   Read notes   ")
        self.assertEqual(task.title, "Read notes")

    def test_add_empty_title_is_rejected(self):
        for title in ["", "   "]:
            with self.assertRaises(ValueError):
                self.manager.add_task(title)
        self.assertEqual(self.manager.get_tasks(), [])


class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task("Math homework")
        self.manager.add_task("Lab report")
        self.manager.add_task("Essay")

    def test_complete_task(self):
        self.assertTrue(self.manager.complete_task(1))
        self.assertTrue(self.manager.find_task(1).completed)
        self.assertFalse(self.manager.find_task(2).completed)

    def test_complete_unknown_task(self):
        self.assertFalse(self.manager.complete_task(99))

    def test_complete_selected_tasks(self):
        self.manager.complete_task(2)
        result = self.manager.complete_tasks([1, 2, 7])
        self.assertEqual(result["completed"], [1])
        self.assertEqual(result["already_done"], [2])
        self.assertEqual(result["not_found"], [7])
        self.assertFalse(self.manager.find_task(3).completed)


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task("Math homework")
        self.manager.add_task("Lab report")

    def test_delete_task(self):
        self.assertTrue(self.manager.delete_task(1))
        self.assertIsNone(self.manager.find_task(1))
        self.assertEqual(len(self.manager.get_tasks()), 2)

    def test_delete_unknown_task(self):
        self.assertFalse(self.manager.delete_task(5))
        self.assertEqual(len(self.manager.get_tasks()), 2)

    def test_delete_invalid_id_is_rejected(self):
        for bad_id in ["1", 0, -1, 1.5, True]:
            with self.assertRaises(ValueError):
                self.manager.delete_task(bad_id)
        self.assertEqual(len(self.manager.get_tasks()), 2)


class TestPersistence(unittest.TestCase):
    def test_tasks_are_saved_and_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "tasks.json")
            manager = TaskManager(path)
            manager.add_task("Math homework")
            manager.complete_task(1)

            reloaded = TaskManager(path)
            self.assertEqual(len(reloaded.get_tasks()), 1)
            self.assertTrue(reloaded.find_task(1).completed)
            self.assertEqual(reloaded.add_task("Essay").id, 2)


if __name__ == "__main__":
    unittest.main()
