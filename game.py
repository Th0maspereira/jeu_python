import random
from utils import get_all

#on va devoir prendre aleatoirement un monstre de la table
def monstre_random(db):

    # on commance par recuperer la liste des monstre
    liste_des_monstres = get_all("monstres", db)

    #on genere un monstre aleatoirement 
    ennemie = random.choice(liste_des_monstres)

    #on affiche le monstre random
    print(f"vous aller affrontr le boss Nom: {ennemie["nom"]} ATK: {ennemie["ATK"]} DEF: {ennemie["DEF"]} PV: {ennemie["PV"]}")
    
    #on le recupere pour le reutiliser
    return ennemie