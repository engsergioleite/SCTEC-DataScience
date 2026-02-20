nomeTelefone = {"sergio": "1111",
                "ana": "2222",
                "lana": "3333",
                "lais": "4444"} # exemplo de dicionário

print(nomeTelefone)

# Transformando uma list em dicionário

nomeTelefone = [("sergio", "1111"),
                ("ana", "2222"),
                ("lana", "3333"),
                ("lais", "4444")]

novoDict = dict(nomeTelefone)

print(novoDict)


print(novoDict["lais"]) # acessando apenas a chave lais do dict novoDict para imprimir o valor de lais

novoDict["cookie"] = "5555" # Adicionando chave: valor ao dicionario

print(novoDict)

novoDict.pop("cookie") # removendo a chave cookie do dict

print(novoDict)