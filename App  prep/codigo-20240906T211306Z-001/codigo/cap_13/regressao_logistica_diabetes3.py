import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

# Importação dos dados:
df = pd.read_csv("diabetes.csv", names=['#Gravidezes', 'Glicose', 'PD', \
                                        'DobraTriceps', 'Insulina', 'IMC', \
                                        'DiabetesPedigreeFunction', 'Idade', \
                                        'Classe'])
arquivo = ProfileReport(df)
arquivo.to_file(output_file='relatorio.html')