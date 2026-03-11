from pymongo import MongoClient

def initialisation_de_la_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    
    #pour reset les col
    db.heros.drop()
    db.monstres.drop()

    list_heros = [
        {"id" : "1", "nom": "guerrier", "ATK": "15", "DEF": "10", "PV": "100"},
        {"id" : "2", "nom": "mage", "ATK": "20", "DEF": "5", "PV": "80"},
        {"id" : "3", "nom": "archer", "ATK": "18", "DEF": "7", "PV": "90"},
        {"id" : "4", "nom": "voleur", "ATK": "22", "DEF": "8", "PV": "85"},
        {"id" : "5", "nom": "paladin", "ATK": "14", "DEF": "12", "PV": "110"},
        {"id" : "6", "nom": "sorcier", "ATK": "25", "DEF": "3", "PV": "70"},
        {"id" : "7", "nom": "chevalier", "ATK": "17", "DEF": "15", "PV": "120"},
        {"id" : "8", "nom": "moine", "ATK": "19", "DEF": "9", "PV": "95"},
        {"id" : "9", "nom": "berserker", "ATK": "23", "DEF": "6", "PV": "105"},
        {"id" : "10","nom": "chasseur", "ATK": "16", "DEF": "11", "PV": "100"}
    ]

    list_monstres=[
        {"id" : "1", "nom": "Gobelin", "ATK": "10", "DEF": "5", "PV": "50"},
        {"id" : "2", "nom": "Orc", "ATK": "20", "DEF": "8", "PV": "120"},
        {"id" : "3", "nom": "Dragon", "ATK": "35", "DEF": "20", "PV":"300"},
        {"id" : "4", "nom": "Zombies", "ATK": "12", "DEF": "6", "PV": "70"},
        {"id" : "5", "nom": "Troll", "ATK": "25", "DEF": "15", "PV": "200"},
        {"id" : "6", "nom": "Spectre", "ATK": "18", "DEF": "10", "PV": "100"},
        {"id" : "7", "nom": "Golem", "ATK": "30", "DEF": "25", "PV": "250"},
        {"id" : "8", "nom": "Vampire", "ATK": "22", "DEF": "12", "PV": "150"},
        {"id" : "9", "nom": "Loup-garou", "ATK": "28", "DEF": "18", "PV": "180"},
        {"id" : "10", "nom": "Squelette", "ATK": "15", "DEF": "7", "PV": "90"}
    ]
    db.heros.insert_many(list_heros)
    db.monstres.insert_many(list_monstres)

    print("c bon")
initialisation_de_la_db()
