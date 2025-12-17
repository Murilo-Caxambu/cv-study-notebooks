import numpy as np
def tirar_borda(t):
    grid = np.ones((t,t), dtype = "int")
    grid[0,:] = 0
    grid[-1,:] = 0
    grid[:,0] = 0
    grid[:,-1] = 0
    return grid
print(tirar_borda(20))
