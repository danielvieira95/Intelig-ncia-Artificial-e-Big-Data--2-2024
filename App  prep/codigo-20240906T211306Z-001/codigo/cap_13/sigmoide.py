import matplotlib.pyplot as plt
import numpy as np

def sigmoide(z):
    resultado = 1.0 / (1.0 + np.exp(-z))
    return resultado

z = np.arange(-6, 6, 0.1)
fi_z = sigmoide(z)
plt.plot(z, fi_z)                           # Desenha a curva sigmóide
plt.axvline(0.0, color='k')                 # Eixo Vertical (Y)
plt.axhline(y=0.5, color='k')               # Eixo Horizontal (X)
plt.axhline(y=0.0, color='k', ls='dotted')  # Linha tracejada
plt.axhline(y=1.0, color='k', ls='dotted')  # Linha tracejada
plt.yticks([0.0, 0.5, 1.0])                 # Marcadores no eixo Y
plt.xlabel('z')                             # Legenda do eixo das abscissas (X)
""" Legenda do eixo das ordenadas (Y) - Usando a sintaxe do TeX para imprimir a
                                        letra grega Fi """
plt.ylabel('$\phi (z)$')                
plt.show()