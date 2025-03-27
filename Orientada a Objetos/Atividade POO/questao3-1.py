class Instrumento:
    def __init__(self, nome):
        self.nome = nome

    def tocar(self):
        print(f'Tocando um som genérico.')
    
    def mostrar_dados(self):
        print(f"\nInstrumento: {self.nome}")

class Violao(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)
    
    def tocar(self):
        print(f'Tocando acordes no violão.')
    
    def mostrar_dados(self):
        super().mostrar_dados()

class Flauta(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)
    
    def tocar(self):
        print(f'Tocando uma melodia na flauta.')
    
    def mostrar_dados(self):
        super().mostrar_dados()

instrumento = Instrumento('Piano')
violao = Violao('Violão')
flauta = Flauta('Flauta')

instrumento.mostrar_dados()
instrumento.tocar()
violao.mostrar_dados()
violao.tocar()
flauta.mostrar_dados()
flauta.tocar()


