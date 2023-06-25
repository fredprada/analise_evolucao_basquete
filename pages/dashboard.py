import streamlit as st
import plotly.express as px
from functions import transform_to_dataframe, main_metrics, data_transformation

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard", layout="wide")

lista_players = ['Bia','Fred']
player = st.selectbox('Jogador(a):', lista_players)

###################################################################
# Defining metrics
df_all_info = transform_to_dataframe()
dict_metricas = main_metrics(df_all_info, player)

jogos_essa_semana = dict_metricas['jogos_essa_semana']
jogos_semana_passada = dict_metricas['jogos_semana_passada']

###################################################################
# Title and subheader
st.header(f'Oi {player}!')
st.subheader('Dá uma olhadinha aqui nas suas estatísticas')

###################################################################
# Games played metrics
col1, col2 = st.columns(2)
col1.metric(label="Número total de dias jogados", value = dict_metricas['qtd_de_jogos'])
col2.metric(label='Jogos essa semana', value = dict_metricas['jogos_essa_semana'], delta=dict_metricas['jogos_semana_passada'])