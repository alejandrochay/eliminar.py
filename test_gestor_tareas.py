import unittest
from gestor_tareas import GestorTareas, Tarea

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.manager = GestorTareas()
        self.tarea1 = Tarea(1, "Tarea 1", "alta")
        self.tarea2 = Tarea(2, "Tarea 2", "normal")
        self.manager.agregar_tarea(self.tarea1)
        self.manager.agregar_tarea(self.tarea2)

    def test_eliminar_tarea_exito(self):
        resultado = self.manager.eliminar_tarea(1)
        self.assertTrue(resultado)
        self.assertIsNone(self.manager.buscar_tarea(1))

    def test_eliminar_tarea_no_existente(self):
        resultado = self.manager.eliminar_tarea(3)
        self.assertFalse(resultado)

    def test_buscar_tarea_existente(self):
        tarea = self.manager.buscar_tarea(1)
        self.assertEqual(tarea, self.tarea1)

    def test_buscar_tarea_no_existente(self):
        tarea = self.manager.buscar_tarea(3)
        self.assertIsNone(tarea)

    def test_buscar_tareas_por_id(self):
        tarea_encontrada = self.manager.buscar_tarea(2)
        self.assertEqual(tarea_encontrada, self.tarea2)

    def test_marcar_tarea_completada(self):
        self.manager.buscar_tarea(1).marcar_completada()
        self.assertTrue(self.tarea1.completada)

    def test_marcar_tarea_no_existente(self):
        with self.assertRaises(KeyError):
            self.manager.buscar_tarea(3).marcar_completada()

    def test_listar_tareas(self):
        tareas = self.manager.listar_tareas()
        self.assertEqual(len(tareas), 2)

    def test_listar_tareas_pendientes(self):
        self.tarea1.marcar_completada()
        tareas = self.manager.listar_tareas(filtrar_completadas=False)
        self.assertEqual(len(tareas), 1)

    def test_filtrar_por_prioridad(self):
        tareas = self.manager.filtrar_por_prioridad("alta")
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0], self.tarea1)

    def test_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            self.manager.validar_prioridad("media")

    def test_comparacion_personalizada(self):
        # Prueba de igualdad
        tarea3 = Tarea(1, "Tarea 3", "baja")
        self.assertEqual(self.tarea1, tarea3)  # Debe ser igual
        self.assertNotEqual(self.tarea1, self.tarea2)  # No debe ser igual

    def test_eq_tarea(self):
        tarea_a = Tarea(1, "Tarea A", "alta")
        tarea_b = Tarea(1, "Tarea B", "normal")
        tarea_c = Tarea(2, "Tarea C", "baja")

        self.assertEqual(tarea_a, tarea_b)  # Mismo ID, deben ser iguales
        self.assertNotEqual(tarea_a, tarea_c)  # Diferente ID, no deben ser iguales

if __name__ == '__main__':
    unittest.main()