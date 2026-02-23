import matplotlib.pyplot as plt

x = ["Sérgio", "Ana", "Lana", "Laís"]
y = [3000, 4000, 5000, 6000]

plt.bar(x,y, color = "red")

plt.title("Gráfico de salários")
plt.xlabel("Nomes")
plt.ylabel("Salários")

plt.show()