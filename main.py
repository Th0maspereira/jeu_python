from game import monstre_random
from utils import get_db,get_all


db = get_db()
#on creer le menu avec les choix
def afficher_menu():
    #afficher le titre
    print("\n ==========================="
            "\n     menu principale"
            "\n ===========================")
    # afficher les possibiliter 
    print("1. lancer le jeu")
    print("2. voir le tableau des scores")
    print("3. quiter le jeu")

# on demande au user un nombre et on le vérifie  
def choix_nb_valide(min_val, max_val):

    # boucle qui se répète jusqu'à ce que le nombre soit bon
    while True:

        # demander un choix au user
        choix_user = input("faites un choix : ")

        # vérifier si l'utilisateur a entré un nombre
        if choix_user.isdigit():

            nombre = int(choix_user)

            # vérifier si le nombre est égal ou entre les bornes
            if min_val <= nombre <= max_val:

                # si tout est bon on retourne la valeur
                return nombre

            else:
                # si la valeur est invalide
                print(f"choix invalide. entrez un nombre entre {min_val} et {max_val}")
        print ("veuillez entre un nombre")

afficher_menu()

#on demande au joueur de creer un nom valide 
def choix_nom_valide():
    # boucle qui se répète jusqu'a ce que le nom soit bon
    while True:
        #demander le nom
        nom_user =  input("entrez votre pseudo : ")
        # verification des normes
        if len(nom_user) > 0 and len(nom_user) < 21:
            # on enregistre le nom
            return nom_user
        else:
                #si le nom est invalide
                print("le nom n'est pas valide")
# on affiche la list des perso pour la premiere fois
def db_heros():
    heros = get_all("heros", db)

    print("voici la liste des heros diponible")

    for perso in heros:
        print(f"numero: {perso["id"]} Nom: {perso["nom"]} ATK: {perso["ATK"]} DEF: {perso["DEF"]} PV: {perso["PV"]}")

    return heros
# on permet au user de choisir 
def choisir_mon_equipe(heros_libres):
    #on creer la liste de c perso choisi
    teams_user = []

    #on veut faire une boucle qui repete le joueur dispo 3 
    while len(teams_user) < 3:
        heros_trouve = False
        # on veut que la liste ce reaffiche une fois les heros choisis sont retirer
        if len(teams_user) > 0:
            for libre in heros_libres:
                print(f"numero: {libre["id"]} Nom: {libre["nom"]} ATK: {libre["ATK"]} DEF: {libre["DEF"]} PV: {libre["PV"]}")
        #on veut que le user puisse choisir son equipe avec un nb valide
        id_choisi =  choix_nb_valide(1,10)
            
        #on creer une fonction pour que le heros passe de la table heros a la team
        for perso in heros_libres:
            if int(perso["id"]) == id_choisi:
                teams_user.append(perso)
                heros_libres.remove(perso)
                print(f"le heros {perso["nom"]} fais officiellement partie de ton equipe")
                heros_trouve = True
                break
            
        if not heros_trouve:
             print("ce heros a deja ete selectionner prend en un autre")
    return teams_user

#on veut afficher l'equipe 
def afficher_l_equipe(equipe):
    print("\n ================================"
          "\n     ta team est composé de"
            "\n ================================")
    for team in equipe:
        print(f"{team["nom"]} ATK: {team["ATK"]} DEF: {team["DEF"]} PV: {team["PV"]}")



#on recupere le choix valide
choix = choix_nb_valide(1,3)

#on execute le choix valider du user en fonction de ce qu'il a choisi
def lancer_choix(choix):
    #lancer le jeu
    if choix == 1:
        print("lancement du jeu")
        #on dois recuperer et afficher un nom valide
        nom_du_joueur = choix_nom_valide()

        print(f"bienvenue {nom_du_joueur} le jeu va commencer")
        # on veut afficher la liste des heros
        liste_de_tous_les_heros = db_heros()
        #affichage de l'equipe finaliser
        equipe_user_finaliser = choisir_mon_equipe(liste_de_tous_les_heros)
        afficher_l_equipe(equipe_user_finaliser)
        #on veut afficher le monstre contre qui le joueur va devoir jouer
        ennemie = monstre_random(db)

    #voir le leaderboard
    elif choix == 2:
        print("voici le tableau des score")
    #quiter le jeu
    elif choix == 3: 
        print("fermeture du programme")
        exit()
lancer_choix(choix)

afficher_menu()