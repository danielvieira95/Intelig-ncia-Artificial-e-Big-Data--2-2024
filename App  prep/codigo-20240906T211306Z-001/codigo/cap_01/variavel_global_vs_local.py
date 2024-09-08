teste1 = 123

def funcao_f():
    global teste2
    teste2 = 456
    for x in range(1,10):
        z = x * 2
        print(f'z = {z}')
    print(f'Valor de z, após o loop: {z}')
    print(f'Valor de teste1, dentro da função: {teste1}')
    print(f'Valor de teste2, dentro da função: {teste2}')

funcao_f()
print(f'Valor de teste1, fora da função: {teste1}')
print(f'Valor de teste2, fora da função: {teste2}')
print(f'Valor de z, após o loop: {z}')
