# -*- coding: utf-8 -*-
# Regressão Linear Múltipla

# Importando os módulos das bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np
from sklearn.linear_model import LinearRegression

# Carregando o dataset
dataset = pd.read_csv('startups.csv')

# Separando as variáveis independentes da dependente
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Codificando a variável categórica Estado

columnTransformer = ColumnTransformer([('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X = np.array(columnTransformer.fit_transform(X), dtype=np.float)

# Evitando a armadilha da variável fictícia
X = X[:, 1:]

# Dividindo o dataset em treino e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Ajustando o modelo de Regressão Linear para o dataset de treino
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Prevendo os resultados de teste
y_pred = regressor.predict(X_test)

for k in range(len(y_test)):
    y_teste = y_test[k]
    y_previsto = y_pred[k]
    erro = abs((y_test[k] - y_pred[k])/ y_pred[k] *100)
    print(f'y_teste: {y_teste:.2f} y_previsto: {y_previsto:.2f} erro: {erro:.2f}')
