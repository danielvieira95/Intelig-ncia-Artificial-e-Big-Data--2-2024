import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

# Importação dos dados:
df = pd.read_csv("diabetes.csv", names=['#Gravidezes', 'Glicose', 'PD', \
                                        'DobraTriceps', 'Insulina', 'IMC', \
                                        'DiabetesPedigreeFunction', 'Idade', \
                                        'Classe'])
print('Estatísticas Descritivas:')
print(df.describe())
print('\nContando os zeros na amostra:\n')
print(f'Número de gravidezes: {(df["#Gravidezes"]==0).sum()}')
print(f'Glicose: {(df["Glicose"]==0).sum()}')
print(f'Pressão diastólica: {(df["PD"]==0).sum()}')
print(f'Espessura da dobra do tríceps: {(df["DobraTriceps"]==0).sum()}')
print(f'Insulina: {(df["Insulina"]==0).sum()}')
print(f'IMC: {(df["IMC"]==0).sum()}')
print(f'Idade: {(df["Idade"]==0).sum()}')
