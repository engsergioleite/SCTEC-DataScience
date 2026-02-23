import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregando o dataset "flights" (voos).
# Este conjunto de dados mostra o número de passageiros de uma companhia aérea 
# entre os anos de 1949 e 1960.
voos = sns.load_dataset("flights")

# 2. Transformando os dados com PIVOT (O "pulo do gato"):
# O Heatmap precisa de uma tabela onde os meses sejam as linhas (index) 
# e os anos sejam as colunas. O .pivot() reorganiza a lista de dados 
# nesse formato de "grade" ou "tabuleiro de xadrez".
voos = voos.pivot(index="month", columns="year", values="passengers")

# 3. Definindo o tamanho da imagem.
# Como temos muitos anos e meses, um tamanho maior (10x6) ajuda a ler os números.
plt.figure(figsize=(10, 6))

# 4. Criando o Mapa de Calor (Heatmap):
# voos: A nossa tabela organizada em grade.
# annot=True: "Annotation" (Anotação). Escreve o número exato dentro de cada quadradinho.
# fmt=".0f": Formata os números. O ".0f" diz ao Python para não mostrar casas decimais 
# (deixar o número "inteiro"), para o gráfico não ficar poluído.
sns.heatmap(voos, annot=True, fmt=".0f")

# 5. Finalizando a visualização.
# Exibe o gráfico com a escala de cores lateral (color bar).
plt.show()