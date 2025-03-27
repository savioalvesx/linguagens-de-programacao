class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    def mover(self):
        print(f'o veiculo {self.tipo} ta se movendo')

class Carro(Veiculo):
    def __init__(self, tipo, modelo):
        super().__init__(tipo)
        self.modelo = modelo

    def mover(self):
        print(f'o veiculo {self.tipo} do modelo {self.modelo} ta se movendo')

veiculo1 = Veiculo('moto') 
veiculo1.mover()
veiculo2 = Carro('Carro', 'Fiat')
veiculo2.mover()