import pandas as pd
from pandas.plotting import scatter_matrix

df = pd.read_csv("diabetes_preprocessado.csv", names=['#Gravidezes', 'Glicose', 'PD', \
                                        'DobraTriceps', 'Insulina', 'IMC', \
                                        'DiabetesPedigreeFunction', 'Idade', \
                                        'Classe'])
scatter_matrix(df, figsize=(15,15))
