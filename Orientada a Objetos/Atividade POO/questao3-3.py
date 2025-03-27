class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        print(f'Som genérico do animal.')
    
    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')

class Cachorrro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazer_som(self):
        print(f'Au Au!')
    
    def mostrar_dados(self):
        super().mostrar_dados()

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazer_som(self):
        print(f'Miau!')
    
    def mostrar_dados(self):
        super().mostrar_dados()

animal = Animal('Coelho')
cachorro = Cachorrro('Cachorro')
gato = Gato('Gato')


animal.mostrar_dados()
animal.fazer_som()
cachorro.mostrar_dados()
cachorro.fazer_som()
gato.mostrar_dados()
gato.fazer_som()



    
        