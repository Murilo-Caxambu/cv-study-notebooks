# Tabuleiro de xadrez 8x8 -> vou ter q intercalar entre brancas e pretas: 0 1 0 1 0 1 0 1 dps inverte, 8 colunas
import numpy as np
tabuleiro = np.zeros((8,8), dtype="int")
tabuleiro[0::2,1::2] = 1
tabuleiro [1::2,0::2] = 1
print(tabuleiro)
