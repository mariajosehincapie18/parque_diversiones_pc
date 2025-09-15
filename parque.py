from cola import Queue
from gestor_atraccion import Atraccion

class Parque:

    def __init__(self):
        self.atracciones =  Queue()

    def agregar_atraccion(self, nueva_atraccion : Atraccion):
        self.atracciones.enqueue(nueva_atraccion)

    def ingresar_visitantes (self,visitante):
        if not self.atracciones.is_empty():
            primera_atraccion = self.atracciones.first()
            primera_atraccion.agregar_visitante(visitante)

    def obtener_atraccion(self):
        atraccion_actual = self.atracciones.enqueue(self.atracciones.dequeue())
        return atraccion_actual

    def __str__(self):
            return f"Atracciones en el parque:\n{self.atracciones}"


