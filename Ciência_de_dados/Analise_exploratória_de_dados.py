# é conhecida como EDA: Exploratory data Analysis
# consiste em varias etapas. mas as principais são: importar um conjunto de dados, compreender o quadro geral, preparação dos dados, compreensao de variaveis, estudo das relacoes entre variaveis, debate sobre resultados.
# nao precisa seguir sempre os mesmos passos, vai depender muito do problema e da solucao encontrada.

import pandas as pd

df = pd.read_csv("Ice Cream Sales - temperatures.csv")


dfOrdenado = df.sort_values(by="Temperature")
print(dfOrdenado)