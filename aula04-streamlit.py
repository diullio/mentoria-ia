## STREAMLIT

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Meu primeiro sistema')
st.write('Aqui esta um exemplo de linha')


df = pd.read_excel('teste.xlsx')
st.dataframe(df)


option = st.selectbox('Escolha um numero:', [1,2,3,4,5])
st.write(f'Voce selecionou o numero {option}')

x = df['Padrao']
y = df['Estoque']

fig, ax = plt.subplots()
ax.plot(x,y)

st.write('Grafico de Padrao x Estoque')
st.pyplot(fig)

st.slider('Escolha um numero', 0, 10)
file = st.file_uploader('Selecione um arquivo')
st.write(file)


calendario = st.date_input('Escolha uma data')

check = st.checkbox('Item1')


items = ['Item1', 'Item2', 'Item3', 'Item4']
opcoes = st.multiselect('Selecione um ou mais itens', items)

radio = st.radio('Escolha uma opcao', items)

color = st.color_picker('Selecione uma cor')


