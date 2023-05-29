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
        return print("Informações inseridas corretamente")
    except:
        return print("Informações não foram inseridas corretamente")

def call_database_insertion(list_to_add):
    # client = os.getenv('CLIENT_TOKEN')
    client = "mongodb+srv://conexao-api:dmi4zj8EuJbExh9l@personal-cluster.gdixbl3.mongodb.net/?retryWrites=true&w=majority"
    collection = connect_to_mongodb(client)
    # st.sidebar.text('Tentando adicionar ao banco via insert_information')
    insert_information(collection, list_to_add)
    # st.sidebar.text(insertion)