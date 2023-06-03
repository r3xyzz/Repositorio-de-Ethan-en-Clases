''' 1.1 Crear un arreglo //unidimensional// de tamaño 10, conelementos aleatorios de números enteros del 0 al 100, 
para ello deberá investigar la función que permita crear números aleatorios.
'''

''' 1.2. Crear una copia del arreglo y muestre:
o Elemento mayoro 
o Elemento menoro 
o Suma de los elementoso 
o Promedio de los elementoso 
o Mostrar todos los elementos 
'''

import numpy as np
import random as rd

# arreglo = [] esto es una lista (de cualquier tipo)
print("---------------------------------------------------")
arreglo = np.zeros(10) # es un arreglo 
# print(arreglo)

for i in range(len(arreglo)):
    arreglo[i] = rd.randint(1,100)
print(arreglo)

arregloDos = arreglo[:].copy()
print("---------------------------------------------------")

print("El numero mayor del arregloDos : ", arregloDos.max())
print("El numero menor del arregloDos : ", arregloDos.min())
print("La suma de los elementos del arregloDos : ", arregloDos.sum())
print("El promedio de sus elementos del arregloDos : ", arregloDos.mean())

print("fin")
print("fin2")

