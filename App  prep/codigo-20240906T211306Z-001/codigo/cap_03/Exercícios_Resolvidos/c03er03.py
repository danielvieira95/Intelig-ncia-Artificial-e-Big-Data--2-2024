#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
numero_aleatorio = random.randint(-100,101) # Gera um número entre -100 e 100
if numero_aleatorio > 0:
    print(f'O número {numero_aleatorio} é positivo.')
elif numero_aleatorio <0:
    print(f'O número {numero_aleatorio} é negativo.')
else:
    print(f'O número {numero_aleatorio} é neutro.')
    