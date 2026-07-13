def show_menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Add students")
        print("2. show students")
        print("3. Top 3 students")
        print("4. General average")
        print("5. Export CSV")
        print("6. Import CSV")
        print("7. Exit")

        try:
            option = int(input("Seleccione una opción: "))

            if 1 <= option <= 7:
                return option
            else:
                print("Debe ingresar una opción entre 1 y 7.")

        except ValueError:
            print("Debe ingresar un número.")