lista_duplicados = ['A', 'B', 'C', 'B', 'A', 'C']
print(f'Conteúdo inicial da lista: {lista_duplicados}')
print('Convertendo a lista em conjunto para eliminar duplicidades...')
conjunto = set(lista_duplicados)
print('Convertendo o conjunto em uma lista sem duplicações...')
lista_sem_duplicacoes = list(conjunto)
print(f'Conteúdo da lista sem valores duplicados: {lista_sem_duplicacoes}')