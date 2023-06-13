import funciones_DEF as fn
op = 0
while op != 4:
    print("===================")
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. IMC")
    print("4. Salir")
    print("===================")
    op = int(input("Ingrese su opción: "))

    if op == 1:
        precioProducto = int(input("Ingrese precio: "))
        precioFinal = fn.calcularIVA(precioProducto)
        print("El precio final es: ",precioFinal)
    else:
        if op == 2:
            precioProducto = int(input("Ingrese precio: "))
            descuento = float(input("Ingrese el descuento: "))
            precioFinal = fn.funcionDescuento(precioProducto,descuento)
            print("El precio final es : ",precioFinal)
        else:
            if op == 3:
                peso = int(input("Ingrese su peso: "))
                estatura = float(input("Ingrese su estatura: "))
                fn.calcularIMC(peso,estatura)