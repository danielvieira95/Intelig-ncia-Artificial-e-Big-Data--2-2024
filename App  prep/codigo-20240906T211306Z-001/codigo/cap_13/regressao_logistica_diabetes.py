import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Importação do Dataset
df = pd.read_csv("diabetes.csv", names=['#Gravidezes', 'Glicose', 'PD', 
                                        'DobraTriceps', 'Insulina', 'IMC',
                                        'DiabetesPedigreeFunction', 
                                        'Idade', 'Classe'])
p = stats.normaltest(df['Glicose']).pvalue
print(f'p_value (Glicose) = {p:.3f}')
print('p-value > 0,001 => aceitar a hipótese nula, portanto, a variável \
      (Gllicose) SEGUE uma Distribuição Normal.')
p = stats.normaltest(df['Insulina']).pvalue
print(f'p_value (Insulina) = {p:.3f}')
print('p-value < 0,001 => rejeitar a hipótese nula, portanto, a variável \
      (Insulina) NÃO segue uma Distribuição Normal.')
p = stats.normaltest(df['IMC']).pvalue
print(f'p_value (IMC) = {p:.3f}')
print('p-value > 0,001 => aceitar a hipótese nula, portanto, a variável \
      (IMC) SEGUE uma Distribuição Normal.')
