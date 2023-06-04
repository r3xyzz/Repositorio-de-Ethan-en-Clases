def suma(num1, num2):
    return num1 + num2 

def resta(num1, num2):
    return num1 - num2 

def multiplicacion(num1, num2):
    return num1 * num2

def divicion(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error compañero, no se puede dividir entre cero."

prinr("Bienvenido a la Calculadora R3X-CORPORATION")
print("--------------------------------------------")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
print("--------------------------------------------")

resultado_suma = suma(num1, num2)
resultado_resta = resta(num1, num2)
resultado_multiplicacion = multiplicacion(num1, num2)
resultado_divicion = divicion(num1, num2)

print("////////////////////////")
print("Suma: ",resultado_suma)
print("Resta: ",resultado_resta)
print("Multiplicacion: ",resultado_multiplicacion)
print("Divicion: ",resultado_divicion)
print("////////////////////////")
