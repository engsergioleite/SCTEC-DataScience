import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregamos o conjunto de dados (dataset) do Titanic.
# Pense nisso como abrir uma planilha do Excel cheia de informações.
titanic = sns.load_dataset("titanic")

# 2. Agrupamos os dados para a análise:
# .groupby("sex"): Separa os passageiros em "man" (homem) e "woman" (mulher).
# ["survived"].sum(): Soma a coluna de sobreviventes (1 para sim, 0 para não).
# .reset_index(): CORREÇÃO -> Transforma o resultado de uma lista simples (Series) 
# em uma tabela organizada (DataFrame) que o gráfico consegue ler.
df_por_sexo = titanic.groupby("sex")["survived"].sum().reset_index()

# 3. Criamos a "moldura" do nosso quadro.
# figsize=(8, 6) define que o gráfico terá 8 polegadas de largura e 6 de altura.
plt.figure(figsize=(8, 6))

# 4. Desenhamos o gráfico de barras (barplot).
# data: a tabela que criamos no passo 2.
# x: o que queremos ver na base (categorias de sexo).
# y: o que define a altura da barra (quantidade de sobreviventes).
sns.barplot(data=df_por_sexo, x="sex", y="survived")

# 5. Adicionamos um título para deixar o gráfico profissional.
plt.title("Total de Sobreviventes por Sexo no Titanic")

# 6. O comando final que abre a janela e mostra o resultado.
plt.show()