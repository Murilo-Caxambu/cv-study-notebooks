import pandas as pd
import numpy as np
df = pd.read_csv("turbinas.csv")
modelo = (df["Modelo"].unique())
print("-Modelos de turbina:")
print(modelo)

inativas = df[df["Status"]=="Inativa"]
print("-Turbinas Inativas: ")
print(inativas)

mais_eficientes = df[df["Eficiencia_%"] > 92.6].sort_values(by="Eficiencia_%", ascending=False)
print("Turbinas mais eficientes: ")
print(mais_eficientes)

media_potencia = df["Potencia_MW"].mean()
media_sup_potencia = df[df["Potencia_MW"] > media_potencia]
print("Turbinas com potencia acima da media: ")
print(media_sup_potencia)