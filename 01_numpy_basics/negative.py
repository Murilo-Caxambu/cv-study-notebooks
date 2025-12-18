import numpy as np
from numpy import random
import matplotlib.pyplot as plt

matriz = random.randint(256,size=(300)).reshape(10,10,3).astype(np.uint8)
matriz_inversa = [255,255,255] - matriz
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes[0].imshow(matriz)
axes[0].set_title('Imagem original')
axes[1].imshow(matriz_inversa)
axes[1].set_title('Imagem Invertida')
plt.show()
