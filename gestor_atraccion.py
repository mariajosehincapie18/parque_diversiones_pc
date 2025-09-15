from pila import Stack
class Visitanes:
    def __init__(self, id: str , tipo: str):
        self.id= id
        self.tipo = tipo

    def __str__(self):
        return f"Visitante {self.id} ({self.tipo})"
        
class Atraccion:
    def __init__(self, nombre_atraccion: str, capacidad:int):
        self.nombre_atraccion = nombre_atraccion
        self.capacidad = capacidad
        self.visitantes= Stack()

    def agregar_visitante(self, nuevo_vistante:Visitanes):
        self.visitantes.push(nuevo_vistante)
    

    def procesar_turno():
        pass

        
    def __str__(self):
        return f"Atracción: {self.nombre_atraccion} | Capacidad: {self.capacidad} |"





