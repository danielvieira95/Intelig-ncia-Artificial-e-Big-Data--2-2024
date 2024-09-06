import pandas as pd

df = pd.read_csv('vendas.csv')
X = df[['Age', 'EstimatedSalary']].values
y = df['Purchased'].values

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

from sklearn.linear_model import LogisticRegression
classificador = LogisticRegression()
classificador.fit(X, y)

import grafico_mapa_decisao

grafico = grafico_mapa_decisao.criar_grafico(X, y, classificador, 'Comprou', 'Idade e Salário')
grafico_mapa_decisao.exibir()
