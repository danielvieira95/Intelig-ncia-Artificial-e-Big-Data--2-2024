import pandas as pd

df = pd.read_csv("diabetes.csv", names=['#Gravidezes', 'Glicose', 'PD', \
                                        'DobraTriceps', 'Insulina', 'IMC', \
                                        'DiabetesPedigreeFunction', 'Idade', \
                                        'Classe'])
print(f'Linhas antes da exclusão: {len(df)}')
excluir_glicose_0 = df.index[df.Glicose == 0].tolist()
excluir_pd_0 = df.index[df['PD'] == 0].tolist() # Selecionando de outra forma
excluir_triceps_0 = df.index[df.DobraTriceps == 0].tolist()
excluir_insulina_0 = df.index[df.Insulina == 0].tolist()
excluir_imc_0 = df.index[df.IMC == 0].tolist()
temp = excluir_glicose_0
temp += excluir_pd_0
temp += excluir_triceps_0
temp += excluir_insulina_0
temp += excluir_imc_0
df = df.drop(df.index[temp])
classe_0 = len(df[df['Classe'] == 0])
classe_1 = len(df[df['Classe'] == 1])
print(f'Linhas após a exclusão: {len(df)}')
print(f'Pessoas COM diabetes na amostra: {classe_0} ({(classe_0 * 100 / (classe_0 + classe_1)):.2f}%)')
print(f'Pessoas SEM diabetes na amostra: {classe_1} ({(classe_1 * 100 / (classe_0 + classe_1)):.2f}%)')
df.to_csv('diabetes_preprocessado.csv', header=False)
