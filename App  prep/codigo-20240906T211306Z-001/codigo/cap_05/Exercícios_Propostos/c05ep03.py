#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def custo(distancia_km, consumo_km_l, preco_litro):
    resultado = (distancia_km / consumo_km_l) * preco_litro
    print(f'Para essa viagem, o gasto com combustivel será de R$ {resultado:.2f}.')
    return resultado
