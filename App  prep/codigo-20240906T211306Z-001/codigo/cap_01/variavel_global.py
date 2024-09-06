""" Exemplo de variável global """

codigo = "123321"  # Definição fora do corpo da função – variável global

def testar():
    print(f'Dentro da funçao testar(), codigo = {codigo}')

testar()
print(f'Fora da funçao testar(), codigo = {codigo}')