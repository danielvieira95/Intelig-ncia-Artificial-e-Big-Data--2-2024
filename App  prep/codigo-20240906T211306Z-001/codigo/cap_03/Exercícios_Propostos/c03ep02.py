lado1 = 6
lado2 = 8
lado3 = 10
resultado = False
if (lado1 > lado2) and (lado1 > lado3):
    hipotenusa = lado1
    cateto1 = lado2
    cateto2 = lado3
if (lado2 > lado1) and (lado2 > lado3):
    hipotenusa = lado2
    cateto1 = lado1
    cateto2 = lado3
if (lado3 > lado1) and (lado3 > lado2):
    hipotenusa = lado3
    cateto1 = lado1
    cateto2 = lado2
if ((hipotenusa**2) == (cateto1**2) + (cateto2**2)):
    print('Os valores fornecidos formam um triângulo retângulo.')
else:
    print('Os valores fornecidos NÃO FORMAM um triângulo retângulo.')
