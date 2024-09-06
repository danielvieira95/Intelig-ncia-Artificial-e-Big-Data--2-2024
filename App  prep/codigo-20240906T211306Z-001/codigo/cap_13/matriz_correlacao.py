# Correction Matrix Plot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

atributos = ['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', 'Insulina', \
             'IMC', 'DiabetesPedigreeFunction', 'Idade', 'Classe']
df = pd.read_csv("diabetes_preprocessado.csv", names=atributos)
matriz = df.corr()
# plot correlation matrix
grafico = plt.figure()
subgrafico = grafico.add_subplot(111)
cax = subgrafico.matshow(matriz, vmin=-1, vmax=1)
grafico.colorbar(cax)
ticks = np.arange(0,9,1)
subgrafico.set_xticks(ticks)
subgrafico.set_yticks(ticks)
titulos_abreviados = ['grav', 'glic', 'PD', 'tric', 'ins', \
             'IMC', 'DPF', 'Idad', 'Clas']
subgrafico.set_xticklabels(titulos_abreviados)
subgrafico.set_yticklabels(titulos_abreviados)
plt.show()