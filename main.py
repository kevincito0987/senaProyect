from excercises.exercise1 import exercise1
from excercises.excercise2 import excercise2
from excercises.excercise3 import excercise3
from excercises.excercise4 import excercise4

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
                        exercise1()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break 
                    case 2:
                        excercise2()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break 
                    case 3:
                        excercise3()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break 
                    case 4:
                        excercise4()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
        except ValueError:
            print("Ingresa un numero porfa.")
    except ValueError:
        print("Ingresa un numero")
