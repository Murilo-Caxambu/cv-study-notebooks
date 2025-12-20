import numpy as np
from numpy import random
import matplotlib.pyplot as plt

dados = random.randn(1000)
fig, ax  = plt.subplots(figsize=(12,6))
ax.hist(dados, bins=30, color='paleturquoise', edgecolor='black')
ax.set_title("Distribuição normal (gaussiana)")
ax.set_ylabel("Quantidade")
ax.set_xlabel("Numeros")
plt.show()

