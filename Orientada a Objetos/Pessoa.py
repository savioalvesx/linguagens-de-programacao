class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'altura: {self.altura:.2f}')
        print('-----------------')

    
pessoa1 = Pessoa('Alvaro', 30, 1.75)
pessoa1.apresentar()
pessoa2 = Pessoa('Dhanndara', 31, 1.60)
pessoa2.apresentar()