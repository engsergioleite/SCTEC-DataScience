class Carro: #Criação da clsse carro
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self. ano = ano
    
    def mostrarPlaca(self):
        print(self.modelo, self.placa, self.ano)

carro1 = Carro("fusca", "444", "1980")
carro2 = Carro("UNO", "555555", "1990")

carro1.mostrarPlaca()
carro2.mostrarPlaca()