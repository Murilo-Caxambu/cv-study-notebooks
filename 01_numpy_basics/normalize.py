import numpy as np
from numpy import random

matriz = random.randint(255, size=(25))
matriz_normalizada = matriz/255.0
print(f"Maior valor:{matriz_normalizada.max()}\nMenor valor:{matriz_normalizada.min()}")