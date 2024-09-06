import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'nome':['João','Maria','Pedro','Roberto','William','Elizabeth','José'],
    'idade':[23,78,22,19,45,33,20],
    'sexo':['M','F','M','M','M','F','M'],
    'peso':[65, 70, 88, 102, 57, 49, 80],
    'estado': ['PE', 'RJ', 'SP', 'PE', 'RJ', 'PE', 'SP']
})

# Obtem o eixo atual (gca = "get current axis"):
eixo = plt.gca()

# Desenha dois gráficos de linha no mesmo eixo:
df.plot(kind='line', x='nome', y='idade', color='grey', ax=eixo)
df.plot(kind='line', x='nome', y='peso', color='black', ax=eixo)

# Exibe o gráfico gerado pelo PyPlot:
plt.show()
