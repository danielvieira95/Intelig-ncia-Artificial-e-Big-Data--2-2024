#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importação das bibliotecas necessárias:
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('vendas.csv')
X = dados['Idade']
y = dados['Comprou']

plt.title('Compras por Idade')
plt.xlabel('Idade')
plt.ylabel('Comprou')
plt.scatter(X, y, s=2)
plt.show()
