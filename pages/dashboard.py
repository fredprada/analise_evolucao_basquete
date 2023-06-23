import streamlit as st
# import plotly.express as px
from functions import transform_to_dataframe, main_metrics, data_transformation

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard")
page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


players_list = ['Bia',
                'Fred']
player = st.selectbox('Jogador(a):', (players_list))

col1, col2 = st.columns(2)

df_all_info = transform_to_dataframe()
data_transformation(df_all_info)

main_metrics_list = main_metrics(df_all_info, player)
dias_jogados = len(df_all_info['dia'].value_counts())
jogos_essa_semana = main_metrics(df_all_info, player)

st.header(f'Oi {player}!')
st.subheader('Dá uma olhadinha aqui nas suas estatísticas')
st.metric(label="Número de dias jogados", value=dias_jogados, delta=1)

st.metric(label='jogos essa semana: ', value = jogos_essa_semana)