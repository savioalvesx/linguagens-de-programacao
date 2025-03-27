class ContaBancaria:
    def __init__(self, titular, conta, agencia):
        self.titular = titular
        self.conta = conta
        self.agencia = agencia
        self.saldo = 0

    def mostrarDados(self):
        print(f'titular: {self.titular}')
        print(f'conta: {self.conta}')
        print(f'agencia: {self.agencia}')
        print(f'saldo: {self.saldo}')
        print('-----------------')

    def depositar(self, valor):
        #self.saldo = self.saldo + valor
        self.saldo += valor
        print(f'foi depositado {valor} na conta de {self.titular}')
        print('-----------------')

    def sacar(self, valor):
        #self.saldo = self.saldo - valor
        if valor > self.saldo:
            print(f'Saldo insuficiente para saque na conta de {self.titular}')
        else:
            self.saldo -= valor
            print(f'foi sacado {valor} na conta de {self.titular}')
        print('-----------------')


conta1 = ContaBancaria('Alvaro', 1234, 4321)
conta1.mostrarDados()
conta2 = ContaBancaria('Jubscreuda', 3456, 4325)
conta2.mostrarDados()

conta1.depositar(150)
conta1.mostrarDados()
conta1.depositar(25)
conta1.mostrarDados()
conta2.sacar(5)
conta1.sacar(5)
