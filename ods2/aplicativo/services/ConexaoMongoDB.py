
from datetime import datetime
import pymongo

class ConexaoDATABASE:

    def getConnection(self):
        return pymongo.MongoClient("mongodb://localhost:27017/odsdatabase")

class CRUD_PessoaCadastro:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
         
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_PessoaCadastro']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

    def delete(self, **kwargs):
        collection = self.db['cd_PessoaCadastro']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        collection.delete_one(query)
    
    def update(self, **kwargs):
        collection = self.db['cd_PessoaCadastro']
        query = {}
        update_data = {}
        for key, value in kwargs.items():
            if key == "_id":
                query[key] = value
            else:
                update_data[key] = value

        collection.update_one(query, {"$set": update_data})
    
    def view(self, **kwargs):
        collection = self.db['cd_PessoaCadastro']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        documents = collection.find(query)
        for document in documents:
            print(document)

class CRUD_PessoaApoio:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
         
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_PessoaApoio']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

    def delete(self, **kwargs):
        collection = self.db['cd_PessoaApoio']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        collection.delete_one(query)
    
    def update(self, **kwargs):
        collection = self.db['cd_PessoaApoio']
        query = {}
        update_data = {}
        for key, value in kwargs.items():
            if key == "_id":
                query[key] = value
            else:
                update_data[key] = value

        collection.update_one(query, {"$set": update_data})
    
    def view(self, **kwargs):
        collection = self.db['cd_PessoaApoio']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        documents = collection.find(query)
        for document in documents:
            print(document)
 
class CRUD_ItemsDoacao:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
         
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_ItemsDoacao']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

    def delete(self, **kwargs):
        collection = self.db['cd_ItemsDoacao']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        collection.delete_one(query)
    
    def update(self, **kwargs):
        collection = self.db['cd_ItemsDoacao']
        query = {}
        update_data = {}
        for key, value in kwargs.items():
            if key == "_id":
                query[key] = value
            else:
                update_data[key] = value

        collection.update_one(query, {"$set": update_data})
    
    def view(self, **kwargs):
        collection = self.db['cd_ItemsDoacao']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        documents = collection.find(query)
        for document in documents:
            print(document)
            
class Find_Login:
    def __init__(self, connection):
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
        self.collectionPF = self.db['cd_PessoaCadastro']

    def find_one(self, query):
            return self.collectionPF.find_one(query)

class Consultas:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']

    def Total_doacoes(self):
    collection = self.db['cd_ItemsDoacao']

    pipeline = [
        {
            '$group': {
                '_id': None,
                'totalDoacoes': {'$sum': 1}
            }
        }
    ]

    result = next(collection.aggregate(pipeline), None)
    total_doacoes = result['totalDoacoes'] if result else 0

    return total_doacoes

def doacoes_por_item(self, item):
    collection = self.db['cd_ItemsDoacao']

    pipeline = [
        {
            '$match': {'item': item}
        },
        {
            '$group': {
                '_id': None,
                'doacoesItem': {'$sum': 1}
            }
        }
    ]

    result = next(collection.aggregate(pipeline), None)
    doacoes_item = result['doacoesItem'] if result else 0

    return doacoes_item

def quantidade_total_por_item(self, item):
        collection = self.db['cd_ItemsDoacao']
        cursor = collection.aggregate([
            {
                '$match': {'item': item}  
            },
            {
                '$group': {
                    '_id': {'item': '$item'},  
                    'totalQuantidade': {
                        '$sum': {
                            '$convert': {
                                'input': '$quantidade',
                                'to': 'int',
                                'onError': 0,
                                'onNull': 0
                            }
                        }
                    }
                }
            }
        ])
        result = next(cursor, None)
        return result['totalQuantidade'] if result else 0


def porcentagem_total_doacoes(self):
    collection = self.db['cd_ItemsDoacao']

    pipeline = [
        {
            '$group': {
                '_id': None,
                'totalDoacoes': {'$sum': 1}
            }
        }
    ]

    result = next(collection.aggregate(pipeline), None)
    total_doacoes = result['totalDoacoes'] if result else 0

    porcentagem_doacoes = total_doacoes * 0.10 if total_doacoes > 0 else 0


    
