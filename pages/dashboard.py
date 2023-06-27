import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from functions import transform_to_dataframe, main_metrics, get_numeric_stats, create_calendar_image

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
period_in_time = st.selectbox('',['esta semana vs semana passada', 'esta semana', 'semana passada'])
col1, col2, col3, col4, col5 = st.columns(5)

dict_tempo_jogado = dict_numeric_stats['specific_dataframe']['tempo_jogado']
dict_calorias = dict_numeric_stats['specific_dataframe']['calorias']
dict_nota = dict_numeric_stats['specific_dataframe']['nota']
dict_pai = dict_numeric_stats['specific_dataframe']['pai']

col1.metric(label="🏀 Jogos", 
            value = dict_metricas['qtd_de_jogos'])
col2.metric(label='⌚ Minutos jogados', 
            value = dict_tempo_jogado['tempo_jogado_soma'])
col3.metric(label='🔥 Calorias gastas', 
            value = dict_calorias['calorias_soma'])
col4.metric(label='👍 Nota média', 
            value = dict_nota['nota_media'])
col5.metric(label='🥇 PAI', 
            value = dict_pai['pai_soma'])

col1, col2, col3, col4, col5 = st.columns(5)
if period_in_time == 'esta semana':
    # col1.text(period_in_time)
    col1.metric(label=f"""🏀 ({period_in_time})""", 
                value = dict_metricas['jogos_essa_semana'])
    col2.metric(label=f"""⌚ ({period_in_time})""", 
                value = dict_tempo_jogado['tempo_jogado_soma_essa_semana'])
    col3.metric(label=f"""🔥 ({period_in_time})""", 
                value = dict_calorias['calorias_soma_essa_semana'])
    col4.metric(label=f"""👍 ({period_in_time})""", 
                value = dict_nota['nota_media_essa_semana'])
    col5.metric(label=f"""🥇 ({period_in_time})""",
                value = dict_pai['pai_soma_essa_semana'])
elif  period_in_time == 'semana passada':
    # col1.text(period_in_time)
    col1.metric(label=f"""🏀 ({period_in_time})""", 
                value = dict_metricas['jogos_semana_passada'])
    col2.metric(label=f"""⌚ ({period_in_time})""", 
                value = dict_tempo_jogado['tempo_jogado_soma_semana_passada'])
    col3.metric(label=f"""🔥 ({period_in_time})""", 
                value = dict_calorias['calorias_soma_semana_passada'])
    col4.metric(label=f"""👍 ({period_in_time})""", 
                value = dict_nota['nota_media_semana_passada'])
    col5.metric(label=f"""🥇 ({period_in_time})""",
                value = dict_pai['pai_soma_semana_passada'])
elif  period_in_time == 'esta semana vs semana passada':
    # col1.text(period_in_time)
    col1.metric(label=f"""🏀 ({period_in_time})""", 
                value = dict_metricas['jogos_essa_semana'], 
                delta = dict_metricas['jogos_essa_semana'] - dict_metricas['jogos_semana_passada'])
    col2.metric(label=f"""⌚ ({period_in_time})""", 
                value = dict_tempo_jogado['tempo_jogado_soma_essa_semana'],
                delta = dict_tempo_jogado['tempo_jogado_soma_essa_semana'] - dict_tempo_jogado['tempo_jogado_soma_semana_passada'])
    col3.metric(label=f"""🔥 ({period_in_time})""", 
                value = dict_calorias['calorias_soma_essa_semana'],
                delta = dict_calorias['calorias_soma_essa_semana'] - dict_calorias['calorias_soma_semana_passada'])
    col4.metric(label=f"""👍 ({period_in_time})""",
                value = dict_nota['nota_media_essa_semana'],
                delta = dict_nota['nota_media_essa_semana'] - dict_nota['nota_media_semana_passada'])
    col5.metric(label=f"""🥇 ({period_in_time})""",
                value = dict_pai['pai_soma_essa_semana'],
                delta = dict_pai['pai_soma_essa_semana'] - dict_pai['pai_soma_semana_passada'])

######################################################################################################################################
# Plotting a calendar with the days I played at leats one time

# Example player activities (replace with your own data)
import datetime
player_activities = [
    datetime.date(2023, 6, 5),
    datetime.date(2023, 6, 10),
    datetime.date(2023, 6, 15),
    datetime.date(2023, 6, 20),
]

# Create the calendar image for the current month
calendar_image = create_calendar_image(player_activities)

# Show the image in Streamlit
st.image(calendar_image)

######################################################################################################################################
# Plotting games per week
fig = px.bar(
    jogos_por_semana,
    x="numero_da_semana",
    y="qtd",
    text="qtd")
fig.update_traces(textposition="outside")
fig.update_layout(xaxis_title="Número da semana", yaxis_title="Dias que jogou", yaxis_range=[0, 7], width=300)
st.plotly_chart(fig, theme=None, use_container_width=True)