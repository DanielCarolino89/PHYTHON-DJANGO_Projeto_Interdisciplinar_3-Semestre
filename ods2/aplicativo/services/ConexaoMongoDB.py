
import pymongo

class ConexaoDATABASE:

    def getConnection(self):
        return pymongo.MongoClient("mongodb://localhost:27017/odsdatabase")

class ConexaoCPF:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
        
    
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_pessoa_fisica']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

class ConexaoCNPJ:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
        
    
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_pessoa_juridica']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 

class ConexaoAPOIO:
    def __init__(self,connection) -> None:
        self.client = connection.getConnection()
        self.db = self.client['odsdatabase']
        
    
    def insert(self, **kwargs):
        data = {}
        collection = self.db['cd_apoio']
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data) 
 
