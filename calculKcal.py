import json
import random

from fonctions import ecritureJson, lectureJson, lectureJsonRandom, creationDictRecettes, nbKcal

# Déclaration variables, dictionnaires, listes
informationsRepas = {}
informationsCollation = {}

listeJoursSemaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
nbJoursSemaine = 7
listeJours = []

kcalMin = 0
kcalMax = 0

# Demande du nombre de jours
nbJours = int(input("Sur combiens de jours voulez-vous générer des recettes ? : "))

# Demande jour de début
jourDebut = input("A partir de quel jour voulez-vous commencer ? : ").lower()

# Vérification si jourDebut existe
while jourDebut not in listeJoursSemaine : 
    jourDebut = input("Veuillez rentrer un jour de la semaine valide ! : ").lower()

if jourDebut == "lundi" : 
    listeJoursSemaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
elif jourDebut == "mardi" :
    listeJoursSemaine = ["mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi"]
elif jourDebut == "mercredi" : 
    listeJoursSemaine = ["mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi"] 
elif jourDebut == "jeudi" : 
    listeJoursSemaine = ["jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi", "mercredi"] 
elif jourDebut == "vendredi" : 
    listeJoursSemaine = ["vendredi", "samedi", "dimanche", "lundi", "mardi", "mercredi", "jeudi"] 
elif jourDebut == "samedi" : 
    listeJoursSemaine = ["vendredi", "samedi", "dimanche", "lundi", "mardi", "mercredi", "jeudi"]
elif jourDebut == "dimanche" : 
    listeJoursSemaine = ["samedi", "dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi"]

print(listeJoursSemaine)

# Association du nombre de jours avec les jours de la semaine
nbJoursSupp = nbJoursSemaine - nbJours
while nbJoursSupp > 0:
    del(listeJoursSemaine[-1])
    nbJoursSupp -= 1

# Demande des bornes pour les kcal à ne pas dépasser pour la journée
kcalMin = nbKcal(kcalMin, "kcal au minimum")
kcalMax = nbKcal(kcalMax, "kcal au maximum")

# Création des dictionnaires pour les repas et les collations --> fichiers JSON
while True :
    typeRecette = input("Voulez-vous enregistrer un repas (r), une collation (c) ou avez-vous fini (x) ? ")
    if typeRecette == "r" : 
        creationDictRecettes(informationsRepas)
        print(f"{informationsRepas}")
        ecritureJson("repas.json", informationsRepas)
    elif typeRecette == "c" : 
        creationDictRecettes(informationsCollation)
        print(f"{informationsCollation}")
        ecritureJson("collations.json", informationsCollation)
    else :
        break

# Lecture et importation du fichier JSON
repasJson = lectureJson("repas.json")
collationsJson = lectureJson("collations.json")

# Boucle qui vérifie si les kcal totales des recettes choisies sont dans les bornes
while nbJours > 0 :
    # Initialisation de choix aléatoire des recettes
    repasRandom1 = lectureJsonRandom("repas.json") 
    repasRandom2 = lectureJsonRandom("repas.json")

    collationRandom1 = lectureJsonRandom("collations.json")
    collationRandom2 = lectureJsonRandom("collations.json")

    kcalRepas1 = repasJson[repasRandom1]["kcal"]
    kcalRepas2 = repasJson[repasRandom2]["kcal"]
    kcalCollation1 = collationsJson[collationRandom1]["kcal"]
    kcalCollation2 = collationsJson[collationRandom2]["kcal"]

    kcalTotal = kcalRepas1 + kcalRepas2 + kcalCollation1 + kcalCollation2

    nbRepasRestant1 = repasJson[repasRandom1]["nb"]
    nbRepasRestant2 = repasJson[repasRandom2]["nb"]
    nbCollationsRestant1 = collationsJson[collationRandom1]["nb"]
    nbCollationsRestant2 = collationsJson[collationRandom2]["nb"]

    if (nbRepasRestant1 > 0) and (nbRepasRestant2 > 0) and (nbCollationsRestant1 > 0) and (nbCollationsRestant2 > 0) and (kcalMin <= kcalTotal <= kcalMax) and (repasRandom1 != repasRandom2) and (collationRandom1 != collationRandom2) :
        nbRepasRestant1 -= 1
        repasJson[repasRandom1]["nb"] = nbRepasRestant1
        nbRepasRestant2 -= 1
        repasJson[repasRandom2]["nb"] = nbRepasRestant2

        ecritureJson("repas.json", repasJson)

        nbCollationsRestant1 -= 1
        collationsJson[collationRandom1]["nb"] = nbCollationsRestant1
        nbCollationsRestant2 -= 1
        collationsJson[collationRandom2]["nb"] = nbCollationsRestant2

        ecritureJson("collations.json", collationsJson)

        proteinesTotal = repasJson[repasRandom1]["proteines"] + repasJson[repasRandom2]["proteines"]  + collationsJson[collationRandom1]["proteines"] + collationsJson[collationRandom2]["proteines"]
        glucidesTotal = repasJson[repasRandom1]["glucides"] + repasJson[repasRandom2]["glucides"]  + collationsJson[collationRandom1]["glucides"] + collationsJson[collationRandom2]["glucides"]
        lipidesTotal = repasJson[repasRandom1]["lipides"] + repasJson[repasRandom2]["lipides"]  + collationsJson[collationRandom1]["lipides"] + collationsJson[collationRandom2]["lipides"]

        print(f"{listeJoursSemaine[nbJours-1]} ({kcalTotal} kcal) :\n- repas : {repasRandom1}, {repasRandom2}\n- collation : {collationRandom1}, {collationRandom2}\nprotéines : {proteinesTotal} g -- glucides : {glucidesTotal} g -- lipides : {lipidesTotal} g\n")
        
        nbJours -= 1
