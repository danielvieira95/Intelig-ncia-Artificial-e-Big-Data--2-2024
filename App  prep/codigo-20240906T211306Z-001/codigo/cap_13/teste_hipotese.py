import pandas as pd
from scipy.stats import shapiro

df = pd.read_csv("diabetes_preprocessado.csv", 
                     names=['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', \
                            'Insulina', 'IMC', 'DiabetesPedigreeFunction', \
                            'Idade', 'Classe'])
stat, p = shapiro(df['PD'])
print(f'Estatística={stat:.3f}, p={p:.3f}')
alfa = 0.4     # Nível de significância de 5% (ou: margem de erro de 2,5% para mais ou para menos)
if p > alfa:
    print('Não é possível rejeitar a hipótese nula (PD segue uma Distribuição Normal)')
else:
    print('Hipótese nula rejeitada (PD NÃO segue uma Distribuição Normal)')
stat, p = shapiro(df['IMC'])
print(f'Estatística={stat:.3f}, p={p:.3f}')
if p > alfa:
    print('Não é possível rejeitar a hipótese nula (IMC segue uma Distribuição Normal)')
else:
    print('Hipótese nula rejeitada (IMC NÃO segue uma Distribuição Normal)')
