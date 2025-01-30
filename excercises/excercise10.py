def excercise10():
    print(
        """
                Realizar un algoritmo que muestre por pantalla la tabla de multiplicar decreciente de cualquier número,
                ingresado entre el 1 y el 10.  
            """
    )

    numero = int(input("Ingresa el número: "))

    for i in range(1, numero + 1):
        print(f"{i} x {numero} = {i * numero}")
