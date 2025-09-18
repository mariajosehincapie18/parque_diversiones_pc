
def mostrar_menu(parque):
    while True:
        print("\n--- MENÚ DEL PARQUE ---")
        print("1. Agregar atracción")
        print("2. Eliminar atracción")
        print("3. Ingresar visitante")
        print("4. Ejecutar un turno")
        print("5. Ver estado del parque")
        print("6. Salir")

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

        elif opcion == "5":
            parque.estado()

        elif  opcion == "6":
            print("saliendo del parque")

        else:
            print("Opcion no valida, intente de nuevo")