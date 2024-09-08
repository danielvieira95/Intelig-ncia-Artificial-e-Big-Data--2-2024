#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

numeros = []
for i in range(101):
    numeros.append(True)
i = 2
while(i <= int(math.sqrt(100))):
    if numeros[i]:
        for j in range(i*2, 101, i):
            numeros[j]=False
    i = i+1
for i in range(2,101):
  if numeros[i]:
      print(i)
