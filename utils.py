from pymongo import MongoClient

#nous permet de recuprer la bonne db 
def get_db(db_name="game_db"):
    client = MongoClient("mongodb://localhost:27017/")
    return client[db_name]

# va nous permettre d'importer toutes les col
def get_all(collection_name,db):
    collection = db[collection_name]
    return list(collection.find())
