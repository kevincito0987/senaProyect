def excercise5():
    print(
        """
                Elaborar un algoritmo que permita ingresar 20 números y muestre todos los números menores e iguales a 25. 
            """
    )

    numeros = []
    for i in range(20):
        numero = int(input("Ingresa el numero: "))
        numeros.append(numero)

    for i in range(len(numeros)):
        if numeros[i] <= 25:
            print(numeros[i])
