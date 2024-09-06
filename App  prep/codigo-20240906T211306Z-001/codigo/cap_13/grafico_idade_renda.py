#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importação das bibliotecas necessárias:
import pandas as pd
import matplotlib.pyplot as plt

EIXO_LINHAS = 0
EIXO_COLUNAS = 1

dados = pd.read_csv('vendas.csv')
compradores = dados[dados['Comprou']==1]
compradores.drop(['Comprou'], axis=EIXO_COLUNAS)

plt.title('Compras por Idade e Renda')
plt.xlabel('Renda Anual x 1000 (R$)')
plt.ylabel('Idade (Anos)')
plt.scatter(compradores.Renda/1000, compradores.Idade, s=2)
plt.show()
