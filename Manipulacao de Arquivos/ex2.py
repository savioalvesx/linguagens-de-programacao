with open('linguagens.txt', 'r') as arquivo:
    lista = arquivo.readlines()

    numeroLinhas = len(lista)

    print(f'Número de itens: {numeroLinhas}')