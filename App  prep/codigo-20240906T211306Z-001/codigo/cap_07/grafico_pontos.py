import pandas as pd

df = pd.read_csv('placement.csv')
df.plot(kind='scatter', x='degree_t', y='age')
