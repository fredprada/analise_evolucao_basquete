import os
import streamlit as st
from pymongo import MongoClient
import pandas as pd
import numpy as np
import datetime


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
def database_insertion(list_to_add):
    """
    Function to insert the information that the player have put on the forms.
    """
    connect_to_mongodb()
    st.sidebar.text('Inserção em progresso')
    collection.insert_many(list_to_add)

# ###################################################################
# def database_deletion(id):
#     """
#     Function to delete a row from the database.
#     """
#     connect_to_mongodb()
#     collection.delete_one({ '_id' : f'ObjectId({id})'})

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
def data_transformation(dataframe):
    """
    Edit the columns, create new metrics and separate into new dataframes
    """
    # Transforming all empty into nan
    df_data_list = df_data_list.fillna(value=np.nan)

    # Editing the types of the columns
    df_data_list['dia'] = df_data_list['dia'].astype('datetime64[ns]')
    df_data_list['hora_do_jogo'] = pd.to_datetime(df_data_list['hora_do_jogo'],format= '%H:%M').dt.time
    df_data_list['tempo_de_descanso'] = pd.to_numeric(df_data_list['tempo_de_descanso'], errors='coerce')
    df_data_list['nota'] = pd.to_numeric(df_data_list['nota'], errors='coerce')
    df_data_list['pai'] = pd.to_numeric(df_data_list['pai'], errors='coerce')
    df_data_list['calorias'] = pd.to_numeric(df_data_list['calorias'], errors='coerce')
    df_data_list['tempo_jogado'] = pd.to_numeric(df_data_list['tempo_jogado'], errors='coerce')
    df_data_list['animo_pra_jogar'] = pd.to_numeric(df_data_list['animo_pra_jogar'], errors='coerce')

    # Creating new metric "calorias_por_min"
    df_data_list['calorias_por_min'] = df_data_list['calorias']/df_data_list['tempo_jogado']

    # Creating a new column with the week number
    df_data_list['numero_da_semana'] = df_data_list['dia'].apply(lambda x: datetime.date.isocalendar(x)[1])

    # Separating into the player's dataframes
    df_data_list_fred = df_data_list.query('jogador == "Fred"').sort_values(by='dia', ascending=False)
    df_data_list_bia = df_data_list.query('jogador == "Bia"').sort_values(by='dia', ascending=False)

    return df_data_list_fred, df_data_list_bia

###################################################################
def main_metrics(dataframe, player):
    today = datetime.datetime.now() - datetime.timedelta(hours=3)
    current_week = datetime.date.isocalendar(today)[1]

    if player == 'Fred':
        df_index = 0
    elif player == 'Bia':
        df_index = 1
    
    specific_dataframe = data_transformation(dataframe)[df_index]
    
    df_games_by_week = (pd.DataFrame(specific_dataframe['numero_da_semana'].value_counts().sort_index(ascending = False))).reset_index()
    df_games_by_week = df_games_by_week.rename(columns={'numero_da_semana':'qtd_jogos', 'index':'numero_da_semana'})
    jogos_essa_semana = df_games_by_week.query(f'numero_da_semana == {current_week}')['qtd_jogos'][0]

    return [jogos_essa_semana]
