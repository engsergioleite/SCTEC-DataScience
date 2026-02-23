# a visualização de dados, também conhecida com data visualization ou dataviz, e o conjunto de tecnicas para representar informacoes e dados de forma visual de maneira comprreensivel a fim de transmitir resultados de analise de dados. 
# essas tecnicas sao utilizadas para transformar grande volume de dados e registros em gráficos, tabelas e diagramas qe podem ser processados mais facilmente e por qualquer pessoa. 
# a visualizacao de dados é importante para compreender de forma mais representativa as informacoes e a partir dos dados gerados, gerar decisoes.
# as razoes pelas quais a visualizacao de dados e importante e seu papel: 
# - a compreensao de dados: é a visualizacao de dados e ajuda a entender melhor a estrutura, padroes e tendencia dos dados, graficos de plot podem revelar insigths que nao seria perceptiveis so olhando os numeros.
# - a identificação de padrões: sao graficos que podem ajudar a identificar padroes que podem levar a descobertas importantes, por exemplo, um grafico de dispersao pode mostrar relacao entre duas variaveis
# - comunicação eficaz: comunicacoes claras e informativas sao essenciais para comunicar resultados e insigths de forma eficaz para outras pessoas (colegas, clientes e stakeholders)
# - Suporte a tomada de decisão: a vizualizacao dos dados pode ajudar na tomada de decisao informada, fornecendo uma representação visual das informacoes necessarias para avaliar diferentes opções:
#   - detecção de anomalias: matplotlib, seaborn e ploty ajudam a criar graficos de barras, linhas, depressao, mapas de calor, etc. 
# o matplotlib é uma biblioteca para vizualizar graficos em python em 2d, em diversos tipos
# a documentacao do matplotlib disponibiliza 2 links interessantes para visualizar sua galeria de gráficos: o plot types (a pagina mostra os tipos de visualizacoes possiveis com o matplotlib) e o examples e ambos mostrar ate os codigos que sao usados para chegar em determinada visuzlizacao

import matplotlib.pyplot as plt
"""
# Criando o gráfico de linha
# plt.plot([1, 3, 5], [2, 6, 7])
# plt.show()

x = ["Macas", "Laranja", "Uva"]
y = [5, 3, 7]

# criaçao grafico de barra e definicao da cor
plt.bar(x,y, color = "green") #
# adicionando rotulos
plt.title("Gráfico de quantidade de frutas") # add titulo
plt.xlabel("Frutas") # add Nome eixo X
plt.ylabel("Quantidade") # add nome eixo y

plt.show() # comando para visualizar o grafico
"""
# SCATTER - comando para criar grafico de pontos

x = [1,3,5,3,4,7,8,9,4]
y = [4,8,9,3,2,5,4,5,7]

# criando o gráfico

plt.scatter(x,y, label = "Pontos", color = "c", marker= "*", s = 100) # comando para criar o grafico de pontos a cor e o tipo de marcador
plt.legend()
plt.show()