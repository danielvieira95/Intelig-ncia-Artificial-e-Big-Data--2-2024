# Importando os módulos das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Carregando o dataset
dataset = pd.read_csv('tempo_salarios.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
# Dividindo o dataset entre treino e teste:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3,\
                                                    random_state = 0)
# Ajustando o modelo de Regressão Linear para o dataset de treino
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
# Visualizar os resultados de treino
plt.figure(figsize=(15,8))
plt.plot(X, y, 'Dr')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salário x Experiência ')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário')
plt.show()