#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import numpy as np

dataset = pd.read_csv('tempo_salarios.csv')
X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

X = X.reshape(len(X),1)
y = y.reshape(len(y),1)

sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# KERNEL Linear
regressor_linear = SVR(kernel='linear')

# KERNEL Gaussian Radial Basis Function
regressor_rbf = SVR(kernel='rbf')

# para o regressor iremos voltar o y padronizado para uma lista de valores
y = np.ravel(y)

regressor_linear.fit(X,y)

plt.figure(dpi=300)
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor_linear.predict(X)), color = 'blue')
plt.title('Regressão Linear usando SVR - kernel Linear')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário')
plt.show()

y = np.ravel(y)

regressor_rbf.fit(X,y)

plt.figure(dpi=300)
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor_rbf.predict(X)), color = 'blue')
plt.title('Regressão usando SVR - kernel RBF')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário')
plt.show()