import os
import streamlit as st
from pymongo import MongoClient
import pandas as pd

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