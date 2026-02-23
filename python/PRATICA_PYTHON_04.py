# numeros pares

num = int(input("digite o primeiro número do intervalo: "))
num2 = int(input("digite o último número do intervalo: "))

for i in range(num, num2+1): # adicionei o +1 para chegar até o 40, pois Quando o loop chega no 40, ele entende que o trabalho acabou e encerra antes de testar se o 40 é par
    if i%2==0:
        print(i)

