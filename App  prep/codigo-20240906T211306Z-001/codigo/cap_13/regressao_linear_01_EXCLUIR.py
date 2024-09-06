import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv('compras.csv')
X = dados.iloc[:, :-1].values
plt.show()

print(dados.head())