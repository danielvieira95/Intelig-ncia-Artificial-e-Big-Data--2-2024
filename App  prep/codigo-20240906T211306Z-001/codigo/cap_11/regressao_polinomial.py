#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importando os módulos das bibliotecas
import matplotlib.pyplot as plt
import pandas as pd

# Carregando o dataset
dataset = pd.read_csv('cargo_nivel_salarios.csv')

# Separando o dataset em X e Y - colunas  
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Dividindo o dataset entre treino e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Ajustando o modelo de Regressão Linear para o dataset de treino
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Criando o modelo de Regressão Polinomial
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)

# Ajustando o modelo para os dados de treino
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, y_train)
poly_reg.fit(X_train,y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y_train)

# Visualizar os resultados de treino
plt.figure(figsize=(15,8))
plt.plot(X_train, y_train, 'Dr')
plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)),'^b')
plt.title('Nível x Salário (Regressão Polinomial)')
plt.xlabel('Nível')
plt.ylabel('Salário')
plt.show()

# Criando o modelo de Regressão Polinomial - grau 4
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)

# Ajustando o modelo para os dados de treino
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, y_train)
poly_reg.fit(X_train,y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y_train)

# Visualizar os resultados de treino
plt.figure(figsize=(15,8))
plt.plot(X_train, y_train, 'Dr')
plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)),'^b')
plt.title('Nível x Salário (Regressão Polinomial)')
plt.xlabel('Nível')
plt.ylabel('Salário')
plt.show()

# Visualizar os resultados de teste
plt.figure(figsize=(15,8))
plt.plot(X_test, y_test, 'Dr')
plt.plot(X_test, lin_reg_2.predict(poly_reg.fit_transform(X_test)),'^b')
plt.title('Nível x Salário (Regressão Polinomial)')
plt.xlabel('Nível')
plt.ylabel('Salário')
plt.show()

# Visualizar com todas as amostras
plt.figure(figsize=(15,8))
plt.plot(X, y, 'Dr')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)),'^b--')
plt.title('Nível x Salário (Regressão Polinomial)')
plt.xlabel('Nível')
plt.ylabel('Salário')
plt.show()

# Ajustando e plotando o modelo para grau 8
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 8)

# Ajustando o modelo para todos os dados
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
poly_reg.fit(X,y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualizar com todas as amostras
plt.figure(figsize=(15,8))
plt.plot(X, y, 'Dr')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)),'^b--')
plt.title('Nível x Salário (Regressão Polinomial)')
plt.xlabel('Nível')
plt.ylabel('Salário')
plt.show()

# Ajustando e plotando o modelo para grau 12
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 12)

# Ajustando o modelo para todos os dados
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
poly_reg.fit(X,y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualizar com todas as amostras
plt.figure(figsize=(15,8))
plt.plot(X, y, 'Dr')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)),'^b--')
plt.title('Nível x Salário (Regressão Polinomial)')
plt.xlabel('Nível')
plt.ylabel('Salário')
plt.show()
