"""
Criar lista de alunos
Add outros 2 alunos
remover um aluno
usar conceito de dict para pesquisar um aluno especifico na lista
"""

alunos = ["sergio", "marcelo", "romulo", "caio", "everson"]
alunos.extend(["lucas", "eduardo"]) # adicionando 2 alunos
print(alunos)

# alunos.remove("eduardo")
alunos.pop(6) # O pop apaga pelo indice
print(alunos) 

# usar conceito de dicionario
print(alunos.index("sergio"))

