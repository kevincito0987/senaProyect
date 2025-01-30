from excercises.excercise1 import excercise1

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
                5.Ejercico 5
                6.Ejercico 6
                7.Ejercico 7
                8.Ejercico 8
                9.Ejercico 9
                10.Ejercico 10
                0.Salir
                """
        )
        opc = int(input())
        if opc == 0:
                break 
        try:
            while True:
                match opc:
                    case 1:
                        excercise1()
                        continuar = input("¿Desea calcular el tiempo para otro corredor? (s/n): ")
                        if continuar.lower() != 's':
                            break 
        except ValueError:
            print("Ingresa un numero porfa.")
    except ValueError:
        print("Ingresa un numero")
