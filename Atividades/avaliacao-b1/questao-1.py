idade = int(input("Informe a idade: "))

if idade < 12:
    print("Você é Criança!")
elif idade >= 12 and idade <= 17:
    print("Você é Adolescente!")
elif idade >= 18 and idade <= 59:
    print("Você é Adulto!")
else:
    print("Você é Idoso!")
    