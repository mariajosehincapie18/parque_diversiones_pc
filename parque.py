from cola import Queue
from gestor_atraccion import Atraccion, Visitante


class Parque:

    def __init__(self):
        self.atracciones =  Queue()
        self.salida_visitantes= Queue()

    def agregar_atraccion(self, nombre, capacidad):
        nueva_atraccion = Atraccion(self,nombre, capacidad)
        self.atracciones.enqueue(nueva_atraccion)

    def ingresar_visitantes(self,id, tipo):
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
            atraccion_actual = self.atracciones.dequeue()
            print(f"{atraccion_actual.nombre_atraccion}:   {atraccion_actual.visitantes}: ")
            self.atracciones.enqueue(atraccion_actual)
        print("Visitantes que ya salieron: ", self.salida_visitantes)


    def eliminar_atraccion(self, nombre_atraccion_eli:str):
    
        parque_aux = Queue()
        atraccion_eliminada= None
        siguiente_atraccion = None

        while not  self.atracciones.is_empty():
            atraccion_actual = self.atracciones.dequeue()
            if atraccion_actual.nombre_atraccion.lower() == nombre_atraccion_eli.lower():
                atraccion_eliminada= atraccion_actual
                if not self.atracciones.is_empty():
                    siguiente_atraccion = self.atracciones.first()
                print(f"/n la atracion {atraccion_actual.nombre_atraccion} fue eliminada con exito")

            else:
                parque_aux.enqueue(atraccion_actual)


        if atraccion_eliminada:
            if siguiente_atraccion:
                while not atraccion_eliminada.visitantes.is_empty():
                    visitante_act = atraccion_eliminada.visitantes.pop()
                    siguiente_atraccion.agregar_visitante(visitante_act)
            else:
                while not atraccion_eliminada.visitantes.is_empty():
                    visitante_act = atraccion_eliminada.visitantes.pop()
                    self.salida_visitantes.enqueue(visitante_act)



        while not parque_aux.is_empty():
            self.atracciones.enqueue(parque_aux.dequeue())

            
        

        
    

    def __str__(self):
            return f"Atracciones en el parque:\n{self.atracciones}"


