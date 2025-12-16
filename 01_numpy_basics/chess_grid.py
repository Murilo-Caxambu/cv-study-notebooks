# Tabuleiro de xadrez 8x8 -> vou ter q intercalar entre brancas e pretas: 0 1 0 1 0 1 0 1 dps inverte, 8 colunas
import numpy as np
tabuleiro = np.array([0,1,0,1,0,1,0,1, 
                      1,0,1,0,1,0,1,0,
                      0,1,0,1,0,1,0,1, 
                      1,0,1,0,1,0,1,0,
                      0,1,0,1,0,1,0,1, 
                      1,0,1,0,1,0,1,0,
                      0,1,0,1,0,1,0,1, 
                      1,0,1,0,1,0,1,0,])

n_tabuleiro = tabuleiro.reshape(8,8)
print (n_tabuleiro)