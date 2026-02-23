telefones = ["1111", "2222", "3333", "4444"]

telefones.append("5555") # adiciona um elemento no final da lista
telefones.extend(["6666", "7777"]) # adiciona vários elementos no final da lista
telefones.insert(3, "0000") #Adiciona um único elemento no indice 3 antes do index


for i in telefones:
    print(i)


telefones.remove("2222") # remove o item da lista, passando o elemento
telefones.pop(4) # remove o indice da lista

for i in telefones:
    print(i)
