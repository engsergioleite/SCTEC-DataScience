import seaborn as sns
import matplotlib.pyplot as plt

# 1. Importação do conjunto de dados (dataset) do Titanic.
# Pense nisso como abrir o "Manifesto de Embarque" oficial do navio.
titanic = sns.load_dataset("titanic") 

# 2. Definimos o tamanho da nossa "tela".
# 8 polegadas de largura por 6 de altura. Um tamanho ótimo para apresentações!
plt.figure(figsize=(8, 6))

# 3. Criamos o Histograma (Histplot).
# data=titanic: Dizemos ao Seaborn qual tabela usar.
# x="age": Escolhemos a coluna 'age' (idade) para ser analisada.
# O Seaborn vai contar automaticamente quantas pessoas existem em cada faixa de idade.
# O histplot (Histograma) é como se você pegasse todas as pessoas do Titanic e as organizasse em "baldes" ou "caixas" por idade: o balde dos 0-10 anos, o dos 10-20, e assim por diante. A altura da barra mostra quantas pessoas estão dentro de cada balde.

sns.histplot(data=titanic, x="age")

# 4. Mostramos o gráfico na tela.
# Sem esse comando, o Python prepara o gráfico na memória, mas não abre a janela.
plt.show()

