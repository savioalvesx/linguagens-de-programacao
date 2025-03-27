   
def main(): #incompleto
    nota1 = float(input("Informe a 1° Nota: "))
    nota2 = float(input("Informe a 2° Nota: "))
    nota3 = float(input("Informe a 3° Nota: "))
    nota4 = float(input("Informe a 4° Nota: "))
    

def calculo (nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4

def resultado(media):
    if media >= 7:
        print(f"Sua média é {media}. Você foi aprovado.")
    else:
        print(f"Sua média é {media}. Você foi reprovado.")