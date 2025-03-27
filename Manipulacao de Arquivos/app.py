#R Read Leitura
#W Write Escrita
#a append adicionar
#x Criar arquivos

# arquivo = open('linguagens.txt', 'a')

# Permissao de 'r'

# print(arquivo.readable()) verificar se e possivel ler o arquivo.

# print(arquivo.read()) Ler o arquivo todo.

# print(arquivo.readline())
# print(arquivo.readline()) #Ler orquivo por linha.
# print(arquivo.readline()) 

#lista = arquivo.readlines() # Ler o arquivo e transformar em lista.
#print(lista[1])

# Permissao de 'a'

# write("\nSQL\n")
# arquivo.write("\nJavascript\n") # Adiciona o texto no arquivo.
# arquivo.write("\nC++\n")

# Com permissao 'w' adiciona o texto no arquivo e substitui o resto.

# Permissao 'x'

# arquivo = open('linguagens.txt', 'x')
#arquivo.write()


# arquivo.close() # Necessario fecgar o arquivo no final para poder usar depois.

try:
    with open("texte4.txt", "x") as arquivo: # Com with, arquivo ja fecha quando e executado. 
        # print(arquivo.read())
        arquivo.write("Adicionando texto")
except FileExistsError:
    print("Arquivo Existente")