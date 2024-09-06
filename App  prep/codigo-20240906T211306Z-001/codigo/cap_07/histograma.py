import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'nome':['João','Maria','Pedro','Roberto','William','Elizabeth','José'],
    'idade':[23,78,22,19,45,33,20],
    'sexo':['M','F','M','M','M','F','M'],
    'peso':[65, 70, 88, 102, 57, 49, 80],
    'estado': ['PE', 'RJ', 'SP', 'PE', 'RJ', 'PE', 'SP']
})

df[['idade']].plot(kind='hist', bins=[0, 20, 40, 60, 80, 100])
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()
