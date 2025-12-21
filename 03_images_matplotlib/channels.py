import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("monet.png")
r = img[:,:,0]
g = img[:,:,1]
b= img[:,:,2]
fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(12,8))

#imagem original
ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title("Imagem original")
#imagem vermelho
ax[1].imshow(r, cmap='Reds')
ax[1].axis('off')
ax[1].set_title("Imagem em vermelho")
#img verde
ax[2].imshow(g, cmap='Greens')
ax[2].axis("off")
ax[2].set_title("Imagem em verde")

# img azul
ax[3].imshow(b, cmap='Blues')
ax[3].axis("off")
ax[3].set_title("Imagem em azul")

plt.show()
