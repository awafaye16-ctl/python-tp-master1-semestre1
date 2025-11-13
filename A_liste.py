# --- CRÉATION DE LISTES ---
# une liste est une collection ordonnée et modifiable d'éléments
# Les listes peuvent contenir des éléments de types différents (entiers, chaînes, etc.)
# un tuple est une collection ordonnée et immuable d'éléments
# un set est une collection non ordonnée d'éléments uniques
# un dictionnaire est une collection non ordonnée de paires clé-valeur
# Liste de nombres
nombres = [1, 2, 3, 4]


# Liste de types différents
melange = ["Awa", 21, 3.14, True]

# Liste vide
liste_vide = []

# Affichage des listes
print("Liste de nombres :", nombres)
print("Liste de types mixtes :", melange)
print("Liste vide :", liste_vide)

# --- ACCÈS AUX ÉLÉMENTS ---

print("\nPremier élément :", nombres[0])
print("Dernier élément :", nombres[-1])
print("Slicing (éléments 1 à 2) :", nombres[1:3])
print("Slicing (jusqu'à l'avant-dernier) :", nombres[:-1])
print("Slicing (tous les éléments) :", nombres[:])
print("Slicing (éléments avec pas de 2) :", nombres[::2])  # tous les 2 éléments exemple daffichage : [1, 3]
print("Slicing (éléments de 1 à 3) :", nombres[1:3])  # de l'index 1 à 2
print("Slicing (éléments de 1 à 3 avec pas de 2) :", nombres[1:3:2])  # de l'index 1 à 2 avec un pas de 2
print("Slicing (inversé) :", nombres[::-1])  # liste inversée
print("Slicing (inversé avec pas de 2) :", nombres[::-2])  # tous les 2 éléments en partant de la fin


# --- MODIFICATION D'ÉLÉMENTS (les listes sont mutables !) ---

nombres[0] = 100
print("Liste après modification :", nombres) # affichera [100, 2, 3, 4]

# --- MÉTHODES IMPORTANTES ---

nombres.append(5)  # Ajoute à la fin
print("\nAprès append(5) :", nombres)

nombres.insert(1, 99)  # Insère à l'indice 1
print("Après insert(1, 99) :", nombres)

nombres.extend([6, 7])  # Ajoute plusieurs éléments
print("Après extend([6,7]) :", nombres) # affichera [100, 99, 2, 3, 4, 5, 6, 7]

nombres.remove(99)  # Supprime la première occurrence de 99 de la liste
print("Après remove(99) :", nombres)

dernier = nombres.pop()  # Supprime et retourne le dernier élément
print("Après pop() :", nombres, "| Élément supprimé :", dernier)
# --- SUPPRESSION un element avec pop() ---
nombres.pop(0)  # Supprime l'élément à l'indice 0
print("Après pop(0) :", nombres)  # affichera [2, 3, 4, 5, 6, 7]


# --- EFFACER UNE PARTIE DE LA LISTE AVEC SLICING ---

del nombres[1:3]  # supprime les éléments d'index 1 à 2 inclus
print("Après del[1:3] :", nombres)

# ---- TRI ----

liste_a_trier = [5, 3, 8, 1]
liste_a_trier.sort()  # trie sur place
print("\nListe triée avec sort() :", liste_a_trier)


# --- TRI AVEC sorted() ---
# sorted() retourne une nouvelle liste triée sans modifier l'originale
l=sorted(liste_a_trier)  # retourne une nouvelle liste triée
print("Liste triée avec sorted() :", l)

# Remettons une nouvelle version désordonnée
liste_non_ordonnee = [5, 3, 8, 1]
sorted_liste = sorted(liste_non_ordonnee)  # retourne une nouvelle liste triée
print("Liste triée avec sorted() :", sorted_liste)
print("Liste d'origine reste intacte :", liste_non_ordonnee)

# --- COPIE DE LISTE : piège à éviter ! ---

# Ne pas faire ça : alias de la liste originale car les listes sont mutables
# Mauvaise méthode : copie par référence
nombres = [2, 3, 4, 5, 6, 7]
copie_fausse = nombres
copie_fausse[0] = 999
print("\nAttention : modification affecte les deux :", nombres, copie_fausse)#affichage sera :
# Original : [2, 3, 4, 5, 6, 7]
# Copie indépendante : [999, 3, 4, 5, 6, 7]

# Bonne méthode : utiliser copy()
nombres = [1, 2, 3]
copie_correcte = nombres.copy()
copie_correcte[0] = 100
print("Original :", nombres)
print("Copie indépendante :", copie_correcte)

# --- UTILISATION DE ENUMERATE ---

