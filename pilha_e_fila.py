# demonstração de pilha (LIFO - Last in First out)
pilha = []
pilha.append(1)
pilha.append(2)
pilha.append(3)
print(pilha)
pilha.pop() # remoção de um elemento vai ser o ultimo elemento - o último que entra o primeiro que sai

# demonstração de fila (FIFO - First in First out)

from collections import deque
fila = deque()
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)
fila.popleft()
print(fila)