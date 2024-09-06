import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


class GraficoMapaDecisao:
    def __init__(self, X: 'Variáveis independentes', y: 'Variável dependente',
                 classificador: 'Classificador do SKLearn', titulo_grafico: str, titulo_eixo_x: str) -> None:
        self.__X = X
        self.__y = y
        self.__titulo_grafico = titulo_grafico
        self.__titulo_eixo_x = titulo_eixo_x
        self.__classificador = classificador

    def exibir(self) -> None:
        self.__definir_grid()
        self.__definir_contorno_grafico()
        self.__limitar_eixos()
        self.__definir_scatter_plot()
        self.__inicializar_titulo_e_legendas()
        plt.show()

    def __definir_grid(self) -> None:
        self.__x1, self.__x2 = np.meshgrid(
            np.arange(start=self.__X[:, 0].min() - 1, stop=self.__X[:, 0].max() + 1, step=0.01),
            np.arange(start=self.__X[:, 1].min() - 1, stop=self.__X[:, 1].max() + 1, step=0.01))

    def __definir_contorno_grafico(self) -> None:
        plt.contourf(self.__x1, self.__x2,
                     self.__classificador.predict(np.array([self.__x1.ravel(), self.__x2.ravel()]).T).reshape(
                         self.__x1.shape), alpha=0.5, cmap=ListedColormap(('red', 'blue')))

    def __limitar_eixos(self) -> None:
        plt.xlim(self.__x1.min(), self.__x1.max())
        plt.ylim(self.__x2.min(), self.__x2.max())

    def __definir_scatter_plot(self) -> None:
        for i, j in enumerate(np.unique(self.__y)):
            plt.scatter(self.__X[self.__y == j, 0], self.__X[self.__y == j, 1], c=ListedColormap(('red', 'blue'))(i),
                        label=j)

    def __inicializar_titulo_e_legendas(self) -> None:
        plt.xlabel('X')
        plt.ylabel('y')
        plt.legend()
        plt.title(self.__titulo_grafico)
