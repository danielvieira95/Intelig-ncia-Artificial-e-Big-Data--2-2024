import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("diabetes_preprocessado.csv", 
                     names=['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', \
                            'Insulina', 'IMC', 'DiabetesPedigreeFunction', \
                            'Idade', 'Classe'])

# Seleção dos atributos:
# Variáveis independentes:
X = df.drop('Classe', axis=1)
y = df['Classe']

# Padronização dos dados:
escalonador = StandardScaler()
X = escalonador.fit_transform(X)
df_X = pd.DataFrame(X)

X_treino, X_teste, y_treino, y_teste = train_test_split(df_X, y, test_size = 0.15)

# Criando e treinando o classificador:
algoritmo = LogisticRegression()
algoritmo.fit(X_treino, y_treino)

# Realizando previsões sobre os dados de teste:
y_previsao = algoritmo.predict(X_teste)

# Verificando a acurácia do modelo:
score = algoritmo.score(X_teste, y_teste)
print(f'Acurácia do modelo: {score:.2f}')

import grafico_mapa_decisao_oo as mapa

mapa_log = mapa.GraficoMapaDecisao(X_treino, y_treino, algoritmo, 
                                   "Mapa de Decisão - Regressão Logística", 
                                   "Diabetes", "Classe")
mapa_log.exibir()