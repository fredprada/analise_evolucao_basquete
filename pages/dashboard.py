import streamlit as st
import plotly.express as px
import pandas as pd
from functions import transform_to_dataframe, main_metrics, get_numeric_stats, get_specific_dataframe

######################################################################################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard", layout="wide")

lista_players = ['Bia','Fred']
player = st.selectbox('Jogador(a):', lista_players)

######################################################################################################################################
# Defining metrics
df_all_info = transform_to_dataframe()
dict_metricas = main_metrics(df_all_info, player)
dict_numeric_stats = get_numeric_stats(df_all_info, player)
specific_dataframe = get_specific_dataframe(df_all_info, player)

jogos_essa_semana = dict_metricas['jogos_essa_semana']
jogos_semana_passada = dict_metricas['jogos_semana_passada']
jogos_por_semana = dict_metricas['jogos_por_semana']

######################################################################################################################################
# Title and subheader
st.header(f'Oi {player}!')
st.subheader('Dá uma olhadinha aqui nas suas estatísticas 😉')
# st.text(dict_numeric_stats)

######################################################################################################################################
# Current and last week numeric metrics
col1, col2, col3, col4, col5, col6, col7= st.columns(7)
period_in_time = col1.selectbox('',['esta semana vs semana passada', 'esta semana', 'semana passada'])# 'este mês vs mês passado'])

dict_tempo_jogado = dict_numeric_stats['specific_dataframe']['tempo_jogado']
dict_calorias = dict_numeric_stats['specific_dataframe']['calorias']
dict_nota = dict_numeric_stats['specific_dataframe']['nota']
dict_pai = dict_numeric_stats['specific_dataframe']['pai']

col3.metric(label="🏀 Jogos", 
            value = dict_metricas['qtd_de_jogos'])
col4.metric(label='⌚ Minutos jogados', 
            value = dict_tempo_jogado['tempo_jogado_soma'])
col5.metric(label='🔥 Calorias gastas', 
            value = dict_calorias['calorias_soma'])
col6.metric(label='👍 Nota média', 
            value = dict_nota['nota_media'])
col7.metric(label='🥇 PAI', 
            value = dict_pai['pai_soma'])

_, _, col3, col4, col5, col6, col7= st.columns(7)
if period_in_time == 'esta semana':
    # col1.text(period_in_time)
    col3.metric(label="🏀", 
                value = dict_metricas['jogos_essa_semana'])
    col4.metric(label="⌚", 
                value = dict_tempo_jogado['tempo_jogado_soma_essa_semana'])
    col5.metric(label="🔥", 
                value = dict_calorias['calorias_soma_essa_semana'])
    col6.metric(label="👍", 
                value = dict_nota['nota_media_essa_semana'])
    col7.metric(label="🥇",
                value = dict_pai['pai_soma_essa_semana'])
elif  period_in_time == 'semana passada':
    # col1.text(period_in_time)
    col3.metric(label="🏀", 
                value = dict_metricas['jogos_semana_passada'])
    col4.metric(label="⌚", 
                value = dict_tempo_jogado['tempo_jogado_soma_semana_passada'])
    col5.metric(label="🔥", 
                value = dict_calorias['calorias_soma_semana_passada'])
    col6.metric(label="👍", 
                value = dict_nota['nota_media_semana_passada'])
    col7.metric(label="🥇",
                value = dict_pai['pai_soma_semana_passada'])
elif  period_in_time == 'esta semana vs semana passada':
    # col1.text(period_in_time)
    col3.metric(label="🏀", 
                value = dict_metricas['jogos_essa_semana'], 
                delta = dict_metricas['jogos_essa_semana'] - dict_metricas['jogos_semana_passada'])
    col4.metric(label="⌚", 
                value = dict_tempo_jogado['tempo_jogado_soma_essa_semana'],
                delta = dict_tempo_jogado['tempo_jogado_soma_essa_semana'] - dict_tempo_jogado['tempo_jogado_soma_semana_passada'])
    col5.metric(label="🔥", 
                value = dict_calorias['calorias_soma_essa_semana'],
                delta = dict_calorias['calorias_soma_essa_semana'] - dict_calorias['calorias_soma_semana_passada'])
    col6.metric(label="👍",
                value = dict_nota['nota_media_essa_semana'],
                delta = dict_nota['nota_media_essa_semana'] - dict_nota['nota_media_semana_passada'])
    col7.metric(label="🥇",
                value = dict_pai['pai_soma_essa_semana'],
                delta = dict_pai['pai_soma_essa_semana'] - dict_pai['pai_soma_semana_passada'])

######################################################################################################################################
period_to_display = st.selectbox('',['semanal', 'diário'])
col1, col2 = st.columns([1, 2])

# Plotting games per week
fig = px.bar(jogos_por_semana, x="numero_da_semana", y="qtd", text="qtd")
fig.update_traces(textposition="outside")
fig.update_layout(xaxis_title="Número da semana", yaxis_title="Dias que jogou", yaxis_range=[0, 7],width=600,height=400)
fig.update_traces(marker=dict(color='#20837b'))
col1.plotly_chart(fig, theme=None, use_container_width=True)

######################################################################################################################################
# Plotting "PAI" per day
grouped_data = specific_dataframe.groupby('numero_da_semana')['pai'].sum().to_dict()
x = list(grouped_data.keys())
y = list(grouped_data.values())

if period_to_display == 'semanal':
    fig = px.bar(x=x, y=y, text=y)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title='Semana', yaxis_title='PAI que ganhou', width=600, height=400)
    fig.update_traces(marker=dict(color='#20837b'))
elif period_to_display == 'diário':
    fig = px.bar(specific_dataframe, x='dia', y='pai', text='pai')
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title='Dia', yaxis_title='PAI que ganhou', width=600, height=400)
    fig.update_traces(marker=dict(color='#20837b'))

col2.plotly_chart(fig, theme=None, use_container_width=True)