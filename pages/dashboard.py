import streamlit as st
import plotly.express as px
from functions import transform_to_dataframe, main_metrics, get_numeric_stats

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard")#, layout="wide")

lista_players = ['Bia','Fred']
player = st.selectbox('Jogador(a):', lista_players)

###################################################################
# Defining metrics
df_all_info = transform_to_dataframe()
dict_metricas = main_metrics(df_all_info, player)
dict_numeric_stats = get_numeric_stats(df_all_info, player)

jogos_essa_semana = dict_metricas['jogos_essa_semana']
jogos_semana_passada = dict_metricas['jogos_semana_passada']
jogos_por_semana = dict_metricas['jogos_por_semana']

###################################################################
# Title and subheader
st.header(f'Oi {player}!')
st.subheader('Dá uma olhadinha aqui nas suas estatísticas 😉')

st.text(dict_numeric_stats)

###################################################################
# Current and last week numeric metrics
col1, col2, col3, col4 = st.columns(4)
col1.subheader('Total')
col2.metric(label="🗓️ Jogos", value = dict_metricas['qtd_de_jogos'])
col3.metric(label='⌚ Minutos jogados', value = dict_numeric_stats['specific_dataframe']['tempo_jogado']['tempo_jogado_soma'])
col4.metric(label='🔥 Calorias gastas', value = dict_numeric_stats['specific_dataframe']['calorias']['calorias_soma'])

col1, col2, col3, col4 = st.columns(4)
col1.subheader('Essa semana (vs semana passada)')
col2.metric(label='🗓️ Jogos', 
            value = dict_metricas['jogos_essa_semana'], 
            delta = dict_metricas['jogos_essa_semana'] - dict_metricas['jogos_semana_passada'])
col3.metric(label='⌚ Minutos jogados', 
            value = dict_numeric_stats['specific_dataframe']['tempo_jogado']['tempo_jogado_soma_essa_semana'],
            delta = dict_numeric_stats['specific_dataframe']['tempo_jogado']['tempo_jogado_soma_essa_semana'] - dict_numeric_stats['specific_dataframe']['tempo_jogado']['tempo_jogado_soma_semana_passada'])
col4.metric(label='🔥 Calorias gastas', 
            value = dict_numeric_stats['specific_dataframe']['calorias']['calorias_soma_essa_semana'],
            delta = dict_numeric_stats['specific_dataframe']['calorias']['calorias_soma_essa_semana'] - dict_numeric_stats['specific_dataframe']['calorias']['calorias_soma_semana_passada'])

###################################################################
# Plotting games per week
fig = px.bar(
    jogos_por_semana,
    x="numero_da_semana",
    y="qtd",
    text="qtd")
fig.update_traces(textposition="outside")
fig.update_layout(xaxis_title="Número da semana", yaxis_title="Dias que jogou", yaxis_range=[0, 7], width=300)
st.plotly_chart(fig, theme=None, use_container_width=True)