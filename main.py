from excercises.exercise1 import exercise1
from excercises.excercise2 import excercise2
from excercises.excercise3 import excercise3
from excercises.excercise4 import excercise4
from excercises.excercise5 import excercise5
from excercises.excercise6 import excercise6
from excercises.excercise7 import excercise7
from excercises.excercise8 import excercise8
from excercises.excercise9 import excercise9
from excercises.excercise10 import excercise10

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
                    case 5:
                        excercise5()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 6:
                        excercise6()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 7:
                        excercise7()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 8:
                        excercise8()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 9:
                        excercise9()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 10:
                        excercise10()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 0 : break
                    case _ : print("Opción no válida")
        except ValueError:
            print("Ingresa un numero porfa.")
    except ValueError:
        print("Ingresa un numero")
