#!/usr/bin/env python3
# -*- coding: utf-8 -*-
itens = []
itens.append("livro")
itens.append("caderno")
itens.append("borracha")
itens[1] = "régua"
if "caderno" in itens:
    print('A lista contém um caderno.')
print(f'A lista possui {len(itens)} elementos.')
ultimo_elemento = itens.pop()
print(f'Após a remoção de {ultimo_elemento}, a lista ficou com {len(itens)} elementos.')
fatia = itens[-2:]
print(f'Os dois últimos elementos da lista são {fatia}.')
