import streamlit as st
from pymongo import MongoClient
import pandas as pd
import os

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "✅ Adc Novo Jogo")
st.subheader('Conta aqui como foi seu último jogo:')

###################################################################
def connect_to_mongodb():
    """
    Function to connect to mongoDB.
    """
    global collection
    client = os.getenv('CLIENT_TOKEN')
    myclient = MongoClient(client)
    db = myclient.get_database('db_evolucao_basquete')
    collection = db.collection_evolucao_basquete
    return collection

###################################################################
# Function to insert data into mongodb
def database_insertion(list_to_add):
    """
    Function to insert the information that the player have put on the forms.
    """
    connect_to_mongodb()
    st.sidebar.text('Inserção em progresso')
    collection.insert_many(list_to_add)

###################################################################
def retrieve_data_from_mongodb():
    """
    Function to get all information from mongodb.
    """
    collection = connect_to_mongodb()
    data_list = []
    data_list = [x for x in collection.find()]
    return data_list

###################################################################
def transform_to_dataframe():
    """
    Transforms the information collected from mongoDB into a dataframe to be displayed.
    """
    data_list = retrieve_data_from_mongodb()
    df_data_list = pd.DataFrame(data_list)
    return df_data_list

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
                 'Frustrado',
                 'Puto']

lista_jogadores = ['Fred',
                   'Bia']

col1, col2, col3 = st.columns(3)

with col1:
    player = st.selectbox('Jogador(a):', (lista_jogadores))
    date_of_the_game = st.date_input('Data do jogo')
    time_played = st.number_input('Tempo que jogou (min)', min_value= 0)
    pai = st.number_input('Quantos PAI você ganhou?', min_value = 0)

with col2:
    time_of_the_game = st.time_input('Hora do jogo')
    enthusiasm_before_playing = st.number_input('Qual era seu ânimo para jogar?', min_value = 0, max_value = 10)
    rating = st.number_input('Qual nota você dá pro seu jogo?', min_value = 0, max_value = 10)
    played_alone = st.radio('Você jogou sozinho?', ['sim', 'não'])

with col3:
    rest_time = st.number_input('Tempo de descanso (min)', min_value = 0)
    feeling_before_game = st.selectbox('Como você tava se sentindo antes de jogar?', (feelings_list))
    calorias = st.number_input('Quantas calorias você perdeu?', min_value = 0)
    listened_to_music = st.radio('Você ouviu música?', ['sim', 'não'])


###################################################################
# Buttons to edit information inside the database
def func_add_row(date_of_the_game,time_played,pai,played_alone,time_of_the_game,enthusiasm_before_playing,rating,listened_to_music,rest_time,feeling_before_game,calorias):
    global list_to_add
    list_to_add=[]
    dict_dia = {}
    dict_dia['jogador'] = player
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

st.write("""Atenção, ao clicar em Adicionar, as informações acima \
                irão para o banco de dados. \
                A única forma de corrigir é solicitando suporte ao responsável pelo bando de dados.""")

button_add_row = st.button('Adicionar')

if button_add_row:
    list_to_add = func_add_row(date_of_the_game,time_played,pai,played_alone,time_of_the_game,enthusiasm_before_playing,rating,listened_to_music,rest_time,feeling_before_game,calorias)
    database_insertion(list_to_add)
    st.sidebar.text('Informações inseridas no banco de dados 😉')

###################################################################
# Table that shows all information from the database
st.dataframe(transform_to_dataframe())