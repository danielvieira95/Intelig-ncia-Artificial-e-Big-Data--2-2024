#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

vermelhas = azuis = 0
for i in range(1, 11):
    cor = random.randint(0,2)
    if cor == 0:
        vermelhas = vermelhas + 1
    else:
        azuis = azuis + 1
print('Resultado:')
print(f'Azuis: {azuis}')
print(f'Vermelhas: {vermelhas}')
if azuis > vermelhas:
    print('As azuis venceram.')
elif vermelhas > azuis:
    print('As vermelhas venceram.')
else:
    print('Houve um empate.')