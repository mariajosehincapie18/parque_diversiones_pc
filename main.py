
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

parque.estado()

      




    
    


