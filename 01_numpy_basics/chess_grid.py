# Tabuleiro de xadrez 8x8 -> vou ter q intercalar entre brancas e pretas: 0 1 0 1 0 1 0 1 dps inverte, 8 colunas
import numpy as np
def criar_grid_tabuleiro():
    tabuleiro = np.zeros((8,8), dtype="int")
    tabuleiro[0::2,1::2] = 1
    tabuleiro [1::2,0::2] = 1
    return tabuleiro
tabuleiro_criado = criar_grid_tabuleiro()
print(tabuleiro_criado)