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
print(f'Linhas após a exclusão: {len(df)}')
