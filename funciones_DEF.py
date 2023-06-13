import math
# declaración de funciones
def saludo(nombre):
    print("Hola")
    print("Como estas",nombre)
    print("")

def calcularEdad(añoActual,añoNac):
    edad = añoActual - añoNac
    print("Su edad es: ",edad)

def sumar(num1,num2):
    suma = num1 + num2
    return suma

def areaCirculo(radio):
    area = math.pi * radio **2
    return area

def calcularIVA(precio):
    IVA = precio * 0.19
    precioFinal = precio + IVA
    return precioFinal

def funcionDescuento(precioProducto,descuento):
    precio = precioProducto - (precioProducto * descuento/100)
    return precio

def calcularIMC(peso,estatura):
    imc = peso/estatura**2

    if imc < 18.5:
        print("Bajo Peso")
    else:
        if imc >= 18.5 and imc <= 24.9:
            print("Adecuado")
        else:
            if imc >= 25.9 and imc <= 29.9:
                print("Sobrepeso")
            else:
                if imc >=30 and imc <= 34.9:
                    print("Obesidad grado 1")
                else:
                    if imc >= 35 and imc <= 39.9:
                        print("Obesidad grado 2")
                    else:
                        if imc > 40:
                            print("Obesidad grado 3")
                        else:
                            print("Sin registros!")