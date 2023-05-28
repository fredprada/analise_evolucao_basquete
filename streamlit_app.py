###################################################################
import streamlit as st
import plotly.express as px
import os

###################################################################
# Defining page properties
st.set_page_config(
    layout="wide",  
    page_title="🏀 Análise de performance")

###################################################################
# Forms to collect latest game information
st.title('Conta aqui como foi seu último jogo:')

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
    time_played = st.time_input('Tempo que jogou (min)')

    pai = st.number_input('Quantos PAI você ganhou?', 
                            min_value = 0)
    played_alone = st.radio('Você jogou sozinho?',
                            ['sim', 'não'])
with col2:
    time_of_the_game = st.time_input('Hora do jogo')
    mood_before_playing = st.number_input('Qual era seu ânimo para jogar?', 
                                        min_value = 0, 
                                        max_value = 10)
    rating = st.number_input('Qual nota você dá pro seu jogo?',
                            min_value = 0, 
                            max_value = 10)
    listened_to_music = st.radio('Você ouviu música?',
                             ['sim', 'não'])

with col3:
    rest_time = st.time_input('Tempo de descanso (min)')
    feeling_before_game = st.selectbox('Como você tava se sentindo antes de jogar?',
                                       (feelings_list))
    calorias = st.number_input('Quantas calorias você perdeu?', 
                                min_value = 0)

###################################################################
col1, col2 = st.columns(2)

with col1:
    button_add_row = st.button('Adicionar')

with col2:
    button_remove_row = st.button('Remover última entrada')

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



