# --- CRÉATION DE TUPLES ---

# Un tuple simple
from itertools import count 
#itertools est une bibliothèque standard de Python qui fournit des outils pour créer et manipuler des itérateurs.


t1 = (1, 2, 3, 4)

# Un tuple peut contenir des types différents
t2 = ("Awa", 21, 3.14, True)

# Un tuple à un seul élément DOIT avoir une virgule
t3 = (42,)  # sinon c'est un entier

# Tuple vide
t4 = ()

# Affichage
print("Tuple t1 :", t1)
print("Tuple t2 :", t2)
print("Tuple t3 :", t3)
print("Tuple vide :", t4)

# --- ACCÈS AUX ÉLÉMENTS ---

print("\nPremier élément de t1 :", t1[0])  # accès par index
print("Dernier élément de t1 :", t1[-1])  # index négatif
print("Tranche de t1 :", t1[1:3])         # slicing

# --- IMMUTABILITÉ ---

try:
    t1[0] = 100  # ERREUR ! les tuples ne sont pas modifiables
except TypeError as e:
    print("\nErreur attendue :", e)

# --- PIÈGE : Attribuer des attributs à un tuple (ce n’est pas possible) ---

t = (1, 2, 3)

try:
    t.count = 1   # faux : count est une méthode, pas un attribut qu'on peut modifier
except AttributeError as e:
    print("Erreur attendue :", e)

try:
    t.index = 2   # faux aussi, on ne peut pas fixer un index manuellement
except AttributeError as e:
    print("Erreur attendue :", e)

# --- MÉTHODES DISPONIBLES POUR LES TUPLES ---

print("\nNombre de fois que 2 apparaît dans t1 :", t1.count(2))
print("Index de la valeur 3 dans t1 :", t1.index(3))  # retourne la première position trouvée

# --- OPÉRATIONS AVEC LES TUPLES ---

# Concaténation
t5 = t1 + t2
print("\nConcaténation de t1 et t2 :", t5)

# Répétition
t6 = ("Hello",) * 3 #affiche ('Hello', 'Hello', 'Hello')
print("Tuple répété :", t6) 

# Vérification d'appartenance
print("Est-ce que 4 est dans t1 ?", 4 in t1) # Affiche True 

# on peut faire de meme avec un dictionnaire
dictionnaire = {'Awa': 21, 'Modou': 25}
print("Est-ce que 'Awa' est une clé dans le dictionnaire ?", 'Awa' in dictionnaire) # Affiche True
print("Est-ce que 'Awa' est dans t2 ?", "Awa" in t2) # Affiche True

# --- DÉBALLAGE (unpacking) ---
#l'idee est de creer des variables distinctes pour chaque élément du tuple et de les assigner aux 
# valeurs correspondantes du tuple

tuple_personne = ("Awa", 22, "Étudiante")
nom, age, statut = tuple_personne
print("\nDéballage du tuple :", nom, age, statut) # affichera : Déballage du tuple : Awa 22 Étudiante comme ceci:
# nom = "Awa", age = 22, statut = "Étudiante"

# --- TRIER UN TUPLE ---

t7 = (4, 1, 3, 2)
liste_triee = sorted(t7)  # on doit convertir car un tuple ne peut être modifié
print("Tuple trié (retourne une liste) :", liste_triee) # affichera : Tuple trié (retourne une liste) : [1, 2, 3, 4]
# On peut aussi trier en place avec une liste
liste_triee.sort()  # trie la liste en place 
print("Liste triée en place :", liste_triee) # affichera : Liste triée en place : [1, 2, 3, 4]

# Si besoin de le remettre en tuple :
t7_trie = tuple(sorted(t7))
print("Tuple trié converti :", t7_trie)

# --- BOUCLER SUR UN TUPLE AVEC ENUMERATE ---

print("\nParcours de t1 avec enumerate :")
for i, val in enumerate(t1):
    print(f"Index {i} -> Valeur {val}")

