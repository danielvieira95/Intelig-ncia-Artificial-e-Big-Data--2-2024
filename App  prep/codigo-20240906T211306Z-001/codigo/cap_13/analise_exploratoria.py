import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("diabetes_preprocessado.csv", names=['#Gravidezes', 'Glicose', 'PD', \
                                        'DobraTriceps', 'Insulina', 'IMC', \
                                        'DiabetesPedigreeFunction', 'Idade', \
                                        'Classe'])
com_diabetes = df[df.Classe==1]
sem_diabetes = df[df.Classe==0]

for variavel in df.columns:
    if variavel != 'Classe':
        # Histograma da variável:
        plt.figure(figsize=(10, 3))
        plt.subplot(1,3,1)
        plt.title('Histograma - ' + variavel + ' (Toda a amostra)')
        sns.distplot(df[variavel],kde=False)
        plt.subplot(1,3,2)
        # Histograma por classe:
        sns.distplot(sem_diabetes[variavel],kde=False,color="Blue", 
                     label=variavel + " sem Diabetes")
        sns.distplot(com_diabetes[variavel],kde=False,color="Red", 
                     label=variavel + " com Diabetes")
        plt.title("Histograma para " + variavel + " por Classe")
        plt.legend(['Sem Diabetes', 'Com Diabetes'])
        # Boxplot por classe:
        plt.subplot(1,3,3)
        sns.boxplot(x=df.Classe,y=df[variavel])
        sns.boxplot(x=df.Classe,y=df[variavel])
        plt.title("Boxplot para " + variavel + " por Classe")
