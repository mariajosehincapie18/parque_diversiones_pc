
from parque import Parque


parque = Parque()

  
# agregarmos atracciones
parque.agregar_atraccion("montaña_rusa",3)
parque.agregar_atraccion("carros_chocones",2)
parque.agregar_atraccion("rueda_fortuna",2)
parque.agregar_atraccion("castillo_terror",2)



parque.ingresar_visitantes("A1", "adulto")
parque.ingresar_visitantes("N1", "niño")
parque.ingresar_visitantes("A2", "adulto")
parque.ingresar_visitantes("N2", "niño")
parque.ingresar_visitantes("N3", "niño")
parque.ingresar_visitantes("A3", "adulto")
parque.ingresar_visitantes("N4", "niño")
parque.ingresar_visitantes("A4", "adulto")
parque.ingresar_visitantes("N5", "niño")
parque.ingresar_visitantes("A5", "adulto")
parque.ingresar_visitantes("N6", "niño")
parque.ingresar_visitantes("A6", "adulto")

parque.estado()




turno = 1
while True:
    print(f"\n--- TURNO {turno} ---")
    parque.ejecutar_turno()
    parque.estado()
    turno += 1

    n = parque.atracciones.len()
    todas_atracciones_vacias= True
    for i in range(n):
        atraccion = parque.atracciones.dequeue()
        if not atraccion.visitantes.is_empty():
            todas_atracciones_vacias= False
        
        parque.atracciones.enqueue(atraccion)


    if todas_atracciones_vacias:
        break

      




    
    


