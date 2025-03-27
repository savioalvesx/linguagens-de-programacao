print("Programa simula uma Agenda Telefônica.\n\n")

contatos = {}

while True:
    print("\n===== Gerenciador de Contatos =====")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Exibir todos os contatos")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Informe o nome do contato: ")
        if nome in contatos:
            print(f"Contato '{nome}' já existe. Use outro nome ou atualize o existente.")
        else:
            telefone = input("Informe o número de telefone: ")
            contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")

    elif opcao == "2":
        nome = input("Informe o nome do contato que deseja buscar: ")
        if nome in contatos:
            print(f"\n{nome}: {contatos[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado.")

    elif opcao == "3":
        nome = input("Informe o nome do contato que deseja remover: ")
        if nome in contatos:
            del contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    elif opcao == "4":
        if contatos:
            print("\n===== Lista de Contatos =====")
            for nome, telefone in contatos.items():
                print(f"{nome}: {telefone}")
        else:
            print("Nenhum contato cadastrado.")

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
