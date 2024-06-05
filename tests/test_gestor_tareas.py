# tests/test_gestor_tareas.py

import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
        self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")

    def test_agregar_tarea_sin_titulo(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Descripción")

    def test_ver_tareas_vacio(self):
        self.assertEqual(self.gestor.ver_tareas(), [])

    def test_ver_tareas_con_tareas(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.agregar_tarea("Tarea 2", "Descripción de la tarea 2")
        tareas = self.gestor.ver_tareas()
        self.assertEqual(len(tareas), 2)
        self.assertEqual(tareas[0].titulo, "Tarea 1")
        self.assertEqual(tareas[0].descripcion, "Descripción de la tarea 1")
        self.assertEqual(tareas[1].titulo, "Tarea 2")
        self.assertEqual(tareas[1].descripcion, "Descripción de la tarea 2")

    def test_marcar_tarea_como_completada(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.marcar_tarea_completada(0)
        self.assertTrue(self.gestor.tareas[0].completada)

    def test_marcar_tarea_como_completada_indice_invalido(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        with self.assertRaises(IndexError):
            self.gestor.marcar_tarea_completada(1)

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.agregar_tarea("Tarea 2", "Descripción de la tarea 2")
        self.gestor.eliminar_tarea(0)
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 2")

    def test_eliminar_tarea_indice_invalido(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        with self.assertRaises(IndexError):
            self.gestor.eliminar_tarea(1)

if __name__ == "__main__":
    unittest.main()


