nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura (em metros): "))

idadeArredondada = round(idade)
alturaArredondada = round(altura, 2)

print(f"\nNome: {nome}")
print(f"Idade: {idadeArredondada} anos")
print(f"Altura: {alturaArredondada} metros")