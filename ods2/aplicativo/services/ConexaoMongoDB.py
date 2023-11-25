
import pymongo

class ConexaoDATABASE:

    def getConnection(self):
        return pymongo.MongoClient("mongodb://localhost:27017/odsdatabase")

class CRUD_PessoaFisica:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
         
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_PessoaFisica']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

    def delete(self, **kwargs):
        collection = self.db['cd_PessoaFisica']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        collection.delete_one(query)
    
    def update(self, **kwargs):
        collection = self.db['cd_PessoaFisica']
        query = {}
        update_data = {}
        for key, value in kwargs.items():
            if key == "_id":
                query[key] = value
            else:
                update_data[key] = value

        collection.update_one(query, {"$set": update_data})
    
    def view(self, **kwargs):
        collection = self.db['cd_PessoaFisica']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        documents = collection.find(query)
        for document in documents:
            print(document)

class CRUD_PessoaJuridica:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
         
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_PessoaJuridica']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

    def delete(self, **kwargs):
        collection = self.db['cd_PessoaJuridica']
        query = {}
        for key, value in kwargs.items():
            query[key] = value

        collection.delete_one(query)
    
    def update(self, **kwargs):
        collection = self.db['cd_PessoaJuridica']
        query = {}
        update_data = {}
        for key, value in kwargs.items():
            if key == "_id":
                query[key] = value
            else:
                update_data[key] = value

        collection.update_one(query, {"$set": update_data})
    
    def view(self, **kwargs):
        collection = self.db['cd_PessoaJuridica']
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
        self.collectionPF = self.db['cd_PessoaFisica']
        self.collectionPJ = self.db['cd_PessoaJuridica']

    def find_one(self, query):
            return self.collectionPF.find_one(query)
    def find_one2(self, query):
            return self.collectionPJ.find_one(query)

  
    