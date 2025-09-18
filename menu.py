
def mostrar_menu(parque):
    while True:
        print("\n--- MENÚ DEL PARQUE ---")
        print("1. Agregar atracción")
        print("2. Eliminar atracción")
        print("3. Ingresar visitante")
        print("4. Ejecutar un turno")
        print("5. Ver estado del parque")
        print("6. Turnos automaticos")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre_atr = input("Nombre de la atraccion: ")
            capacidad = int(input("Capacidad: "))
            parque.agregar_atraccion(nombre_atr,capacidad)

        elif opcion == "2":
            nombre_eli = input("Nombre de la atraccion a eliminar: ")
            parque.eliminar_atraccion(nombre_eli)
            
        elif opcion  == "3":
            nombre_visitante = input("Nombre del nuevo visitante: ")
            tipo = input("Adulto/niño")
            parque.ingresar_visitantes(nombre_visitante,tipo)

        elif opcion == "4":
            parque.ejecutar_turno()
            parque.estado()
                

        elif opcion == "5":
            parque.estado()

        elif  opcion == "6":
            while not parque.esta_vacia():
                parque.ejecutar_turno()
                parque.estado()
            print("\n El parque esta vacio. ")

        elif opcion == "7":
            print("saliendo del parque")

        else:
            print("Opcion no valida, intente de nuevo")