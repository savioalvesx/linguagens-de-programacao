print("Este programa ler 5 nomes e exibe em ordem alfabética.\n")

nomes = []

for i in range(5):
    nome = str(input(f"Informe o {i+1}º nome: "))
    nomes.append(nome)

nomes.sort()

for nome in nomes:
    print(f"\n{nome}")