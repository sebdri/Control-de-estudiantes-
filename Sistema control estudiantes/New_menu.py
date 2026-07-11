def show_menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Top 3 estudiantes")
        print("4. Promedio general")
        print("5. Exportar CSV")
        print("6. Importar CSV")
        print("7. Salir")

        try:
            option = int(input("Seleccione una opción: "))

            if 1 <= option <= 7:
                return option
            else:
                print("Debe ingresar una opción entre 1 y 7.")

        except ValueError:
            print("Debe ingresar un número.")