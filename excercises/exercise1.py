def exercise1():
    print(
            """
                Un corredor de maratón (distancia 42,195 Km) ha recorrido la carrera en 2 horas 25 minutos. Se desea un
                algoritmo que calcule el tiempo medio en minutos por kilómetro
            """
                )
    
    km = float(input("Ingresa la distancia en kilómetros: "))
    horas = float(input("Ingresa la cantidad de horas: "))
    minutos = float(input("Ingresa la cantidad de minutos: "))
    
    total = km * horas + minutos
    media = total / km
    print(f"El tiempo medio es {media} minutos por kilómetro")