# --- LONGUEUR D’UN TUPLE ---

print("\nLongueur de t2 :", len(t2))

# --- CONVERSION LISTE → TUPLE ---

ma_liste = [10, 20, 30]
mon_tuple = tuple(ma_liste)
print("Liste convertie en tuple :", mon_tuple)

# --- CONVERSION TUPLE → LISTE ---

mon_tuple2 = (5, 6, 7)
ma_liste2 = list(mon_tuple2)
ma_liste2[0] = 100  # on peut maintenant modifier
print("Tuple converti en liste puis modifié :", ma_liste2)

# --- PIÈGE : CRÉATION D’UN TUPLE À UN SEUL ÉLÉMENT SANS VIRGULE ---

t8 = (5)
print("\nt8 sans virgule est de type :", type(t8))  # ce sera un entier

t9 = (5,)
print("t9 avec virgule est de type :", type(t9))    # ce sera un tuple
# --- PIÈGE : CRÉATION D’UN TUPLE AVEC UNE LISTE ---
ma_liste3 = [1, 2, 3]
t10 = tuple(ma_liste3)  # convertit la liste en tuple
# exemple en utilisant la compréhension de tuple
t11 = tuple(x for x in ma_liste3)  # même résultat
print("Tuple créé à partir d'une liste :", t10)
print("Tuple créé avec compréhension :", t11)
# --- PIÈGE : CRÉATION D’UN TUPLE AVEC UNE CHAÎNE DE CARACTÈRES ---
ma_chaine = "Hello"
t12 = tuple(ma_chaine)  # convertit la chaîne en tuple de caractères et l'affichage sera :
# Tuple créé à partir d'une chaîne de caractères : ('H', 'e', 'l', 'l', 'o')
print("Tuple créé à partir d'une chaîne de caractères :", t12)
#tuple et split
# Exemple de tuple avec split
ma_phrase = "Bonjour, comment ça va ?"
t13 = tuple(ma_phrase.split())  # convertit la phrase en tuple de mots
print("Tuple créé à partir d'une phrase :", t13)
# exemple de affichage
# donc on aura comme affichage : ('Bonjour,', 'comment', 'ça', 'va', '?')

# --- PIÈGE : CRÉATION D’UN TUPLE AVEC UNE CHAÎNE DE CARACTÈRES ET UN SLICING ---
ma_chaine2 = "Python"
t14 = tuple(ma_chaine2[1:4])  # convertit une tranche de la chaîne en tuple
print("Tuple créé à partir d'une tranche de chaîne :", t14)
# donc on aura comme affichage : ('y', 't', 'h')

# supprimer un element d'un tuple
# Les tuples sont immuables, donc on ne peut pas supprimer un élément directement.
# Cependant, on peut créer un nouveau tuple sans l'élément à supprimer.
#par utilsation des listes sans oublier de convertir en tuple
t15 = (1, 2, 3, 4, 5)
t15_liste = list(t15)  # Convertir en liste
t15_liste.remove(3)  # Supprimer l'élément 3
t15_sans_3 = tuple(t15_liste)  # Convertir de nouveau en tuple
print("Tuple après suppression de l'élément 3 :", t15_sans_3)


#les points essentiels sont :
# 1. Création et manipulation de tuples en Python.  
# 2. Accès aux éléments par index et slicing.
# 3. Immutabilité des tuples et implications.
# 4. Méthodes disponibles : count() et index().
# 5. Opérations courantes : concaténation, répétition, appartenance.
# 6. Déballage (unpacking) de tuples.
# 7. Conversion entre listes et tuples.
# 8. Utilisation de fonctions intégrées comme sorted() et enumerate().
# Ceci illustre l'utilisation pratique des tuples en Python pour stocker et 
# manipuler des collections de données immuables.
# De plus, les tuples sont souvent utilisés pour représenter des données structurées, 
# comme des points dans un plan, des coordonnées, etc.