print("\nParcours avec enumerate() :")
for i, val in enumerate(nombres):
    print(f"Index {i} → Valeur {val}")
# donc enumerate() permet d'obtenir l'index et la valeur en même temps
# l'affichage sera :
# Index 0 → Valeur 1
# Index 1 → Valeur 2
# Index 2 → Valeur 3


# --- COMPRÉHENSION DE LISTE ---

carres = [x**2 for x in range(5)]
print("\nCarrés de 0 à 4 :", carres) # affichera [0, 1, 4, 9, 16]

# Liste des pairs seulement
pairs = [x for x in range(10) if x % 2 == 0]
print("Nombres pairs de 0 à 9 :", pairs)

# --- FONCTIONS UTILES ---

print("\nTaille de la liste :", len(nombres))
print("Somme :", sum(nombres))
print("Minimum :", min(nombres))
print("Maximum :", max(nombres))

# --- TRANSFORMATION EN CHAÎNE DE CARACTÈRES ---

fruits = ["pomme", "banane", "mangue"]
chaine = " ".join(fruits)
print("\nListe transformée en chaîne :", chaine)# affichera :
# Liste transformée en chaîne : pomme banane mangue

# --- LISTE INVERSEE ---

inverse = list(reversed(nombres)) #ou inverse = nombres[::-1]
print("\nListe originale :", nombres) 
print("Liste inversée :", inverse)

# --- CONVERSION LISTE ↔ TUPLE ---

liste_origine = [1, 2, 3]
tuple_converti = tuple(liste_origine)
print("Liste convertie en tuple :", tuple_converti)# affichera :
# Liste convertie en tuple : (1, 2, 3)

# --- MÉTHODES MOINS FRÉQUENTES ---

fruits.clear()  # Vide la liste
print("\nListe fruits après clear() :", fruits)# affichera :
# Liste fruits après clear() : []

# --- zip() : combiner plusieurs listes élément par élément ---

noms = ["Awa", "Moussa", "Fatou"]
notes = [18, 15, 19]

for nom, note in zip(noms, notes):
    print(f"{nom} a eu {note}/20")# affichera :
# Awa a eu 18/20

# zip retourne un objet qu'on peut convertir en liste de tuples
z= list(zip(noms, notes))
print("\nRésultat du zip combiné :", z) #l'affichage sera :
# Résultat du zip combiné : [('Awa', 18), ('Moussa', 15), ('Fatou', 19)]

#laffichage sera :
# [('Awa', 18), ('Moussa', 15), ('Fatou', 19)]


# --- enumerate() : accès aux index et aux valeurs dans une boucle ---

print("\nAvec enumerate() :")
for i, val in enumerate(noms):
    print(f"Index {i} → Élément {val}")

# --- format() : personnaliser des chaînes (remplace les f-strings si besoin) ---

nom = "Awa"
note = 18
message = "L'étudiante {} a obtenu {} sur 20.".format(nom, note)
print("\nUsage de format() :", message)
# --- format() : personnaliser des chaînes de caractères ---
# Exemple d'utilisation de format() pour formater une chaîne
#affichage sera :
# L'étudiante Awa a obtenu 18 sur 20.


# on peut aussi utiliser des indices ou noms
message2 = "L'étudiante {0} a eu la note de {1}".format(nom, note)
print("Format avec indices :", message2)
#affichage sera :
# L'étudiante Awa a eu la note de 18

#on peut aussi utiliser .format() pour les decimal
# Exemple d'utilisation de format() pour formater un nombre décimal
print("\nFormatage d'un nombre décimal :")
nombre_decimal = 3.14159
message_decimal = "La valeur de pi est {:.2f}".format(nombre_decimal)
print(message_decimal)
#ou bien avec f-string
print(f"La valeur de pi est {nombre_decimal:.2f}")

# --- split() : découper une chaîne en liste de mots ---

texte = "Python est un langage puissant"
mots = texte.split()  # par défaut coupe sur les espaces
print("\nListe des mots :", mots) # affichera :
# Liste des mots : ['Python', 'est', 'un', 'langage', 'puissant']

# --- strip() : enlever les espaces (ou caractères) autour d'une chaîne ---

salutation = "   Bonjour Awa!   "
print("Avant strip:", repr(salutation))#repr ici permet de voir les espaces
# affichera : Avant strip: '   Bonjour Awa!   ' sans le repr on aurait pas vu les espaces
# On enlève les espaces en début et fin de chaîne
print("Après strip:", repr(salutation.strip()))  # enlève les espaces en début/fin

