import streamlit as st
# import plotly.express as px
import os
from insert_to_database import call_database_insertion

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(
    layout="wide",  
    page_title="🏀 Análise de performance")

st.header('Evolução da performance de Basquete')
st.subheader('Conta aqui como foi seu último jogo:')

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

def func_add_row():
    global list_to_add
    list_to_add=[]
    dict_dia = {}
    dict_dia['dia'] = date_of_the_game
    dict_dia['hora_do_jogo'] = time_of_the_game
    dict_dia['tempo_de_descanso'] = rest_time
    dict_dia['jogou_sozinho'] = played_alone
    dict_dia['ouviu_musica'] = listened_to_music
    dict_dia['nota'] = rating
    dict_dia['pai'] = pai 
    dict_dia['calorias'] = calorias 
    dict_dia['tempo_jogado'] = time_played
    dict_dia['animo_pra_jogar'] = enthusiasm_before_playing
    dict_dia['sentimento_do_dia'] = feeling_before_game
    list_to_add.append(dict_dia)
    return list_to_add

with col1:
    button_add_row = st.button('Adicionar')

if button_add_row:
    try:
        list_to_add = func_add_row()
        call_database_insertion(list_to_add)
        print('rodou o call_database_insertion')
        st.sidebar.text('Adicionado no banco!')
    except:
        print('erro ao rodar o call_database_insertion')
        st.sidebar.text('Erro ao adicionar no banco')

###################################################################
# Buttons to edit information inside the database




# # introdução de contexto da análise
# st.title("Análise de evolução de Basquete")
# st.header("Essa análise é focada em entender se há uma tendência entre as variáveis coletadas depois de um jogo de basquete.")
# st.write("""Gosto bastante de jogar basquete, e quero entender se há essa correlação entre as variáveis, e se estou tendo algum avanço na nota que dou para meu jogo.""")

# # apresentação de análise descritiva do dataframe
# col1, col2 = st.columns([2,3])
# col1.write(df_raw_data.describe())

# # primeiro gráfico de linha mostrando a nota pelo dia
# col2.subheader("Gráfico de Nota pelo dia do jogo")
# fig = px.line(df_raw_data.sort_values(by='dia', ascending=True), 
#                  y = 'nota', 
#                  x = 'dia',
#                  markers=True)
# fig.update_layout(
#     autosize=False,
#     width=600,
#     height=300,
#     margin=dict(
#         l=30,
#         r=30,
#         b=60,
#         t=30,
#         pad=4
#     ))
# col2.plotly_chart(fig, theme=None)
# col2.caption("Gráfico do índice 'PAI' dos dias que joguei.")
# col2.caption("PAI é o *personal activity intelligence*, da Amazfit, que dá uma nota ao exercício físico de acordo com certos critérios.")

# st.metric(label="Número de dias jogados", value=dias_jogados, delta=1)



