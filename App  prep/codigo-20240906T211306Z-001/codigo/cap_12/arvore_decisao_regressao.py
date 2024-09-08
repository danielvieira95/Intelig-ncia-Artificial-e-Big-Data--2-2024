# Importando os módulos das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Carregando o dataset
dataset = pd.read_csv('cargo_nivel_salarios.csv')

# Separando o dataset em X e Y - colunas  
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Criando o modelo de Árvore de Decisão - Regressão
from sklearn.tree import DecisionTreeRegressor

# Ajustando o modelo para todas as amostras
# regressor = DecisionTreeRegressor(random_state = 0)
regressor = DecisionTreeRegressor(
                      criterion='mse', max_depth=None, max_features=None,
                      max_leaf_nodes=None, min_impurity_decrease=0.0,
                      min_impurity_split=None, min_samples_leaf=1,
                      min_samples_split=2, min_weight_fraction_leaf=0.0,
                      presort=False, random_state=0, splitter='best')
regressor.fit(X, y)

# Visualizar os resultados do modelo
# plt.figure(figsize=(15,8)) # definindo o tamanho da figura
X_grid = np.arange(min(X), max(X), 0.01) # Deixando o eixo X com mais pontos
X_grid = X_grid.reshape((len(X_grid), 1)) # gráfico mais suave
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Nível x Salário (Árvore de Decisão Regressão)')
plt.xlabel('Nível')
plt.ylabel('Salário')
plt.show()