class veiculo:
    def __init__(self, marca, modelo, ano, preco, ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def mostrar_dados(self):
        print(f'\nMarca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Preco: R$ {self.preco}')
    
class Carro(veiculo):
    def __init__(self, marca, modelo, ano, preco, quantidade_portas):
        super().__init__(marca, modelo, ano, preco)
        self.quantidade_portas = quantidade_portas
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'Quantidade de portas: {self.quantidade_portas}')

class Moto(veiculo):
    def __init__(self, marca, modelo, ano, preco, cilidradas):
        super().__init__(marca, modelo, ano, preco)
        self.cilidradas = cilidradas
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'Cilindradas: {self.cilidradas}')

#Carro
carro1 = Carro("Fiat", "Uno", 2020, 60000, 4)
carro1.mostrar_dados()

carro2 = Carro("Toyata", "Civic", 2024, 250000, 4)
carro2.mostrar_dados()

#Moto
moto1 = Moto("Yamaha", "R15", 2023, 25000, 250)
moto1.mostrar_dados()