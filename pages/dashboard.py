import streamlit as st
import plotly.express as px
from functions import transform_to_dataframe, main_metrics, data_transformation

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard")

lista_players = ['Bia','Fred']
player = st.selectbox('Jogador(a):', lista_players)

df_all_info = transform_to_dataframe()
data_transformation(df_all_info)

main_metrics_list = main_metrics(df_all_info, player)
dias_jogados = len(df_all_info['dia'].value_counts())
jogos_essa_semana = main_metrics(df_all_info, player)

st.header(f'Oi {player}!')
st.subheader('Dá uma olhadinha aqui nas suas estatísticas')

col1, col2 = st.columns(2)
col1.metric(label="Número de dias jogados", value=dias_jogados)
col2.metric(label='jogos essa semana: ', value = jogos_essa_semana, delta=3)