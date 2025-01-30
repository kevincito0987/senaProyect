def excercise1():
    while True:
        try:
            horas = int(input("Ingrese la cantidad de horas que duró el recorrido: "))
            if horas < 0:
                raise ValueError("La cantidad de horas debe ser positiva.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            minutos = int(
                input("Ingrese la cantidad de minutos que duró el recorrido: ")
            )
            if minutos < 0:
                raise ValueError("La cantidad de minutos debe ser positiva.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    while True:
        try:
            distancia = int(input("Ingrese la cantidad de kilómetros que recorrió: "))
            if distancia < 0:
                raise ValueError("La cantidad de kilómetros debe ser positiva.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    minutos_totales = (horas * 60) + minutos

    print(f"Su recorrido de {distancia} duró {minutos_totales}")
