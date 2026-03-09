from pymongo import MongoClient

# connexion à MongoDB
def get_db(db_name="game_db"):
    client = MongoClient("mongodb://localhost:27017/")
    return client[db_name]


def get_all(collection_name, db):
    collection = db [collection_name]
    return list(collection.find())
