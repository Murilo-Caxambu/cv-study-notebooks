import numpy as np
from numpy import random
import matplotlib.pyplot as plt

#variaveis do grafico 1:
notas = np.random.randint(0,10, size=5)
mes = np.array(["Fevereiro","Março","Abril","Maio","Junho"])

#variaveis do grafico 2(scatter)
matematica = random.randint(0,100, size=(50))
fisica = random.randint(0,100, size=(50))
nomes = [
    "Maria", "Jose", "Antonio", "Joao", "Francisco", "Ana", "Luiz", "Paulo",
    "Carlos", "Manoel", "Pedro", "Francisca", "Marcos", "Raimundo", "Sebastiao",
    "Antonia", "Marcelo", "Jorge", "Ricardo", "Eduardo", "Fernando", "Monica",
    "Teresa", "Renata", "Camila", "Mariana", "Patricia", "Sergio", "Roberto",
    "Fabio", "Alexandre", "Bruno", "Daniel", "Rafael", "Eliane", "Sandra",
    "Cristina", "Luciana", "Angela", "Debora", "Erica", "Vitor", "Tiago",
    "Andre", "Felipe", "Gabriela", "Juliana", "Letícia", "Priscila", "Vanessa"
]

#variaveis do grafico 3:
idade = 2 * random.randn(100) + 20
idade = idade.astype(int)
idade[idade < 0 ] = 0
idade [idade > 100 ]= 100

#variaveis do 4:
cursos=["Medicina","Direito","Psicologia"]
alunos = random.randint(20,80, size=(3))


fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12,8) )
#grafico 1: nota por mes
ax[0,0].plot(mes, notas,'o--r', mfc = 'r')
ax[0,0].grid(True)
ax[0,0].set_xlabel("Mês")
ax[0,0].set_ylabel("Notas")
ax[0,0].set_title("Evolução das notas médias")

#grafico2:scatter de notas:
scatter = ax[0,1].scatter(matematica,fisica, c=fisica, cmap="plasma", alpha =0.8)
ax[0,1].set_xlabel("Matemática")
ax[0,1].set_ylabel("Física")
ax[0,1].set_title("Matemática vs Física")
ax[0,1].grid(True)
for x, y, nome in zip(matematica, fisica, nomes):
    if (y > 80):
        if(x >80):
            ax[0,1].annotate(nome, (x, y), xytext=(5, 5), textcoords='offset points')
    if(y < 20):
        if(x < 20):
            ax[0,1].annotate(nome,(x,y), xytext=(5,5), textcoords='offset points')
                    
#grafico 3: historiograma com distribuicao de idades
ax[1,0].hist(idade, bins=10, color="paleturquoise", edgecolor='black')
ax[1,0].set_xlabel("Idades")
ax[1,0].set_ylabel("Quantidade de pessoas")
ax[1,0].grid(True)
ax[1,0].set_title("Distribuição das Idades")

#grafico 4- barras de cursos
ax[1,1].bar(cursos,alunos, color="paleturquoise", edgecolor='black')
ax[1,1].set_xlabel("Cursos")
ax[1,1].set_ylabel("Quantidade de alunos matriculados")
ax[1,1].set_title("Inscritos por Curso")


plt.tight_layout()
plt.show()
