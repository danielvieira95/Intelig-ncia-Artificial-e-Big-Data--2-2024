from collections import Counter
lista_numeros = [0, 1, 2, 2, 1, 2, 0]
lista_strings = ['A', 'B', 'B', 'A', 'C', 'A', 'A', 'C']
c1 = Counter(lista_numeros)
c2 = Counter(lista_strings)
print(f'Lista de números: {lista_numeros}')
print(f'Distribuição dos números: {c1}')
print(f'Lista de letras: {lista_strings}')
print(f'Distribuição das letras: {c2}')