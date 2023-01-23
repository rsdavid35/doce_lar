# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:53:31 2023

@author: David Rodrigues
"""

from doce_lar import *
from PIL import Image
import streamlit as st
import locale
locale.setlocale( locale.LC_ALL, '' )

#title
st.title('Doce Lar')

# imagem
image = Image.open('img/hs.jpg')
st.image(image)

# inputs
range_area = dados_input()['range_area']
arr_quarto = dados_input()['arr_quarto']
arr_banheiro = dados_input()['arr_banheiro']

col_area, col_quarto, col_banheiro = st.columns(3)
with col_area:
    input_area = st.slider('Área [SqFt]',
                           value=range_area,
                           min_value=range_area[0],
                           max_value=range_area[1],)
with col_quarto:
    input_quarto = st.selectbox('Número de quartos', options=arr_quarto)
with col_banheiro:
    input_banheiro =st.selectbox('Número de banheiros', options=arr_quarto)
    
# indicadores
dados_filtrados = filtrar_dados(input_area,
                                int(input_quarto),
                                int(input_banheiro))
ind = stats_dados(dados_filtrados)

col_media, col_max, col_min = st.columns(3)
with col_media:
    if ind['delta'] >= 0:
        delta = "${:,.2f}".format(ind['delta']/10**6)
    else:
        delta = "-${:,.2f}".format(abs(ind['delta']/10**6))
    st.metric('Média de Preço (em milhões)',
              value=locale.currency( ind['media_valor']/10**6, grouping=True ),
              delta= delta)
    st.caption('Comparação com a Média Geral')
with col_min:
    st.metric('Menor Preço (em milhões)',
              value=locale.currency( ind['menor_valor']/10**6, grouping=True ))
    with col_max:
        st.metric('Maior Preço (em milhões)',
                  value=locale.currency( ind['maior_valor']/10**6, grouping=True ))
      
# tabela
col_tabela, col_descricao = st.columns(2)
with col_tabela:
    st.dataframe(dados_filtrados, height=200)

with col_descricao:
    st.write('Você pode baixar os dados filtrados clicando no botão abaixo.')
    
    # baixar dados
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    
    csv = convert_df(dados_filtrados)
    
    st.download_button(
        label="Baixar dados",
        data=csv,
        file_name='housing.csv',
        mime='text/csv',
    )
