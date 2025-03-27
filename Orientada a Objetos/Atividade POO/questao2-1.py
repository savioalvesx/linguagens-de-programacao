class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_detalhes(self):
        print(f'\nMarca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_combustivel):
        super().__init__(marca, modelo, ano)
        self.tipo_combustivel = tipo_combustivel

    def mostraDados(self):
        super().exibir_detalhes()
        print(f'Tipo Combustivel: {self.tipo_combustivel}')

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def mostrarDados(self):
        super().exibir_detalhes()
        print(f'Cilidrandas {self.cilindradas}')

carro = Carro('Fiat', 'Uno', 2010, 'Gasolina')
moto = Moto('Yamaha', 'R15', 2024, 150)
carro.mostraDados()
moto.mostrarDados()

    
