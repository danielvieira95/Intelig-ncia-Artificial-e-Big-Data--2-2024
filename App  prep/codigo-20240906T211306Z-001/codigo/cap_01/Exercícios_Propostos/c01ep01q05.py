#!/usr/bin/env python3
# -*- coding: utf-8 -*-
palavra = "Teste"
numero = 15
booleano = True
print('Usando %%: palavra = \'%s\', numero=%d, booleano=%s' % (palavra, numero, 
                                                               booleano))
print(f'Usando f-string: palavra=\'{palavra}\', numero={numero}, booleano={booleano}')