def excercise2():
    while True:
                try:
                    C = int(input("Ingrese la cantidad de grados celcios a convertir a farenheit, (0 para salir): "))
                    if C < 0:
                        raise ValueError("La cantidad de horas debe ser positiva.")
                    elif C == 0:
                     break
                except ValueError as e:
                    print(f"Error: {e}")

    F = ((9/5) * C) + 32


    print(f"La temperatura en grados Farenheit es de {F}")