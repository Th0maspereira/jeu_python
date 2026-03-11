from utils import get_db,get_all
def main():

    db = get_db()
    #on creer le menu avec les choix
    def afficher_menu():
        #afficher le titre
        print("\n ===========================" \
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
    
    def db_heros():
        heros = get_all("heros", db)

        print("voici la liste des heros diponible")

        for perso in heros:
            print(f"numero: {perso["id"]} Nom: {perso["nom"]} ATK: {perso["ATK"]} DEF: {perso["DEF"]} PV: {perso["PV"]}")

        return heros


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
            print_les_heros = db_heros()
            #on veut que le user puisse choisir son equipe avec un nb valide
            
 
        #voir le leaderboard
        elif choix == 2:
            print("voici le tableau des score")
        #quiter le jeu
        elif choix == 3: 
            print("fermeture du programme")
            exit()
    lancer_choix(choix)

main()