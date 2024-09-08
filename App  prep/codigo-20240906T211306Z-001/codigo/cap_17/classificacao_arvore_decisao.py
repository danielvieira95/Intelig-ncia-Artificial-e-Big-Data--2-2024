#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classificação usando Árvore de Decisão

"""

# Importando os módulos das bibliotecas
import matplotlib.pyplot as plt
from sklearn import datasets

# Carregando o dataset
iris = datasets.load_iris()

# Carregando o módulo Árvore da biblioteca sklearn
from sklearn import tree

# Carretando X e y do dataset
X,y = iris.data, iris.target

# Criando um novo Classificador do tipo
# árvore de decisão
classificador = tree.DecisionTreeClassifier(max_depth=3, random_state=0)

# Chamando o método fit
classificador.fit(X,y)

# Setando a variárvel figsize do objeto plot
fig = plt.figure(figsize=(30,25))

# Imprimindo a árvore
tree.plot_tree(classificador, \
               feature_names=iris.feature_names,  \
                   class_names=iris.target_names, \
                       filled=False)

# gerando os gráficos de dispersão
# agrupando por comprimento da sépala e comprimento da pétala
plt.figure(figsize=(15, 10))
plt.scatter(iris.data[:, 0], iris.data[:, 2], c=iris.target)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[2])

plt.tight_layout()
plt.show()


# agrupando por comprimento da pétala e largura da pétala
plt.figure(figsize=(15, 10))
plt.scatter(iris.data[:, 2], iris.data[:, 3], c=iris.target)
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])

plt.tight_layout()
plt.show()