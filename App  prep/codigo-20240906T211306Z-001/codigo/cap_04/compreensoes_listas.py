print('Entendendo List Comprehensions:')
print('C1 = {x**3 | 0<=x<=3}')
c1 = [x**3 for x in range(4)]
print(c1, sep=' ')
print('C2 = {x**3 | 0<=x<=20 e x é par}')
c2 = [x * 2 for x in range(0, 11)]
print(c2, sep=' ')
print('C3 = {x | -20<=x<=40 e x é ímpar}')
c3 = [x * 2 + 1 for x in range(-10, 20)]
print(c3, sep=' ')
