#!/usr/bin/env python3
# -*- coding: utf-8 -*-
teste = [1, 2, 3, 4, 5]
# Lembre-se que as listas sÃ£o baseadas em zero
print(f'O segundo elemento da lista é {teste[1]}.')
print(f'E o conteúdo da lista completa: {teste}.')
teste2 = [6, 7, 8, 9, 10]
teste.extend(teste2)
print(f'Após acrescentar {teste2}: {teste}')