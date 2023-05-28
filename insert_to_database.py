from pymongo import MongoClient
import os
from streamlit_app import func_add_row

def connect_to_mongodb(client):
    global collection
    try:
        myclient = MongoClient(client)
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")

    db = myclient.get_database('db_evolucao_basquete')
    collection = db.collection_evolucao_basquete
    return collection

client = os.getenv(CLIENT_TOKEN)
collection = connect_to_mongodb(client)

list_to_insert = func_add_row()

def insert_information(collection, list_to_insert):
    collection.insert_one(list_to_insert)