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
    dataframe_transf = dataframe.fillna(value=np.nan)

    # Editing the types of the columns
    dataframe_transf['dia'] = dataframe_transf['dia'].astype('datetime64[ns]')
    dataframe_transf['hora_do_jogo'] = pd.to_datetime(dataframe_transf['hora_do_jogo'], errors='coerce').dt.time
    dataframe_transf['tempo_de_descanso'] = pd.to_numeric(dataframe_transf['tempo_de_descanso'], errors='coerce')
    dataframe_transf['nota'] = pd.to_numeric(dataframe_transf['nota'], errors='coerce')
    dataframe_transf['pai'] = pd.to_numeric(dataframe_transf['pai'], errors='coerce')
    dataframe_transf['calorias'] = pd.to_numeric(dataframe_transf['calorias'], errors='coerce')
    dataframe_transf['tempo_jogado'] = pd.to_numeric(dataframe_transf['tempo_jogado'], errors='coerce')
    dataframe_transf['animo_pra_jogar'] = pd.to_numeric(dataframe_transf['animo_pra_jogar'], errors='coerce')

    # Creating new metric "calorias_por_min"
    dataframe_transf['calorias_por_min'] = dataframe_transf['calorias']/dataframe_transf['tempo_jogado']

    # Creating a new column with the week number
    dataframe_transf['numero_da_semana'] = dataframe_transf['dia'].apply(lambda x: datetime.date.isocalendar(x)[1])

    # Separating into the player's dataframe_transfs
    df_data_list_fred = dataframe_transf.query('jogador == "Fred"').sort_values(by='dia', ascending=False)
    df_data_list_bia = dataframe_transf.query('jogador == "Bia"').sort_values(by='dia', ascending=False)

    return df_data_list_fred, df_data_list_bia

###################################################################
def main_metrics(dataframe, player):
    global specific_dataframe
    today = datetime.datetime.now() - datetime.timedelta(hours=3)
    current_week = datetime.date.isocalendar(today)[1]

    if player == 'Fred':
        df_index = 0
    elif player == 'Bia':
        df_index = 1
    
    specific_dataframe = data_transformation(dataframe)[df_index]
    df_current_week = specific_dataframe[specific_dataframe['numero_da_semana'] == current_week]
    jogos_essa_semana = len(df_current_week)

    return jogos_essa_semana
