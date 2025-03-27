class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def mostrarDados(self):
        print(f'Nome do produto: {self.nome}')
        print(f'Quantidade do produto: {self.quantidade}')
        print(f'Valor do produto: R${self.preco}')
        print('-------------------------------')
    
    def adicionarEstoque(self, qtde):
        self.quantidade += qtde
        # self.quantidade = self.quantidade + qtde
    
    def removerEstoque(self, qtde):
        if qtde > self.quantidade:
            print('Quantidade indisponível para retirada.')
            print('-------------------------------')
        else:
            self.quantidade -= qtde
            print(f'Foi retirada {qtde} do produto {self.nome}')
            print('-------------------------------')

# Exemplo de uso
produto1 = Produto('Arroz', 5, 10.5)
produto2 = Produto('Feijao', 3, 15.5)

produto1.mostrarDados()
produto2.mostrarDados()
produto1.adicionarEstoque(10)
produto1.mostrarDados()
produto1.removerEstoque(100)
produto1.mostrarDados()