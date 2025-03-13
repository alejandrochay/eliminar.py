class Tarea:
    def __init__(self, id_tarea, descripcion, prioridad):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __eq__(self, otro):
        if isinstance(otro, Tarea):
            return self.id_tarea == otro.id_tarea
        return False

class GestorTareas:
    def __init__(self):
        self.tareas = {}

    def agregar_tarea(self, tarea):
        self.tareas[tarea.id_tarea] = tarea

    def eliminar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            del self.tareas[id_tarea]
            return True
        return False

    def buscar_tarea(self, id_tarea):
        """Busca una tarea por su ID y la devuelve."""
        return self.tareas.get(id_tarea, None)

    def listar_tareas(self, filtrar_completadas=True):
        if filtrar_completadas:
            return list(self.tareas.values())
        return [tarea for tarea in self.tareas.values() if not tarea.completada]

    def filtrar_por_prioridad(self, prioridad):
        if prioridad not in ["alta", "normal", "baja"]:
            raise ValueError("Prioridad no válida")
        return [tarea for tarea in self.tareas.values() if tarea.prioridad == prioridad]

    def validar_prioridad(self, prioridad):
        if prioridad not in ["alta", "normal", "baja"]:
            raise ValueError("Prioridad no válida")