import json
import random

# Création d'une variable pour le nombre de kcal
def nbKcal(nbKcal, MinMax) :
    nbKcal = input(f"Combien de {MinMax} par jour souhaitez-vous ? : ")
    while not nbKcal.isdigit() :
        nbKcal = input("Veuillez renter un nombre valide ! : ")
    return(int(nbKcal))

# Implémentation d'un dictionnaire contenant les recettes
def creationDictRecettes(nomDict) :
    nom = input("Quel est le nom de la recette ? : ")
    nb = int(input("Quelle quantité de cette recette est préparée ? : "))
    kcal = int(input("Quelles sont les kcal de la recette ? : "))
    proteines = int(input("Quelle est la quantité de protéines ? : "))
    glucides = int(input("Quelle est la quantité de glucides ? : "))
    lipides = int(input("Quelle est la quantité de lipides ? : "))
    
    nomDict[nom] = {
        "nb" : nb,
        "kcal" : kcal,
        "proteines" : proteines,
        "glucides" : glucides,
        "lipides" : lipides
    }

# Création d'un fichier json pour les recettes rentrées
def ecritureJson(nomRecette, informationsRecette) :
    with open (nomRecette, 'w') as f :
        json.dump(informationsRecette, f, indent=2)
    return(nomRecette)

# Lecture du fichier json dans lequel se trouvent les recettes
def lectureJson (nomRecette) :
    with open (nomRecette, 'r') as f :
        jsonFile = json.load(f)
    return(jsonFile)

# Lecture fichier json et choix random recette
def lectureJsonRandom (nomRecette) :
    with open (nomRecette, 'r') as f :
        jsonFile = json.load(f)
    recetteRandom = random.choice(list(jsonFile.keys()))
    return(recetteRandom)
