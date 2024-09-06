#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def consumo(distancia_km, consumo_km_l):
    resultado = distancia_km / consumo_km_l
    print(f'Para essa viagem, serão necessários {resultado} litros de combustivel.')
    return resultado