# .__file__ permet d'obtenir le chemin du fichier source Python en cours d'exécution.
# .__help__ affiche la documentation intégrée d'un objet, fonction ou module.
# .__name__ donne le nom de l'objet, fonction ou module.
# .__dir__ liste les attributs et méthodes disponibles pour un objet.
# .__class__ renvoie la classe à laquelle appartient un objet. 


#'''Concaténation'''
t1 = (9,8,7,6,5)
t2 = (4,3,2,1,0)
t3 = t1 + t2
co=t1.count(5)
print("comptons 5: ",co)
print(t3) # Le résultat sera (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

'''Réplication'''
t4 = 2*t1
print(t4) # Le résultat sera (9, 8, 7, 6, 5, 9, 8, 7, 6, 5)

'''Hétérogénéité'''
t5 = (3,6,"modou",True,3.14)
print(t5) # Le résultat sera (3, 6, 'modou', True, 3.14)

'''Tuple de tuple''' # tuple de tuple est une structure de données où chaque 
# élément d'un tuple est lui-même un tuple.
t6 = ((1,2,3),(4,5,6),(7,8,9))
print(t6) # Le résultat sera ((1, 2, 3), (4, 5, 6), (7, 8, 9))

'''Accés indicé'''
print(t6[2][1]) # Le résultat sera 8 car on accède au 2ème élément du 3ème tuple

'''Accés aux tailles'''
print(len(t6)) # Le résultat sera 3
print(len(t6[2])) # Le résultat sera 3 car on accède à la taille du 3ème tuple

#donc il faut noter pour les tuple de tuples on peut accéder aux éléments
# en utilisant des indices multiples et on peut également obtenir la taille en
# utilisant la fonction len() de Python.
# utiliser des [] pour accéder aux éléments et len() pour obtenir la taille.






# 1. **Liste** → Une *liste* est une structure de données ordonnée et modifiable qui peut contenir des 
# éléments de types variés, accessibles par leurs indices.

# 2. **Tuple** → Un *tuple* est une structure de données ordonnée mais immuable, utilisée pour
#  stocker des collections d’éléments non modifiables.

# 3. **Dictionnaire** → Un *dictionnaire* est une collection non ordonnée de paires clé-valeur
#  permettant d’associer des données par correspondance unique.

# 4. **Set (ensemble)** → Un *set* est une collection non ordonnée et non indexée d’éléments uniques, 
# utilisée pour éliminer les doublons et effectuer des opérations ensemblistes.

# 5. **Fonction** → Une *fonction* est un bloc de code réutilisable qui exécute une tâche spécifique
#  et peut retourner une valeur.

# 6. **Module** → Un *module* est un fichier Python contenant du code (fonctions, classes, variables) 
# destiné à être importé et réutilisé dans d’autres programmes.

# 7. **Classe** → Une *classe* est un modèle définissant la structure et le comportement d’objets
#  partageant les mêmes attributs et méthodes.

# 8. **Variable** → Une *variable* est un espace nommé en mémoire qui stocke une valeur modifiable au 
# cours de l’exécution d’un programme.

# 9. **Polymorphisme** → Le *polymorphisme* permet à plusieurs classes différentes d’utiliser la même
#  interface (méthode ou nom de fonction) tout en ayant un comportement adapté à leur nature.

# 10. **Héritage** → L’*héritage* est un mécanisme de la POO permettant à une classe fille de réutiliser 
# et d’étendre les attributs et méthodes d’une classe parente.

# 11. **Composition (héritage par composition)** → La *composition* consiste à construire une classe à 
# partir d’instances d’autres classes, créant une relation « fait partie de » plutôt qu’une relation hiérarchique.

# 12. **Agrégation** → L’*agrégation* est une forme faible de composition où une classe contient des
#  références à d’autres objets existants sans en être responsable de leur cycle de vie.

