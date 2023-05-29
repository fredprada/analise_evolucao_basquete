import streamlit as st
from pymongo import MongoClient
# import plotly.express as px
import os

###################################################################
# Defining page properties and title, header and subheader
st.subheader('Conta aqui como foi seu último jogo:')

###################################################################
# Inserting data into mongodb
def database_insertion(list_to_add):
    # client = os.getenv('CLIENT_TOKEN')
    client = "mongodb+srv://conexao-api:dmi4zj8EuJbExh9l@personal-cluster.gdixbl3.mongodb.net/?retryWrites=true&w=majority"
    myclient = MongoClient(client)
    db = myclient.get_database('db_evolucao_basquete')
    collection = db.collection_evolucao_basquete
    st.sidebar.text('Tentando adicionar ao banco via insert_information')
    collection.insert_many(list_to_add)

###################################################################
# Forms to collect latest game information
feelings_list = ['Radiante',
                 'Feliz',
                 'Entusiasmado',
                 'Esperançoso',
                 'Animado',
                 'Meh',
                 'Cansado',
                 'Desanimado',
                 'Triste',
                 'Frustrado']

col1, col2, col3 = st.columns(3)

with col1:
    date_of_the_game = st.date_input('Data do jogo')
    time_played = st.number_input('Tempo que jogou (min)', min_value= 0)
    pai = st.number_input('Quantos PAI você ganhou?', min_value = 0)
    played_alone = st.radio('Você jogou sozinho?', ['sim', 'não'])

with col2:
    time_of_the_game = st.time_input('Hora do jogo')
    enthusiasm_before_playing = st.number_input('Qual era seu ânimo para jogar?', min_value = 0, max_value = 10)
    rating = st.number_input('Qual nota você dá pro seu jogo?', min_value = 0, max_value = 10)
    listened_to_music = st.radio('Você ouviu música?', ['sim', 'não'])

with col3:
    rest_time = st.number_input('Tempo de descanso (min)', min_value = 0)
    feeling_before_game = st.selectbox('Como você tava se sentindo antes de jogar?', (feelings_list))
    calorias = st.number_input('Quantas calorias você perdeu?', min_value = 0)

###################################################################
# Buttons to edit information inside the database
col1, _ = st.columns(2)

def func_add_row(date_of_the_game,time_played,pai,played_alone,time_of_the_game,enthusiasm_before_playing,rating,listened_to_music,rest_time,feeling_before_game,calorias):
    global list_to_add
    list_to_add=[]
    dict_dia = {}
    dict_dia['dia'] = date_of_the_game.strftime("%Y-%m-%d")
    dict_dia['hora_do_jogo'] = time_of_the_game.strftime("%H:%M")
    dict_dia['tempo_de_descanso'] = str(rest_time)
    dict_dia['jogou_sozinho'] = str(played_alone)
    dict_dia['ouviu_musica'] = str(listened_to_music)
    dict_dia['nota'] = str(rating)
    dict_dia['pai'] = str(pai) 
    dict_dia['calorias'] = str(calorias) 
    dict_dia['tempo_jogado'] = str(time_played)
    dict_dia['animo_pra_jogar'] = str(enthusiasm_before_playing)
    dict_dia['sentimento_do_dia'] = str(feeling_before_game)
    list_to_add.append(dict_dia)
    return list(list_to_add)

with col1:
    button_add_row = st.button('Adicionar')

if button_add_row:
    list_to_add = func_add_row(date_of_the_game,time_played,pai,played_alone,time_of_the_game,enthusiasm_before_playing,rating,listened_to_music,rest_time,feeling_before_game,calorias)
    st.sidebar.text(list_to_add)
    database_insertion(list_to_add)
    st.sidebar.text('rodou o database_insertion')