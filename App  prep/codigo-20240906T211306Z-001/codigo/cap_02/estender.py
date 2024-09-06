#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:01:15 2019

@author: amilcar, francisco
"""
usuarios = []
usuarios_informatica = ['Adriano','Bruno','Carlos']
usuarios_contabilidade = ['Daniele', 'Elisa','Fernanda']
print(f'Lista vazia de usuários: {usuarios}')
print(f'Usuários da informática: {usuarios_informatica}')
print(f'Usuários da contabilidade: {usuarios_contabilidade}')
print('Unindo as listas. Primeiro, testando com a informática:')
usuarios.extend(usuarios_informatica)
print(usuarios)
print('Agora, acrescentando a contabilidade:')
usuarios.extend(usuarios_contabilidade)
print(usuarios)
