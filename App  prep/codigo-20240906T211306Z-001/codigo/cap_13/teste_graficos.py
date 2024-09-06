import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
 
def plot_chart(classifier, X_test, y_test):
    print('X_test.shape', X_test.shape)
    print('y_test.shape', y_test.shape)
    x_set, y_set = X_test, y_test
    x1, x2 = np.meshgrid(np.arange(start=x_set[:, 0].min() - 1, stop=x_set[:, 0].max() + 1, step=0.01),
                         np.arange(start=x_set[:, 1].min() - 1, stop=x_set[:, 1].max() + 1, step=0.01))
    plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(x1.min(), x1.max())
    plt.ylim(x2.min(), x2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title('Limites de Decisão do Algoritmo')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()

