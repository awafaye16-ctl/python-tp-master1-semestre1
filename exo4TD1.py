# ---------------------
# 1. Comptage de la fréquence des chiffres de 0 à 9 dans une liste d'entiers
# ---------------------

L = [1233, 5678899, 78, 1009]

#AUTRE MOETHODE
ch=str(L)  # Convertit la liste L en chaîne de caractères
print("\nFréquence des chiffres de 0 à 9 dans la liste L :")
# On parcourt les chiffres de 0 à 9
for c in '0123456789':
    print(f"Chiffre {c} apparaît {ch.count(c)} fois.")
    # str(L) permet de convertir la liste en chaîne pour utiliser count() car
    # count() fonctionne sur les chaînes

# ---------------------
# Création d'un dictionnaire contenant les chiffres de 0 à 9 avec un compteur initialisé à 0
compteur = {str(i): 0 for i in range(10)}# ici str permet de convertir les chiffres en chaînes pour les utiliser comme clés 

# Parcours de la liste L
for nombre in L:
    for chiffre in str(nombre):  # Conversion de l'entier en chaîne pour accéder à chaque chiffre
                                #nombre represente chaque entier de la liste L
        compteur[chiffre] += 1   # Incrémentation du compteur du chiffre correspondant

# Affichage du résultat
print("Fréquence des chiffres de 0 à 9 :")
for chiffre in sorted(compteur.keys()):
    print(f"Chiffre {chiffre} : {compteur[chiffre]} fois")
# en gros on a defini un dictionnaire avec les chiffres de 0 à 9 comme clés
# et on a parcouru chaque entier de la liste L, converti en chaîne pour accéder à chaque chiffre
# puis on a incrémenté le compteur correspondant dans le dictionnaire

# ---------------------
# 2. Utilisation de zip() pour combiner deux listes
# ---------------------

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
combinaison = list(zip(liste1, liste2))

print("\nCombinaison des listes avec zip() :")
print("ici on combine liste1 et liste2 :", combinaison)
# zip() crée des paires (tuple) en combinant les éléments positionnels des deux listes.


# ---------------------
# 3. Transformation d'une liste en chaîne de caractères avec join()
# ---------------------

# Attention : join() fonctionne uniquement avec des chaînes de caractères
chaine = ''.join(str(x) for x in liste1)
print("\nChaîne de caractères obtenue par join() :", chaine) # affiche 12
# Ici, on utilise une compréhension de liste pour convertir chaque élément en chaîne avant de les assembler
# join() assemble les éléments de la liste en une seule chaîne sans espaces
# Exemple : join() avec des espaces
chaine_espaces = ' '.join(str(x) for x in liste1)
print("\nChaîne de caractères obtenue par join() avec des espaces :", chaine_espaces)

# ---------------------
# 4. Comptage d’occurrences d’un élément dans une chaîne
# ---------------------

# Exemple de chaîne simple
chaine_exemple = "1233213"
for chiffre in '0123456789':
    print(f"Chiffre {chiffre} apparaît {chaine_exemple.count(chiffre)} fois.")


# ---------------------
# 5. Inutile de parcourir L pour chercher les nombres dans une chaîne : la logique était erronée
# Tu essayais de compter un nombre entier (ex: 1233) dans une chaîne contenant des chiffres séparés
# Ce n’est pas pertinent. On ne retrouve pas "1233" dans "123456..."


# ---------------------
# 6. Utilisation de split() et replace() pour manipuler les chaînes
# ---------------------

# Exemple de chaîne avec des chiffres séparés par des espaces
chaine_espaces = "1 2 3 4 5 6 7 8 9 0"

# On enlève les espaces avec replace()
chaine_sans_espaces = chaine_espaces.replace(" ", "")
#OU # chaine_sans_espaces = ''.join(chaine_espaces.split())
# Affichage de la chaîne sans espaces
chaine_sans_espaces = ''.join(chaine_espaces.split())
print("\nChaîne avec espaces :", chaine_espaces)
# ici join et split() sont utilisés pour enlever les espaces
# split() divise la chaîne en une liste de sous-chaînes, et join() les réassemble sans espaces
# Affichage de la chaîne sans espaces

print("\nChaîne sans espaces avec ''.join(chaine_espaces.split()) :", chaine_sans_espaces)
print("Chaîne sans espaces join()seulement :",''.join(chaine_espaces)) #ici ca ne change rien car on n'a pas enlevé les espaces
# Puis on la transforme en liste de chiffres avec list()
liste_chiffres = list(chaine_sans_espaces)
print("Liste des chiffres :", liste_chiffres)
liste = list(set(liste_chiffres))  # On utilise set pour enlever les doublons
print("Liste sans doublons :", sorted(liste))
liste.sort()
print("Liste triée sans doublons :", liste)

# Ici, on a utilisé replace() pour enlever les espaces, list() pour convertir la chaîne en liste de caractères,
# et set() pour éliminer les doublons avant de trier la liste finale.
# ---------------------
# 7. Résumé des méthodes de chaîne de caractères utilisées
# - str(): Convertit un objet en chaîne de caractères.
# - join(): Assemble les éléments d'une liste en une seule chaîne.
# - split(): Divise une chaîne en une liste de sous-chaînes selon un séparateur.
# - replace(): Remplace des sous-chaînes par d'autres dans une chaîne.
# - count(): Compte le nombre d'occurrences d'une sous-chaîne dans une chaîne.
# Ces méthodes sont essentielles pour manipuler et analyser des données textuelles en Python.   
# ---------------------
# 8. Utilisation avancée des dictionnaires en Python
import json
dictionnaire = {
    "bonjour": "hello",
    "maison": "house",
    "chat": "cat"
}
