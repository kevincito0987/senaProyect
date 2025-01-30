def excercise7():
    print(
        """
                Hacer un programa que registre el consumo realizado por los clientes de un restaurante, si el consumo de
                cada cliente excede 50000 se hará un descuento del 20%. Se debe mostrar el pago de cada cliente y el total
                de todos los pagos.  
            """
    )

    clientes = []
    for i in range(20):
        cliente = int(input("Ingresa el consumo de un cliente: "))
        clientes.append(cliente)

    total = 0
    for i in range(len(clientes)):
        if clientes[i] > 50000:
            clientes[i] = clientes[i] - (clientes[i] * 0.2)
        total = total + clientes[i]

    print(f"El total de pagos es {total}")

    for i in range(len(clientes)):
        print(f"El pago de {i+1} es {clientes[i]}")
