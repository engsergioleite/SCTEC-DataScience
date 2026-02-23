# Calculadora para saber quantos anos o usuário terá em 2030


# Código se usar o parametro idade, conforme o texto da apresentação
nome = input("Escreva seu nome: ")
idade = int(input("Escreva a sua idade: "))
anoAtual = int(input("Escreva em que ano você está(AAAA): "))
tempo = int((2030 - anoAtual) + idade)

print(f"O nome é {nome} e a idade agora no ano de {anoAtual} é {idade} e terá {tempo} anos em 2030")

# Código se usar o parametro ano de nascimento, conforme foi falado na apresentação
nome = input("Escreva seu nome: ")
anoNascimento = int(input("Escreva o ano de nascimento(AAAA): "))
tempo = int((2030 - anoNascimento))

print(f"O nome é {nome} e terá {tempo} anos em 2030")
