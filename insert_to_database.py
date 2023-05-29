from pymongo import MongoClient

def call_database_insertion(list_to_add):
    # client = os.getenv('CLIENT_TOKEN')
    client = "mongodb+srv://conexao-api:dmi4zj8EuJbExh9l@personal-cluster.gdixbl3.mongodb.net/?retryWrites=true&w=majority"
    myclient = MongoClient(client)
    db = myclient.get_database('db_evolucao_basquete')
    collection = db.collection_evolucao_basquete
    # st.sidebar.text('Tentando adicionar ao banco via insert_information')
    collection.insert_many(list_to_add)
    # return "Inserção completa"  
    # st.sidebar.text(insertion)
    # return insert_information(collection, list_to_add)

# def insert_information(collection, list_to_add):
#     try:
#         collection.insert_many(list(list_to_add))
#         return "Informações inseridas corretamente"
#     except:
#         return "Informações não foram inseridas corretamente"