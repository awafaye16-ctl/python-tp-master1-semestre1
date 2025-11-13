
celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

# Créer un dictionnaire vide pour stocker les fréquences
frequences = {}

# Parcourir chaque élément de la liste
for objet in celestial_objects:
    if objet in frequences:
        frequences[objet] += 1  # Si le mot existe déjà, on incrémente
    else:
        frequences[objet] = 1   # Sinon, on l’ajoute avec 1
print("methode 1 :affichage",frequences)


#autres methodes avec count
# for objet in celestial_objects:
#     frequences[objet] = frequences.get(objet, 0) + 1  # Utilisation de get pour simplifier l'incrémentation
# Utilisation de get() pour obtenir la valeur actuelle ou 0 si l'objet n'existe pas
# donc on utilise get() pour obtenir la valeur actuelle ou 0 si l'objet n'existe pas
# et on incrémente la valeur de 1 pour chaque occurrence de l'objet



# Affichage final du dictionnaire

# donc le dictionnaire final contient les fréquences de chaque mot
# {'Moon': 2, 'Gas': 1, 'Asteroid': 3, 'Dwarf': 1}
# ainsi on peut compter les occurrences de chaque mot dans la liste

#par comprehension
frequences_comp = {objet: celestial_objects.count(objet) for objet in set(celestial_objects)}
# Affichage du dictionnaire par compréhension
print("par comprehension",frequences_comp)
# ici on utilise une compréhension de dictionnaire pour compter les occurrences de chaque mot
# dans la liste celestial_objects
# et on utilise set(celestial_objects) pour ne pas compter les doublons
# donc le dictionnaire final contient les fréquences de chaque mot


#donc les points essentiels sont :
# 1. Initialisation d’un dictionnaire vide pour stocker les fréquences.
# 2. Parcours de chaque élément de la liste pour mettre à jour le compteur.
# 3. Utilisation d'une compréhension de dictionnaire pour simplifier le comptage.
# Ceci illustre l’utilisation pratique des dictionnaires en Python pour compter les occurrences d’éléments dans une liste.
