from excercises.excercise2 import excercise2
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
                0.Salir
                """
                )
        opc = int(input())
        try:
            while True:
                match opc:
                    case 1 : excercise1()
                    case 2 : excercise2()
                    case 0. : break
                    case _ : print("La opcion ingresada no esta en mi sistema.")
        except ValueError:
            print("Ingresa un numero porfa.")
    except ValueError:
        print("Ingresa un numero")