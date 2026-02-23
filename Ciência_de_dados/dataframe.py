# criando um dataframe - estrutura bidimensional semelhante a uma tabela onde os dados são organizados em linhas em colunas (umas das mais importantes do pandas) e muito usada em analise e manipulação de dados

import pandas as pd

#criando um dicionario para adicionar ao construtor de dataframe

data = {
    "nome": ["Sérgio", "Ana", "Lana", "Laís"],
    "Idade": [42, 41, 8, 6],
    "Cidade": ["Belém", "Florianópolis", "Rio de Janeiro", "São Paulo"]
}

df = pd.DataFrame(data) # construtor de dataframe do pandas, passando dicionario, lista de listas ou array como argumento

print(df) # impressão da variavel com o dataframe

print(df["nome"]) # acessando apenas o nome

print("Método ILOC")
print(df.iloc[0]) # método iloc para acessar linhas por rotulo - linha completa

print("Método LOC")
print(df.loc[0, "nome"]) # método loc para acessar linhas pelo indice inteiro, onde 0 é o indice e "nome a propriedade"


