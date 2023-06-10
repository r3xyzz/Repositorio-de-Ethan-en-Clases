'''
Contador de vocales: Escribe un programa que cuente la cantidad de vocales en una palabra ingresada por el usuario.
'''

palabra = input("Ingrese una palabra: ")

contador = 0 

for letra in palabra:
    if letra.lower() in "aeiou":
        contador += 1

print("La cantidad de vocales en la palabra es: ", contador)