def coeficiente_angular(x1, y1, x2, y2):
    resultado = 0
    delta_y = y2 - y1
    delta_x = x2 - x1
    if (delta_x==0):
        print('Reta vertical - coeficiente angular -> infinito')
    else:
        resultado = delta_y / delta_x
        print(f'O coeficiente angular da reta formada por ({x1},{y1}) e ({x2},{y2}) é {resultado}')
    return resultado

