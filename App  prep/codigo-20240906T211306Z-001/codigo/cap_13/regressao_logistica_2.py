# Importação das bibliotecas necessárias:
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from grafico_mapa_decisao import GraficoMapaDecisao

dados = pd.read_csv('vendas.csv')

# Definindo as variáveis *independentes*:
X = dados[['Idade', 'Renda']].values
# X = dados[['Genero', 'Idade', 'Salario']].values

# Agora, a variável *dependente* (o que queremos inferir):
y = dados['Comprou'].values

# Aplicando uma transformação para que os dados fiquem *na mesma escala*:
scaler = StandardScaler()

# Aplicando o algorimto de regressão logística:
X = scaler.fit_transform(X)
algoritmo = LogisticRegression()
algoritmo.fit(X, y)

grafico = GraficoMapaDecisao(X, y, algoritmo, 'Regressão Logística', 'Idade Padronizada (Score-Z da Idade)',
                             'Renda Anual Padronizada (Score-Z da Renda Anual)')
grafico.exibir()