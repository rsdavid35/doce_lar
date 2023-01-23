# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:04:29 2023

@author: David Rodrigues
"""

import pandas as pd
import numpy as np

data = pd.read_csv('Housing.csv')[['price', 'area', 'bedrooms', 'bathrooms']]

# retorna o conjunto de dados
def obter_dados():
    return data

def dados_input():
    range_area = (int(data['area'].min()), int(data['area'].max()))
    arr_quarto = np.sort(data['bedrooms'].value_counts().index)
    arr_banheiro = np.sort(data['bathrooms'].value_counts().index)
    return {'range_area': range_area,
            'arr_quarto': arr_quarto,
            'arr_banheiro': arr_quarto}

# filtra os dados de acordo com as informações passadas
def filtrar_dados(area, bedrooms, bathrooms, df=data):
    df = df.loc[(area[0]<=df['area'])&(df['area']<area[1])]
    df = df.loc[df['bedrooms']==bedrooms]
    df = df.loc[df['bathrooms']==bathrooms]
    return df

# calcula os indicadores da interface
def stats_dados(df=data):
    media_valor = round(df['price'].mean(), 2)
    media_geral = round(data['price'].mean(), 2)
    delta = round(media_valor - media_geral, 2)
    menor_valor = df['price'].min()
    maior_valor = df['price'].max()
    arr_valor = df['price']
    return {'media_valor': media_valor,
            'media_geral':media_geral,
            'delta':delta,
            'menor_valor':menor_valor,
            'maior_valor':maior_valor,
            'arr_valor': arr_valor}