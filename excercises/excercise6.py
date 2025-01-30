def excercise6():
    print(
        """
                Hacer un programa que sume 5 precios de camisas (en dólares) y que luego muestre el total de la venta en pesos. 
            """
    )

    precio1 = float(input("Ingresa el precio de la primera camisa: "))
    precio2 = float(input("Ingresa el precio de la segunda camisa: "))
    precio3 = float(input("Ingresa el precio de la tercera camisa: "))
    precio4 = float(input("Ingresa el precio de la cuarta camisa: "))
    precio5 = float(input("Ingresa el precio de la quinta camisa: "))

    total = precio1 + precio2 + precio3 + precio4 + precio5
    totalVenta = total * 4168.99
    print(f"El total de la venta es {totalVenta} pesos")
