import numpy as np
import random 

arreglos = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

for k in range(3):
    for e in range(3):
        arreglos[k][e] = random.randint(0, 100)

for fila in arreglos:
    print(fila)

matriz = np.array
