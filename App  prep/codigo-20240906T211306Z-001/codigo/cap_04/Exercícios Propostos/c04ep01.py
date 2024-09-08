#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for x in range(2000,5001):
    if (x % 2 == 0) and (x % 3 == 0) and (x % 4 == 0):
        print(f'{x} é par e divisível, simultaneamente, por 3 e 4.')
