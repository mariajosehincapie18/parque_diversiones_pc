from cola import Queue
from gestor_atraccion import Atraccion, Visitante


class Parque:

    def __init__(self):
        self.atracciones =  Queue()
        self.salida_visitantes= Queue()

    def agregar_atraccion(self, nombre, capacidad):
        nueva_atraccion = Atraccion(self, nombre, capacidad)
        self.atracciones.enqueue(nueva_atraccion)

    def ingresar_visitantes (self,id, tipo):
        nuevo_visitante = Visitante(id, tipo)
        if not self.atracciones.is_empty():
            primera_atraccion = self.atracciones.first()
            primera_atraccion.agregar_visitante(nuevo_visitante)

    def ejecutar_turno(self):
         n= self.atracciones.len()
         for i in range(n):
              atraccion = self.atracciones.dequeue()
              atraccion.procesar_turno(i,n)
              self.atracciones.enqueue(atraccion)

    def estado(self):
        n = self.atracciones.len()
        print("\n --- ESTADO DEL PARQUE ---")
        for i in range(n):
            atraccion = self.atracciones.dequeue()
            print(f"{atraccion.nombre_atraccion}:   {atraccion.visitantes}: ")
            self.atracciones.enqueue(atraccion)
        print("Visitantes que ya salieron: ", self.salida_visitantes)
        

        
    

    def __str__(self):
            return f"Atracciones en el parque:\n{self.atracciones}"


