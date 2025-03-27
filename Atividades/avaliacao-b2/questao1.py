class ContaBancaria:
    def __init__(self, titular, cpf, conta, agencia, saldo):
        self.titular = titular
        self.cpf = cpf
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo
    
    def mostrar_dados(self):
        print(f'\nTitular: {self.titular}')
        print(f'CPF: {self.cpf}')
        print(f'Conta: {self.conta}')
        print(f'Agencia: {self.agencia}')
        print(f'Saldo: {self.saldo}')

    def depositar(self, valor): 
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Saque realizado com sucesso.')
        else:
            print('Saldo insuficiente.')
        

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, cpf, conta, agencia, saldo, taxa_rendimento):
        super().__init__(titular, cpf, conta, agencia, saldo)
        self.taxa_rendimento = taxa_rendimento
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'A taxa de rendimento é de: {self.taxa_rendimento}%')
    
    def depositar(self, valor):
        return super().depositar(valor)
    
    def sacar(self, valor):
        return super().sacar(valor)  


#Conta Bancaria
print('\nConta Bancária Normal\n')
conta_bancaria = ContaBancaria("Sávio Alves", "123.456.789-10", "1234-5", "1234", 0)
conta_bancaria.mostrar_dados()
#Adicionar saldo
deposito = conta_bancaria.depositar(0)
conta_bancaria.mostrar_dados()
#Sacar saldo
saque = conta_bancaria.sacar(50)
conta_bancaria.mostrar_dados()

#Conta Poupança
print('\nConta Poupança\n')
conta_poupanca = ContaPoupanca("Henrique Vieira", "098-765-432-10", "5432-1", "5432", 0, 0.5)
conta_poupanca.mostrar_dados()
#Adicionar saldo
deposito = conta_poupanca.depositar(1000)
conta_poupanca.mostrar_dados()
#Sacar saldo
saque = conta_poupanca.sacar(90)
conta_poupanca.mostrar_dados()