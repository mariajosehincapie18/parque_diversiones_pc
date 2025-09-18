from pila import Stack
class Visitante:
    def __init__(self, id: str , tipo: str):
        self.id= id
        self.tipo = tipo

    def __str__(self):
        return f"\n Visitante {self.id} ({self.tipo})"
        
class Atraccion:
    def __init__(self,parque, nombre_atraccion: str, capacidad:int):
        self.parque = parque
        self.nombre_atraccion = nombre_atraccion
        self.capacidad = capacidad
        self.visitantes= Stack()
    
        

    def agregar_visitante(self,nuevo_visitante):
        self.visitantes.push(nuevo_visitante)
    

    def procesar_turno(self,i,n):
        atraccion_siguente = None
        if i < n -1:
            atraccion_siguente = self.parque.atracciones.first()

        print(f"\n[{self.nombre_atraccion}]")
        for _ in range (self.capacidad):
            if not self.visitantes.is_empty():
                visitante_actual= self.visitantes.pop()
                print(f"\n El visitante procesado es: {visitante_actual}")

                if atraccion_siguente:
                        atraccion_siguente.agregar_visitante(visitante_actual)

                else:
                    self.parque.salida_visitantes.enqueue(visitante_actual)

        print("Quedaron en espera: ", self.visitantes)
        

        
    def __str__(self):
        return f"Atracción: {self.nombre_atraccion} | Capacidad: {self.capacidad} |"





