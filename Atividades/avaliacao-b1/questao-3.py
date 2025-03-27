peso = float(input("Informe o seu peso(em kg): "))
altura = float(input("Informe a sua altura(em metros): "))

imc = peso / altura**2

print(f"Seu IMC é {imc:.2f}.") 