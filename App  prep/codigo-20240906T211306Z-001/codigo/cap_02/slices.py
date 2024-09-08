numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Lista original: {numeros}')
primeiro_elemento = numeros[0]
print(f'Primeiro elemento: {primeiro_elemento}')
ultimo_elemento = numeros[-1]
print(f'Último elemento: {ultimo_elemento}')
penultimo_elemento = numeros[-2]
print(f'Penúltimo elemento: {penultimo_elemento}')
quatro_primeiros = numeros[:4]
print(f'Quatro primeiros elementos: {quatro_primeiros}')
tres_ultimos = numeros[-3:]
print(f'Três últimos elementos: {tres_ultimos}')
sem_os_extremos = numeros[1:-1]
print(f'Sem o primeiro e o último elementos: {sem_os_extremos}')
numeros2 = numeros[:]
print(f'Realizando uma cópia da lista inteira: {numeros2}')
