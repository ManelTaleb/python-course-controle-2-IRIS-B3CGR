FICHIER = "data.txt"

def afficher_historique():
    print("\n ## Historique ## ")

    try:
        with open(FICHIER, "r") as f:
            lignes = f.readlines()

        if len(lignes) == 0:
            print("Aucune partie")
            return

        page = 0
        taille = 5  

        while True:
            debut = page * taille
            fin = debut + taille

            print("\nDATE                 | JOUEUR  | CPU     | RESULTAT")
            print("-"*50)

            for ligne in lignes[debut:fin]:
                date, joueur, cpu, resultat = ligne.strip().split(",")
                print(f"{date} | {joueur:^7} | {cpu:^7} | {resultat:^8}")

            print("\n1. Suivant  2. Précédent  0. Menu")
            choix = input("Choix : ")

            if choix == "1" and fin < len(lignes):
                page += 1
            elif choix == "2" and page > 0:
                page -= 1
            elif choix == "0":
                return

    except:
        print("Aucune donnée")
        input("Entrée pour revenir")