# On peut aussi enlever des caractères spécifiques : avec lstrip() et rstrip()
print("Enlève 'A' au début :", salutation.lstrip("A"))# affichera :# Enlève 'A' au début :   Bonjour Awa!
print("Enlève '!' à la fin :", "salutation!".rstrip("!"))# affichera : Enlève '!' à la fin :   Bonjour Awa!
print("Enlève 'B' au début :", "Bonjour".lstrip("B"))# affichera : Enlève 'B' au début : onjour

# --- str() : conversion en chaîne (utile avant un join par exemple) ---

valeurs = [1, 2, 3]
chaine = "-".join([str(x) for x in valeurs]) #l'utilisation de str() permet de convertir les entiers en chaînes
# On utilise join pour créer une chaîne avec des tirets et l'affichage sera : 1-2-3
print("\nJoin avec str() :", chaine)

# --- indexation négative et slicing avancé ---

liste = ['a', 'b', 'c', 'd', 'e', 'f']
print("\nDernier élément (index négatif) :", liste[-1])#l'affichage sera : Dernier élément (index négatif) : f
print("Derniers 3 éléments :", liste[-3:]) #l'affichage sera : Derniers 3 éléments : ['d', 'e', 'f']
print("3 premiers élément :", liste[ :-3])          # l'affichage sera : Premier élément : ['a', 'b', 'c']
print("les éléments :", liste[-1:-3:-1])  # l'affichage sera : les éléments : ['f', 'e', 'd']
print("les éléments :", liste[-1:-3:-2])  # l'affichage sera : les éléments : ['f', 'd']
print("Un élément sur deux :", liste[1::2])     # l'affichage sera : Un élément sur deux : ['b', 'd', 'f'] 
print("Un élément sur deux :", liste[::2])     ##l'affichage sera : Un élément sur deux : ['a', 'c', 'e']
print("Liste inversée :", liste[::-1])         # l'affichage sera : Liste inversée : ['f', 'e', 'd', 'c', 'b', 'a']

# --- frozenset() : version IMMUTABLE d’un set (utile pour clés de dictionnaire, par exemple) ---

s = frozenset([1, 2, 3, 2])
print("\nFrozenset :", s)# affichera : Frozenset : frozenset({1, 2, 3}) l'object frozenset est
#c'est similaire à un set mais il est immuable en effet
# On ne peut pas ajouter ou supprimer des éléments d'un frozenset
# s.add(4)  # ERREUR : on ne peut pas modifier un frozenset

# --- Erreur volontaire : accéder à un index inexistant ---

try:
    print("\nAccès hors-limite :", liste[100])  # ERREUR
except IndexError as e:
    print("Erreur capturée :", e)

# --- .index() : obtenir la position d'un élément ---

print("Position de 'c' dans la liste :", liste.index('c'))

# Si l’élément n’existe pas, cela lève une erreur :
try:
    print(liste.index('z'))  # ERREUR si absent
except ValueError as e:
    print("Erreur index() :", e)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#Définir une chaine
s1 = "Hello les étudiants du MSDA"
print(s1) # Resultat retrouné : Hello les étudiants du MSDA
#Longueur
long = len(s1)
print(long) # Resultat retrouné : 27 car compte le 
#Accés indicé
s2 = s1[:7]
print(s2) # Resultat retrouné : Hello l
#Non modifiable on peut pas faire s1[0]='h'
#Mais on peut faire une transformation en liste
#s1[5]='-' #erreur car les chaines sont immutables 
s1 = s1[:5] + '-' + s1[6:]
s = s1.upper()
print(s) # Resultat retrouné : HELLO LES ETUDIANTS DU MSDA
#Recherche d'une sous chaine
ok = s.find("EL")
print(ok) # Resultat retrouné : 1
#Nombre d'occurence
cpt = s.count("E")
print(cpt) # Resultat retrouné : 2
#Remplacement d'occurence
rp = s.replace("MSDA","Master en Science des Données et Applications")
print(rp) # Resultat retrouné : HELLO LES ENFANTS DU Master en Science des Données et Applications


#154Python, UIDT / SES / MSDA / M. BOUS
#Définir une chaine
s1 = "Nitou Thies"
#Transformation de chaine en liste
liste = list(s1)
print(liste) #['N', 'i', 't', 'o', 'u', ' ', 'T', 'h', 'i', 'e', 's']
#afficher la liste du 1er au 4ere element
print(liste[0:4]) # ['N', 'i', 't', 'o']

#oubien
print(liste[:4])
#Découpage par séparateur

#le dernnier element est elemt avec indice negatif -1
print("le dernier elemt avec indice negatif ",liste[-1]) # s
decoupe = s1.split(" ")
print(decoupe) # ['Nitou', 'Thies’]
#Former une chaine à partir d'une liste
ok = "/".join(decoupe)
print(ok) # Nitou/Thies
