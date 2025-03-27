class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_salario_anual(self):
        return self.salario * 12
    
    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'Salário mensal: R$ {self.salario:.2f}')
        print(f'Salário anual: R$ {self.calcular_salario_anual():.2f}')

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
    
    def calcular_salario_anual(self):
        return super().calcular_salario_anual() + self.bonus
    
    def mostrar_dados(self):
        super().mostrar_dados()
        super().mostrar_dados()
        print(f'Bônus anual: R$ {self.bonus:.2f}')
        print(f'Salário total anual (com bônus): R$ {self.calcular_salario_anual():.2f}')

class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao
    
    def calcular_salario_anual(self):
        return super().calcular_salario_anual() + self.comissao
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'Comissão anual: R$ {self.comissao:.2f}')
        print(f'Salário total anual (com comissão): R$ {self.calcular_salario_anual():.2f}')
    
    
gerente = Gerente('Sávio', 10000, 20000)
vendedor = Vendedor('João', 5000, 12000)

gerente.mostrar_dados()
vendedor.mostrar_dados()