# conceito de pilha

frutas = ["maça","banana","uva","pera"]
frutas.append("melancia")
frutas.append("melão")
frutas.append("ameixa")
print(frutas)
frutas.pop()
print(frutas)

# conceito de fila

from collections import deque
frutas = deque()
frutas.append("cacau")
frutas.append("caju")
frutas.append("pessego")
print(frutas)
frutas.popleft()
print(frutas)


# aplicando for e while
frutas = ["maça","banana","uva","pera", "cacau", "caju", "pessego"]
for fruta in frutas:
    print(fruta)

# aplicando e while
i = 0
while frutas[i] != "caju":
    print(frutas[i])
    i += 1