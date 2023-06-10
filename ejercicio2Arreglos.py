import random as rd
import numpy as np

arreglo = np.zeros((3, 3))

for i in range(3):
    for c in range(3):
        arreglo[i][c] = rd.randint(0, 100)

print(arreglo)

print("el promedio de sus elementos es: ", arreglo.mean())
print("la suma de sus elementos es: ", arreglo.sum())
print("el numero mayor de sus elementos es: ", arreglo.max())
print("el numero menor de sus elementos es: ", arreglo.min())
print("los elementos de la diagonal es: ", arreglo.diagonal())

arregloDos = np.diag([1,2,3])
print(arregloDos)