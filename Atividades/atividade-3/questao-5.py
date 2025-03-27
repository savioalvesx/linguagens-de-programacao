print("Este programa simula um carrinho de compras.\n\n")

carrinho = []

while True:
    print("\n===== Carrinho de Compras =====")
    print("1. Adicionar produto")
    print("2. Ver produtos no carrinho")
    print("3. Remover produto")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Informe o nome do produto: ")
        carrinho.append(produto)
        print(f"'{produto}' adicionado ao carrinho.")

    elif opcao == "2":
        print("\nProdutos no carrinho:")
        print(", ".join(carrinho) if carrinho else "Carrinho vazio.")

    elif opcao == "3":
        produto = input("Informe o nome do produto para remover: ")
        if produto in carrinho:
            carrinho.remove(produto)
            print(f"'{produto}' removido do carrinho.")
        else:
            print(f"'{produto}' não está no carrinho.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")