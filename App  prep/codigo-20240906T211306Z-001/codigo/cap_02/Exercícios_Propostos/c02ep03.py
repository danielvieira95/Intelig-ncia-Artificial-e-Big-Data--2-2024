#!/usr/bin/env python3
# -*- coding: utf-8 -*-
primos = {2, 3, 5, 7, 11, 13, 17, 19}
pares = {0, 2, 4, 6, 8, 10}
impares = {11, 13, 15, 17, 19}
resultado = pares | (primos & impares)
print(resultado)
