import numpy as np

# o array em numpy é uma estrutura de dados multidimensional e pode armazenar elementos de forma homogenea (todos os elementos de um array numpy devem ter o mesmo tipo de dados)
# o array pode ter qualquer numero de dimensoes (conhecidas como eixos). e é a estrutura fundamental utilizada para manipular dados numericos no numpy (ex. um array unidimensional é semelhante a uma lista enquanto o aerray bidimensional é semelhante a uma lista de listas ou matriz)

# abaixo exemplos de como criar e manipular um array em numpy

arr1 = np.array([10, 20, 30, 40, 50]) # permite a possibilidade de criar matrizes de diferentes dimensoes e nesse caso foi algo semelhante a uma lista de uma dimensão

print(arr1)
print(arr1[3])

# agora vamos criar uma matriz com 3 linhas de 3 colunas cada (3 listas com 3 elementos dentro de cada lista)
# esse código é como se tivessemos linha 1 com coluna A 1, coluna B 3 e coluna c 3
#    A      B       C       D
# indices   0       1       2
#    0      1       2       3
#    1      4       5       6       
#    2      7       8       9

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# quando queremos acesse algum dado na matriz, usamos linha, coluna

print(arr2[0,1])

# ao criar a matriz com o numpy, podemos ter algumas caracteristicas da matriz que são chamadas de atributos
# dentre os atributos mais importantes do objeto ndarray estão o: 
# ndarray.shape (dimensões da matriz), ndarray.size (número de elementos totais da matriz) e o ndarray.dtype (descreve o tipo dos elementos presentes na matriz)  

print(f"o shape da matriz é: {arr2.shape}")
print(f"o tamanho da matriz é: {arr2.size}")
print(f"o tipo da matriz é: {arr2.dtype}")

# uma matriz em numpy é um caso especial de array bidimensional onde as operacoes matematicas seguem as regras da algebra linear
# as matrizes tem  metodos especificos para calculos matriciais como multiplicação de matrizes e inversao de matrizes
# embora os arrays e (ou de) matrizes possam parecer semelhantes em termos da representação me numpy, a principal diferença e como as operacoes matematicas sao tratadas. Ex.: a multiplicacao de array é elemento por elemento e as multiplicacao de matrizes seguem a algebra linear

arr3 = np.array([10, 20, 30, 40, 50])
print(arr3 + 1) # ele vai somar elemento por elemento e entregar um array [11, 21, 31, 41, 51]

# se multiplicar o arr2 que é uma matriz por 2, vamos ter cada elemento multiplicado por 2, da mesma forma que o unidimensional
print(arr2 * 2)

# calculando a média
print(np.mean(arr2))

# construindo a mediana - o numero que esta no meio
print(np.median(arr2))

# desvio padrao - é uma medida que indica a dispersao dos dados
desvioPadrao = np.std(arr1)
print(desvioPadrao)

# calculando a variancia (quadrado do desvio padrao)
variancia = np.var(arr1)
print(variancia)

# calculando valor maximo e minimo do array
valorMax = np.max(arr1)
valorMin = np.min(arr1)
print(f"O valor máximo é: {valorMax} e o valor mínimo é: {valorMin}")