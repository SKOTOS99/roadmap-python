import unittest

from backend.app import app, service
from backend.service.TaskService import TaskService


class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        service = TaskService()
        self.app = app.test_client()
        self.app.testing = True
        service.task = []  # Reinicia las tareas para cada prueba

    def test_get_all_tasks(self):
        response = self.app.get('/api/tareas')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        task = {
            "ids": 1,
            "tittle": "Tarea 1",
            "description": "Descripción de la tarea 1",
            "active": True
        }
        response = self.app.post('/api/tareas', json=task)
        self.assertEqual(response.status_code, 201)

    def test_get_task_by_id(self):
        service.add_task({"ids": 1, "tittle": "Tarea 1", "description": "Descripción", "active": True})
        response = self.app.get('/api/tareas/1')
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        service.add_task({"ids": 1, "tittle": "Tarea 1", "description": "Descripción", "active": True})
        updated_task = {"tittle": "Tarea Actualizada", "description": "Nueva descripción", "active": False}
        response = self.app.put('/api/tareas/1', json=updated_task)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        service.add_task({"ids": 1, "tittle": "Tarea 1", "description": "Descripción", "active": True})
        response = self.app.delete('/api/tareas/1')
        self.assertEqual(response.status_code, 201)
