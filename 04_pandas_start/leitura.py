import pandas as pd

df = pd.read_csv('turbinas.csv')
print(f"Primeiras 5 linhas:\n{df.head()}")
print(df.info())
print(df.describe())