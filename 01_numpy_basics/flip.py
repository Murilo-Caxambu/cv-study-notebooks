import numpy as np
matriz = np.arange((25)).reshape(5,5)
inv_horizontal = np.flip(matriz, axis=1)
inv_vertical = np.flip(matriz, axis=0)
print(f"matriz original:\n {matriz}\n")
print(f"matriz invertida horizontalmente:\n {inv_horizontal}\nmatriz invertida verticalmente:\n {inv_vertical}")