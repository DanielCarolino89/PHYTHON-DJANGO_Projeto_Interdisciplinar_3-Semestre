from pymongo import MongoClient

class MongoConnection:
# Abre a conexão com o servidor
    client = MongoClient("mongodb://localhost:27017/odsdatabase")

    # obter o banco de dados
    db = client.get_database('odsdatabase')

    #  pegue as coleções
    collection = db.get_collection('odscliente')