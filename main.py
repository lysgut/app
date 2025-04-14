# Civic Report - Reportes Urbanos

# Diccionarios para almacenar datos
reportes = {}
prioridad = {"bache": "alta", "luz": "media", "agua": "alta", "basura": "media"}
ubicaciones = {}

def reportar_problema():
    tipo_problema = input("Ingrese el tipo de problema (ej: 'bache', 'luz', 'agua', 'basura', etc.): ").lower()
    if tipo_problema in reportes:
        reportes[tipo_problema] += 1
    else:
        reportes[tipo_problema] = 1

    latitud = input("Ingrese la latitud del problema: ")
    longitud = input("Ingrese la longitud del problema: ")
    ubicaciones[tipo_problema] = {"latitud": latitud, "longitud": longitud}

    print("\nReporte actualizado!")

def mostrar_prioridad_alta():
    print("\nProblemas con prioridad ALTA:")
    for problema, nivel in prioridad.items():
        if nivel == "alta":
            print(f"- {problema}")

def mostrar_reportes():
    print("\nTodos los reportes:")
    if not reportes:
        print("No hay reportes aún.")
    else:
        for problema, cantidad in reportes.items():
            ubicacion = ubicaciones.get(problema, {"latitud": "No registrada", "longitud": "No registrada"})
            print(f"{problema.title()} - Cantidad: {cantidad} - Ubicación: {ubicacion}")

def menu():
    while True:
        print("\n===== Civic Report - Menu Principal =====")
        print("1. Reportar un problema")
        print("2. Mostrar problemas con prioridad alta")
        print("3. Mostrar todos los reportes")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            reportar_problema()
        elif opcion == "2":
            mostrar_prioridad_alta()
        elif opcion == "3":
            mostrar_reportes()
        elif opcion == "4":
            print("\nGracias por usar Civic Report. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

# Iniciar el programa
menu()
