import pandas as pd

# Importação dos dados:
df = pd.read_csv("transportes.csv")
print('Antes da alteração:')
print(df)
print('Excluindo as linhas 3 e 5:')
df = df.drop([3, 5])
print(df)
print('Excluindo a coluna Autonomia:')
df = df.drop('Autonomia', axis=1)
print(df)
print('Excluindo duas colunas pelo nome:')
df = df.drop(['Peso', 'Consumo'], axis=1)
print(df)
