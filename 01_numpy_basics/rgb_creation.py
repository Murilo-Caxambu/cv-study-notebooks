import numpy as np
from numpy import random
import matplotlib.pyplot as plt

matriz = np.zeros((10,10,3), dtype=np.uint8)
matriz[0:] = [0,0,255]
matriz[4:6,4:6] = [255,255,0]
print(matriz[5,5])

plt.imshow(matriz)
plt.axis('off')
plt.show()