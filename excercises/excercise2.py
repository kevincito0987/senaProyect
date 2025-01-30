def excercise2():
    print(
        """
                Realizar la conversión de una temperatura dada en grados Centígrados a grados Fahrenheit (Fórmula: F =
                (9/5) C + 32). 
            """
    )

    centigrados = float(input("Ingresa la temperatura en grados Centígrados: "))
    fahrenheit = (centigrados * 9 / 5) + 32
    print(f"La temperatura en grados Fahrenheit es {fahrenheit}")
