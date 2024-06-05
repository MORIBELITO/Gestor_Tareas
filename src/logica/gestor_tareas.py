
class Tarea:
    def __init__(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título de la tarea no puede estar vacío")
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)

    def ver_tareas(self):
        return self.tareas

    def marcar_tarea_completada(self, indice):
        if indice < 0 or indice >= len(self.tareas):
            raise IndexError("Índice de tarea inválido")
        self.tareas[indice].completada = True

    def eliminar_tarea(self, indice):
        if indice < 0 or indice >= len(self.tareas):
            raise IndexError("Índice de tarea inválido")
        del self.tareas[indice]
