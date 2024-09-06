# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv('bank_note.csv')
print(df.shape)
print(df.head())
X = df.iloc[:,0:4].values
y = df.iloc[:,4].values
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, 
                                                        random_state=3)
escalonador = StandardScaler()
X_treino = escalonador.fit_transform(X_treino)
X_teste = escalonador.fit_transform(X_teste)

algoritmo = KNeighborsClassifier(n_neighbors=3)
algoritmo.fit(X_treino, y_treino)

previsoes = algoritmo.predict(X_teste)
matriz_confusao = confusion_matrix(y_teste, previsoes)
acuracia = accuracy_score(y_teste, previsoes)
print(f'Matriz de Confusão: {matriz_confusao}')
print(f'Acurácia do modelo: {acuracia}')
