A = set()   # Criando um conjunto vazio
print(f'Criado um conjunto vazio: A = {A}')
A.add('X')  # Adicionando um elemento ao conjunto
print(f'Adicionado um elemento ao conjunto A: A = {A}')
A.add('Y')
print(f'Adicionado outro elemento ao conjunto A: A = {A}')
A.add('Z')
print(f'Adicionado mais um elemento ao conjunto A: A = {A}')
A.add(123)
print(f'Adicionado um quarto elemento ao conjunto A: A = {A}')
print(f'A contém agora {len(A)} elementos.')
teste_pertinencia = 'X' in A
print(f'O elemento \'X\' está contido em A? {teste_pertinencia}')
teste_pertinencia = 'a' in A
print(f'O elemento \'a\' está contido em A? {teste_pertinencia}')
