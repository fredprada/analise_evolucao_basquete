from pymongo import MongoClient

def connect_to_mongodb(client):
    global collection
    myclient = MongoClient(client)
    print("Connected successfully!!!")
    db = myclient.get_database('db_evolucao_basquete')
    collection = db.collection_evolucao_basquete
    return collection

def insert_information(collection, list_to_insert):
    try:
        collection.insert_many(list(list_to_insert))
        return "Informações inseridas corretamente"
    except:
        return "Informações não foram inseridas corretamente"