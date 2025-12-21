import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("monet.png")
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

fig,ax = plt.subplots(ncols=2, nrows=1, figsize=(12,12))

ax[0].imshow(img)
ax[0].axis("off")
ax[0].set_title("Impression, soleil levant")

ax[1].hist(r.ravel(),bins =256, color="red", alpha=0.5, label="Vermelho")
ax[1].hist(g.ravel(),bins =256, color="green", alpha=0.5, label="Verde")
ax[1].hist(b.ravel(),bins =256, color="blue", alpha=0.5, label="Azul")
ax[1].set_title("Histograma de cores na imagem")
ax[1].legend()
plt.show()