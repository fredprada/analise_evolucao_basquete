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
    collection = connect_to_mongodb(client)
    return collection

def insert_information(collection, list_to_insert):
    try:
        collection.insert_one(list_to_insert)
        print("Inserted successfully!")
    except:
        print("Could not insert to MongoDB")