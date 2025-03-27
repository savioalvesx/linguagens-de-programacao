import pandas as pd

#Ler o arquivo "Alunos.csv".
#Exibe todo o arquivo.
df = pd.read_csv('alunos.csv')
print(df)

print('\n\n')

#Exibe as 5 primeiras linhas do arquivo.
print(df.head())

#Exibe somente os alunos ativos.
alunos_ativos = df[df['Status'] == 'Ativo']
print(alunos_ativos)

print('\n\n')

#Exibe o agrupamento por curso e a quantidade de alunos.
quantidade_por_curso = df.groupby('Curso')['Aluno'].count()
print(quantidade_por_curso)

print('\n\n')

#Cria um arquivo csv com o resultado do agrupamento.
quantidade_por_curso.to_csv('resultado_agrupamento.csv')