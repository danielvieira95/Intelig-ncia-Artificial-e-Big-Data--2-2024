valor_medido = 87.0
idade = 13
sexo = 'F'
igual_ou_abaixo_da_media = False

if sexo == 'M':
    if (idade >= 7) and (idade <9):
        if valor_medido <= 89.4:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 9) and (idade <11):
        if valor_medido <= 88.0:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 11) and (idade <13):
        if valor_medido <= 88.92:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 13) and (idade <15):
        if valor_medido <= 92.29:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 15) and (idade <18):
        if valor_medido <= 89.69:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
else:   # sexo = 'F'
    if (idade >= 7) and (idade <9):
        if valor_medido <= 83.72:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 9) and (idade <11):
        if valor_medido <= 88.22:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 11) and (idade <13):
        if valor_medido <= 88.58:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 13) and (idade <15):
        if valor_medido <= 88.85:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
    if (idade >= 15) and (idade <18):
        if valor_medido <= 89.77:
            igual_ou_abaixo_da_media = True
        else:
            igual_ou_abaixo_da_media = False
if igual_ou_abaixo_da_media:
    print('O valor da amostra fornecida é igual ou menor que a média do grupo em estudo.')
else:
    print('O valor da amostra fornecida é superior à média do grupo em estudo.')