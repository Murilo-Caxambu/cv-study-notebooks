import numpy as np
from numpy import random
def reshape(t):
    a = np.arange(t)
    uint8_a = a.astype(np.uint8)        
    col = 10
    resto = t % col
    if resto > 0:
        f = col - resto
        z_completa = np.zeros(f, dtype="int")
        uint8_a = np.concatenate((uint8_a, z_completa))
    a_reshape = uint8_a.reshape(-1, 10)
    return a_reshape
print(reshape(24))


