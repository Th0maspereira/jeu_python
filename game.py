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

    return ennemie

#on commance par verifier si l'equipe a plus de hp
def verifier_hp_equipe(teams_user):
    #on commance par calculer tout les hp des 3 perso
    total_des_pv_equipe = 0
    total_des_pv_equipe = sum(heros["PV"] for heros in teams_user)
    return total_des_pv_equipe > 0

#atk en fonction de la def
def attaque(attaquant,victime):
    calcul_des_degats = max(0, attaquant["ATK"] - victime["DEF"])


    return calcul_des_degats

#calcul de la vien en fonction des degat
'''def vie_apres_degat(victime):
    #on va calculer la vie moins le nb de degat calculer juste avant
    calcul_vie_restante = vie["PV"] - attaque


    return nouvelle_hp'''

# on passe au systeme de combat
'''def combat():
    #tant que l'equipe ne passe pas a 0 hp le combat continue 
    while verifier_hp_equipe:
    

    return fin_combat'''




#on passe au systeme de vague 
'''def vague_jeu():
    compteur_de_vague = 0
    return compteur_de_vague
    # chaque tour de boucle rajoutera un a compteur de vague'''


#on affiche le resultat
'''def resultat():
    print(f"bravo vous avec survecu {vague_jeu}")'''