import numpy as np
from numpy import random
import matplotlib.pyplot as plt

img = random.randint(256, size=(300)).reshape(10,10,3).astype(np.uint8)
media = img.mean()
max = img.max()
media_v= img.mean(axis=0)
media_h= img.mean(axis=1)
media_p = img.mean(axis=2)

print(f"A media dos numeros: {media}\n valor maximo: {max}")
print(media_v, media_h, media_p)
plt.imshow(media_p, cmap="grey")
plt.show()
