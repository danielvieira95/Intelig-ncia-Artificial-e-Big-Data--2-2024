# Correction Matrix Plot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

atributos = ['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', 'Insulina', \
             'IMC', 'DiabetesPedigreeFunction', 'Idade', 'Classe']
df = pd.read_csv("diabetes_preprocessado.csv", names=atributos)
correlations = df.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
titulos_abreviados = ['grav', 'glic', 'PD', 'tric', 'ins', \
             'IMC', 'DPF', 'Idad', 'Clas']
ax.set_xticklabels(titulos_abreviados)
ax.set_yticklabels(titulos_abreviados)
plt.show()