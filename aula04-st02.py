import streamlit as st
import pandas as pd


##navbar
selected = st.selectbox("Navegação", ['Home', "Sobre", "Codigo"])

if selected == 'Home':
    st.write('Voce esta na pagina inicial')
elif selected == 'Sobre':
    st.write('Pagina Sobre')
elif selected == "Codigo":

    ## organizar meu codigo = colunas

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('Coluna 1')
        st.button("Botao 1")

    with col2:
        st.write('Coluna 2')
        st.button('Botao 2')

    with col3:
        st.write('Coluna3')
        st.button('Botao3')

    st.write('Novo teste com colunas fazendo um teste para verificar se ele esta dentro da coluna')

    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.write('Coluna estreita a esquerda')

    with col2:
        st.markdown(
            """
            <h2 style="text-align:center"><span style="color:#FF0000"><span style="font-size:14px"><span style="font-family:arial,helvetica,sans-serif"><em><strong>Este &eacute; um texto centralizado</strong></em></span></span></span></h2>   


            """, unsafe_allow_html=True
        )
        st.write("Coluna central larga")

    with col3:
        st.write("Coluna Estreita a Direita")





