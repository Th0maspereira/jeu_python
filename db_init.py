# initialistion de la db
from utils import get_db, get_all

db = get_db()


monstres = get_all("monstres", db)
for m in monstres:
    print(m)

perso = db["perso"].find_one({"_id": 3})
print(perso)
