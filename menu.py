
def mostrar_menu(parque):
    while True:
        print("\n--- 🎡🎢 Bienvenidoo al PARQUE de atracciones 🎢🎡 ---")
        print("1️⃣ Agregar atracción")
        print("2️⃣ Eliminar atracción")
        print("3️⃣ Ingresar visitante")
        print("4️⃣ Ejecutar un turno")
        print("5️⃣ Ver estado del parque")
        print("6️⃣ Turnos automaticos")
        print("❌ Salir")

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
            tipo = input("Adulto/niño: ")
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
            print("\n ⚠️ El parque esta vacio ⚠️")

        elif opcion == "x":
            print("👋 Gracias por visitar el parque👋")


        else:
            print("❌Opcion no valida, intente de nuevo")