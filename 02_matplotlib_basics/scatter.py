import numpy as np
from numpy import random
import matplotlib.pyplot as plt

x = np.random.randint(0,50, size=(50))
y = x +np.random.normal(0,50, size=(50))
fig, ax = plt.subplots(figsize=(10,5))
scatter = ax.scatter(x,y, c=y, cmap='plasma', alpha=0.8)
ax.set_title("Scatter")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.grid(True)
fig.colorbar(scatter, ax=ax, label='Cor por numero')

plt.show()