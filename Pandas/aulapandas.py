import pandas as pd

# DataFrames
# Series

#Lendo o arquivo
df = pd.read_csv('dados_vendas.csv')
# print(df)
print(df.head()) # Imprimir as 5 primeiras linhas.
print(df.info())
print(df.describe())

#Filtro exibe a partir da data definida.
vendas_fevereiro = df[df['Data de Venda'] >= '2023-02-01']
print(vendas_fevereiro)

vendas_por_categoria = df.groupby('Categoria')['Quantidade Vendida'].sum()
print(vendas_por_categoria)

vendas_por_categoria = df.groupby(['Categoria', 'Produto'])['Quantidade Vendida'].sum()
print(vendas_por_categoria)

df['receita'] = df['Quantidade Vendida'] * df['Preço Unitário']
receita_categoria = df.groupby(['Categoria', 'Produto'])['receita'].sum()
print(receita_categoria)

vendas_por_categoria = df.groupby('Categoria')['Quantidade Vendida'].sum()
print(vendas_por_categoria)

vendas_por_categoria.to_csv('agrupamento.csv', index=False)
