FICHIER = "data.txt"
TEMPS = "temps.txt"

def afficher_stats():
    try:
        with open(FICHIER, "r") as f:
            lignes = f.readlines()

        if len(lignes) == 0:
            print("Aucune partie")
            return

        total = len(lignes)
        victoires = 0
        choix_total = {"pierre":0,"feuille":0,"ciseau":0}
        choix_victoires = {"pierre":0,"feuille":0,"ciseau":0}

        for ligne in lignes:
            date, joueur, cpu, resultat = ligne.strip().split(",")
            choix_total[joueur] += 1
            if resultat == "victoire":
                victoires += 1
                choix_victoires[joueur] += 1

        taux = (victoires / total) * 100
        print("\n ## Statistiques ## ")
        print("Nombre de parties :", total)
        print("Taux de victoire :", round(taux,2), "%")

        meilleure = max(choix_victoires, key=choix_victoires.get)
        print("Main la plus gagnante :", meilleure)

        print("\nTaux de victoire par main :")
        for choix in choix_total:
            if choix_total[choix] > 0:
                t = (choix_victoires[choix] / choix_total[choix]) * 100
                print(f"{choix} : {round(t,2)} %")

        with open(TEMPS, "r") as f:
            temps_total = sum(float(x.strip()) for x in f)
        print("\nTemps total joué :", round(temps_total,2),"secondes")

    except:
        print("Aucune donnée")
        input("Entrée pour revenir")