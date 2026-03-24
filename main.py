from jeu import jouer
from historique import afficher_historique
from stats import afficher_stats

while True:
    print("\n ## SHIFUMI ## ")
    print("1. Jouer")
    print("2. Historique")
    print("3. Statistiques")
    print("4. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        jouer()
    elif choix == "2":
        afficher_historique()
    elif choix == "3":
        afficher_stats()
    elif choix == "4":
        print("Au revoir ")
        break
    else:
        print("Choix invalide")