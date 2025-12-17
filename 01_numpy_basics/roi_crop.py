import numpy as np
from numpy import random
matriz = random.randint(255, size=(64))
matriz_reshape = matriz.reshape(8,8)
def recorte():
    recorte_matriz = matriz_reshape[2:6,2:6]
    return recorte_matriz
print(f"Matriz original: \n{matriz_reshape}\n\n\n")
print (f"Matriz 4x4 central\n {recorte()}")