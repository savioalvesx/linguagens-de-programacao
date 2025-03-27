class Veiculo:
    def __init__(self, ano, cor, chassi, placa, modelo):
        self.ano = ano
        self.cor = cor
        self.chassi = chassi
        self.placa = placa
        self.modelo = modelo

    def mostrarDados(self):
        print('---------------------------------------')
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
        print(f'Chassi: {self.chassi}')
        print(f'Placa: {self.placa}')
        print(f'Modelo: {self.modelo}')

class Moto(Veiculo):
    def __init__(self, ano, cor, chassi, placa, modelo, cilindrada):
        super().__init__(ano, cor, chassi, placa, modelo)
        self.cilindrada = cilindrada
    
    def som(self):
        print('som da moto')

    def mostrarDados(self):
        super().mostrarDados()
        print(f'Cilindrada: {self.cilindrada}')

class Carro(Veiculo):
    def __init__(self, ano, cor, chassi, placa, modelo, cavalo):
        super().__init__(ano, cor, chassi, placa, modelo)
        self.cavalo = cavalo
    
    def mostrarDados(self):
        super().mostrarDados()
        print(f'Cavalo: {self.cavalo}')

veiculo1 = Veiculo(2020, 'vermelha', 23642, '123abc', 'Uno')
veiculo1.mostrarDados()

veiculo2 = Moto(2017, 'preta', 12356, '123-tre', 'Yamaha', 150)
veiculo2.mostrarDados()
veiculo2.som()

veiculo3 = Carro(2023, 'Cinza', 3242362, '123hjk', 'Argo', 150)
veiculo3.mostrarDados()


