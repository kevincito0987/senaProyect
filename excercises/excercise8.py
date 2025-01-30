def excercise8():
    print(
            """
                Diseñar un algoritmo que permita ingresar la hora, minutos y segundos, y que calcule la hora en el siguiente
                segundo ("0<= H <=23", "0<= M <=59" "0<= S<=59"). 
            """
                )
    
    hora = int(input("Ingresa la hora: "))
    minutos = int(input("Ingresa los minutos: "))
    segundos = int(input("Ingresa los segundos: "))
    
    hora = hora + 1
    if hora > 23:
        hora = 0
    
    minutos = minutos + 1
    if minutos > 59:
        minutos = 0
    
    segundos = segundos + 1
    if segundos > 59:
        segundos = 0
    
    print(f"La hora en el siguiente segundo es {hora}:{minutos}:{segundos}")

    