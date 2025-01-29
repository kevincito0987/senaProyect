while True:
    try:
        print(
                    """
                Bienvenido al sistema de Ejercicios del SENA :):)
                Selecciona:
                1.Ejercico 1
                2.Ejercico 2
                3.Ejercico 3
                4.Ejercico 4
                0.Salir
                """
                )
        opc = int(input())
        try:
            while True:
                match opc:
                    case 1 : print("EXERCISES")
        except ValueError:
            print("Ingresa un numero porfa.")
    except ValueError:
        print("Ingresa un numero")