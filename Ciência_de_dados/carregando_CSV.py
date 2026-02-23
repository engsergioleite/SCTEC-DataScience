import pandas as pd

# df = pd.read_csv("dados.csv")
df = pd.read_csv('dados.csv', sep=';')

print(df)
print(df.head(2))

print(df.iloc[5])
print(df.loc[2, "Pulse"])