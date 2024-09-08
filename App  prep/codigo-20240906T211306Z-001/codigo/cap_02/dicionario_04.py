from collections import defaultdict
genero = defaultdict(lambda:'Ficção')
genero['Tá todo mundo louco'] = 'Comédia'
genero['Avatar'] = 'Fantasia'
print('Alguns gêneros cadastrados:')
print(f'Tá todo mundo louco: {genero["Tá todo mundo louco"]}')
print(f'Avatar: {genero["Avatar"]}')
print(f'Star Wars: {genero["Star Wars"]}')