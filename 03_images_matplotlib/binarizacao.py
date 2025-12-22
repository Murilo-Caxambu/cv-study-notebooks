import matplotlib.pyplot as plt
import numpy as np 

img = plt.imread('monet.png')
img_2d = img.mean(axis=2)

img_binaria = img_2d > 0.43

plt.imshow(img_binaria, cmap="grey")
plt.title("'Impression, soleil levant' em preto e branco")
plt.axis("off")
plt.show()