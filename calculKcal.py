import csv

informationsRepas = {}
informationsCollation = {}
kacl = input("Combien de kcal par jour souhaitez-vous ? : ")
while True :
    typeRecette = input("Voulez-vous enregistrer un repas (r), une collation (c) ou avez-vous fini (x) ? ")
    if typeRecette == "r" : 
        nomRepas = input("Quel est le nom du repas ? : ")
        nbRepas = input("Quelle quantité de ce repas est préparée ? : ")
        kcalRepas = input("Quelles sont les kcal du repas ? : ")
        proteines = input("Quelle est la quantité de protéines ? : ")
        glucides = input("Quelle est la quantité de glucides ? : ")
        lipides = input("Quelle est la quantité de lipides ? : ")
        
        informationsRepas[nomRepas] = {
            "nomRepas" : nomRepas,
            "nbRepas" : nbRepas,
            "kcalRepas" : kcalRepas,
            "proteines" : proteines,
            "glucides" : glucides,
            "lipides" : lipides,
        }
        
        print(f"{informationsRepas}")
        
    elif typeRecette == "c" :
        nomCollation = input("Quel est le nom de la collation ? : ")
        nbCollation = input("Quelle quantité de cette collation est préparée ? : ")
        kcalCollation = input("Quelles sont les kcal de la collation ? : ")
        proteines = input("Quelle est la quantité de protéines ? : ")
        glucides = input("Quelle est la quantité de glucides ? : ")
        lipides = input("Quelle est la quantité de lipides ? : ")
    
        informationsCollation[nomCollation] = {
            "nbCollation" : nbCollation,
            "kcalCollation" : kcalCollation,
            "proteines" : proteines,
            "glucides" : glucides,
            "lipides" : lipides,
        }
        
        print(f"{informationsCollation}") 
        
    else :
        break

with open ('calculKcal.csv', 'w') as calculKcal:
    informations = csv.writer(calculKcal)
    informations.writerow(['nom', 'nombre', 'kcal', 'proteines', 'glucides', 'lipides'])
    for nomRepas, info in informationsRepas.items() :
        informations.writerow([nomRepas, info["nbRepas"], info["kcalRepas"], info["proteines"], info["glucides"], info["lipides"]])
    for nomCollation, info in informationsCollation.items() :
        informations.writerow([nomCollation, info["nbCollation"], info["kcalCollation"], info["proteines"], info["glucides"], info["lipides"]])

