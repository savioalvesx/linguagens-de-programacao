# Gravar frases em um arquivo
#Solicitar 3 frases

frases = []
for i in range(1, 4): # for i in range(3)
    frase= input("Informe a {i}º Frase: ")
    frases.append(frase)

# Gravar as frases num arquivo
with open('frases.txt', 'w') as arquivo:
    for frase in frases:
        arquivo.write(frase)

with open('frases.txt', 'r') as arquivo:
    print(arquivo.read())