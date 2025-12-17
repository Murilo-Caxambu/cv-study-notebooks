import numpy as np
from numpy import random

matriz = random.randint(256, size=(100)).reshape(10,10)
def binarizar():
    preto = matriz <= 127
    branco = matriz > 127
    matriz[preto] = 1
    matriz[branco] = 0
    return matriz

print(binarizar())