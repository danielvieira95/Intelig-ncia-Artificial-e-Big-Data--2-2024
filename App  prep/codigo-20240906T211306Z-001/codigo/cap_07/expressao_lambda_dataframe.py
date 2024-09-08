import pandas as pd
import numpy as np

cubo = lambda x: x**3
formato_decimal = lambda x:'%.1f' % x  
# Criando um DataFrame:
matriz_4x3 = np.array([[1, 2, 3, 4],
                       [2, 4, 6, 8],
                       [3, 8, 12, 16],
                       [4, 16, 24, 32]])
df = pd.DataFrame(matriz_4x3)
print(f'DataFrame original:\n {df}\n')
df_cubo = df.apply(cubo)
print(f'Elevando os elementos ao cubo:\n {df_cubo}\n')
df_cubo = df_cubo.applymap(formato_decimal)
print(f'Formatando para uma casa decimal:\n {df_cubo}')
