"""def dividir(a,b):
    return a / b # quando nao colocamos a barra, deu erro de sintaxe

# print(dividir(6,6)) função correta

print(dividir(6,0)) # a divisão por 0 nao existe, vai dar um erro de excessão

# quando nao tratamos erros de excessao, jogamos a responsabilidade para a linguagem fazer
# para melhorar isso, o ideal é gerar uma mensagem de erro para gerar melhor iteração com o  usuário
"""
# ai provocamos a divisão por 0 e o python disse que tem erro, mas vamos tratar esse erro:
def dividir(a,b):
    r = 0
    try:
        r = a / b
        return r
    except ZeroDivisionError:
        print("erro: nenhum número é divisivel por zero")
    except TypeError:
        print("erro: nenhum número é divisivel por string")
    except: # usado quando nao queremos definir o tipo de erro, fica algo geral
        print("Algum erro foi detectado")
    finally:
        print("Função executada")
print(dividir(6,a))