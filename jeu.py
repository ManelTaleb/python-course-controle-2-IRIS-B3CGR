import random
import time
import datetime

FICHIER = "data.txt"
TEMPS = "temps.txt"

def jouer():
    debut = time.time()  

    while True:
        print("\n1. Pierre  2. Feuille  3. Ciseau  0. Menu")
        choix = input("Votre choix : ")

        if choix == "0":
            break

        if choix not in ["1", "2", "3"]:
            print("Erreur")
            continue

        options = ["pierre", "feuille", "ciseau"]
        joueur = options[int(choix)-1]
        cpu = random.choice(options)

        print("CPU :", cpu)

        if joueur == cpu:
            resultat = "egalite"
        elif (joueur == "pierre" and cpu == "ciseau") or \
             (joueur == "feuille" and cpu == "pierre") or \
             (joueur == "ciseau" and cpu == "feuille"):
            resultat = "victoire"
        else:
            resultat = "defaite"

        print("Résultat :", resultat)

        date_partie = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(FICHIER, "a") as f:
            f.write(date_partie + "," + joueur + "," + cpu + "," + resultat + "\n")

        print("\n1. Rejouer  2. Menu")
        suite = input("Choix : ")
        if suite == "2":
            break

    fin = time.time()
    duree = fin - debut
    with open(TEMPS, "a") as f:
        f.write(str(duree) + "\n")