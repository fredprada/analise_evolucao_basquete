import streamlit as st
# import plotly.express as px
from functions import transform_to_dataframe, main_metrics, data_transformation

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard")

col1, col2 = st.columns(2)

players_list = ['Bia',
                'Fred']

df_all_info = transform_to_dataframe()
player = st.selectbox('Jogador(a):', (players_list))
data_transformation(df_all_info)

main_metrics_list = main_metrics(df_all_info, player)
dias_jogados = len(df_all_info['dia'].value_counts())
jogos_essa_semana = main_metrics(df_all_info, player)

with col1:
    st.header('Sobre o seu último jogo')
    st.metric(label="Número de dias jogados", value=dias_jogados, delta=1)

st.metric(label='jogos essa semana: ', value = jogos_essa_semana)