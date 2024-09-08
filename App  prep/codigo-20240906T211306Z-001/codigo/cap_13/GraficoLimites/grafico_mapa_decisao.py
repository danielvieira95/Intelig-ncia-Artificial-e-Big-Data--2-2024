import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

X = None
y = None
titulo_grafico = ""
titulo_eixo_x = ""
classificador = None
x1 = -999999
x2 = -999999

def criar_grafico(_X: 'Variáveis independentes', _y: 'Variável dependente',
             _classificador: 'Classificador do SKLearn', _titulo_grafico: str,
             _titulo_eixo_x: str) -> None:
    global X, y, titulo_grafico, titulo_eixo_x, classificador
    X = _X
    y = _y
    titulo_grafico = _titulo_grafico
    titulo_eixo_x = _titulo_eixo_x
    classificador = _classificador

def exibir() -> None:
    __definir_grid()
    __definir_contorno_grafico()
    __limitar_eixos()
    __definir_scatter_plot()
    __inicializar_titulo_e_legendas()
    plt.show()

def __definir_grid() -> None:
    global x1, x2
    x1, x2 = np.meshgrid(
        np.arange(start=X[:, 0].min() - 1, stop=X[:, 0].max() + 1, step=0.01),
        np.arange(start=X[:, 1].min() - 1, stop=X[:, 1].max() + 1, step=0.01))

def __definir_contorno_grafico() -> None:
    global x1, x2
    plt.contourf(x1, x2, 
                 classificador.predict(
                     np.array([x1.ravel(), x2.ravel()]).T)
                    .reshape(x1.shape), 
                 alpha=0.5, cmap=ListedColormap(('red', 'blue')))

def __limitar_eixos() -> None:
    plt.xlim(x1.min(), x1.max())
    plt.ylim(x2.min(), x2.max())

def __definir_scatter_plot() -> None:
    global X, y
    for i, j in enumerate(np.unique(y)):
        plt.scatter(X[y == j, 0], X[y == j, 1], c=ListedColormap(('red', 'blue'))(i), label=j)

def __inicializar_titulo_e_legendas() -> None:
    global titulo_grafico
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.title(titulo_grafico)
