import numpy as np
import matplotlib.pyplot as plt

eixo_x = np.linspace(0,4*np.pi,100)
eixo_y_sen = np.sin(eixo_x)
eixo_y_cos = np.cos(eixo_x)

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(eixo_x,eixo_y_sen, label=("Seno"), color="blue")
ax.plot(eixo_x,eixo_y_cos, label=("Cosseno"), color="red", linestyle='--')
ax.set_title('Cálculo Trigonométrico')
ax.set_xlabel("Ângulo(em radianos)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

plt.show()