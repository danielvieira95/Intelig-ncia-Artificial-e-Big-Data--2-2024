import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'nome':['João','Maria','Pedro','Roberto','William','Elizabeth','José'],
    'idade':[23,78,22,19,45,33,20],
    'sexo':['M','F','M','M','M','F','M'],
    'peso':[65, 70, 88, 102, 57, 49, 80],
    'estado': ['PE', 'RJ', 'SP', 'PE', 'RJ', 'PE', 'SP']
})

# Cria uma nova coluna de nome "temp" no DataFrame, contendo 1 e
# agrupa os dados por estado:
df.assign(temp=1).groupby(
  ['temp','estado']
).size().to_frame().unstack().plot(kind='bar',stacked=True,legend=False)

plt.title('Número de registros por estado')
plt.xlabel('Estado')
plt.xticks([]) # Removendo os traçados no eixo das ordenadas

# Adicionando legendas:
handles, _ = plt.gca().get_legend_handles_labels()
handles_invertidos = reversed(handles)

legendas = reversed(df['estado'].unique())

plt.legend(handles_invertidos, legendas, loc='top right')
plt.show()
