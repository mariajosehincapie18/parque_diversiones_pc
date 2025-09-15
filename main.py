from gestor_atraccion import Visitanes, Atraccion
from parque import Parque

def main():
    parque = Parque()

    #creamos las atracciones
    montaña_rusa = Atraccion("Montaña Rusa", capacidad=3)
    carros_chocones = Atraccion("carros_chocones", capacidad=2)
    rueda_fortuna = Atraccion("rueda_fortuna", capacidad=2)
    castillo_terror = Atraccion("Castillo del Terror", capacidad=2)

    # agregarmos atracciones
    parque.agregar_atraccion(montaña_rusa)
    parque.agregar_atraccion(carros_chocones)
    parque.agregar_atraccion(rueda_fortuna)
    parque.agregar_atraccion(castillo_terror)


    # 3. Ingresar visitantes
    visitante1= Visitanes("A1", "adulto")
    visitante2= Visitanes("n1", "niño")
    visitante3= Visitanes("A2", "adulto")
    visitante4= Visitanes("n2", "niño")
    parque.ingresar_visitantes(visitante1)
    parque.ingresar_visitantes(visitante2)
    parque.ingresar_visitantes(visitante3)
    parque.ingresar_visitantes(visitante4)

    # 4. Mostrar estado del parque
    print ("cola de atracciones de parque")
    print(parque.atracciones) 
    print("visitantes montaña")
    print(montaña_rusa.visitantes) 
    print("visitantes carros")
    print(carros_chocones.visitantes)   
    print("visitantes rueda")      
    print(rueda_fortuna.visitantes) 
    print("visitantes castillo")
    print(castillo_terror.visitantes)     

    
    


if __name__ == "__main__":
    main()