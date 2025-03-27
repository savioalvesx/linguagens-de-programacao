class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: R$ {self.preco:.2f}')
        print(f'Estoque: {self.estoque}')

produto1 = Produto('Arroz', 30, 10)
produto1.detalhes()
