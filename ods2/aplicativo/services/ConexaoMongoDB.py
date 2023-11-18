
import pymongo

class ConexaoDATABASE:

    def getConnection(self):
        return pymongo.MongoClient("mongodb://localhost:27017/odsdatabase")

class InsertCPF:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
         
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_pessoa_fisica']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

class InsertCNPJ:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
        
    
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_pessoa_juridica']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

class InsertAPOIO:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
        
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_apoio']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

class FindCPF:
    def __init__(self, connection):
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
        self.collection = self.db['cd_pessoa_fisica']

    def find_one(self, query):
        return self.collection.find_one(query)
 
