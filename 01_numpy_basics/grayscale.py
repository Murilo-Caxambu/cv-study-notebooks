import numpy as np
from numpy import random
import matplotlib.pyplot as plt


img = random.randint(256, size=(300)).reshape(10,10,3).astype(np.uint8)
pesos = np.array([0.299,0.587,0.114])

broadcasting = img * pesos
s = broadcasting.sum(axis=2)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes[0].imshow(img)
axes[0].set_title('Imagem orginal')
axes[1].imshow(s, cmap = "grey")
axes[1].set_title("Imagem Preto e branco")
plt.show()
