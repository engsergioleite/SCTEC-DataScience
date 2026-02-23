import pandas as pd

funcionarios = {
    "Nome": ["Sérgio", "Ana", "Lana", "Laís"],
    "Endereço": ["Jardim Atlântico", "Coqueiros", "Estreito", "Abraão"],
    "Data de nascimento": [11, 18, 19, 11],
    "Data de admissão": [12, 13, 14, 15],
    "Salário": [5000, 10000, 20000, 30000],
    "Cargo": ["gerente", "coordenadora", "diretora", "presidente"]
}

df = pd.DataFrame(funcionarios) # adicionando o dict funcionarios como pandas dataframe na variavel df
# print(df)

# mostrar na tela todas as linhas da coluna data de admissão
# print(df["Data de admissão"])

print(df.iloc[0]) # vai mostrar todos os rótulos e os atributos do indice 0 da lista

print(df.loc[3, "Nome"])
