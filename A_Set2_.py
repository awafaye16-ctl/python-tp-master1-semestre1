# --- CRÉATION DE SETS ---

# Un set contient des éléments non ordonnés, uniques et non mutables (pas de liste ou dict dedans)
fruits = {"pomme", "banane", "kiwi", "banane"}  # doublon "banane" supprimé
print("Set de fruits (pas de doublons) :", fruits)

# Set vide : ATTENTIOn !
vide = set()      #  C'est un set vide
not_vide = {}     #  Ceci est un dictionnaire vide !
print("Type de vide :", type(vide)) # affichera <class 'set'>
print("Type de not_vide :", type(not_vide)) # affichera <class 'dict'>
print("Type de {} :", type(not_vide))#affichera <class 'dict'>

# --- AJOUT ET SUPPRESSION ---

fruits.add("mangue")  # ajoute un élément
print("\nAprès add('mangue') :", fruits)

fruits.remove("pomme")  # supprime "pomme"
print("Après remove('pomme') :", fruits)

# remove() lève une erreur si l’élément n’existe pas → préfère discard()
fruits.discard("ananas")  # ne lève PAS d’erreur si absent
print("Après discard('ananas') :", fruits)

# --- OPÉRATIONS D'ENSEMBLE ---

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nUnion :", a.union(b))               # {1,2,3,4,5,6}
print("Intersection :", a.intersection(b))   # {3,4}
print("Différence a - b :", a.difference(b)) # {1,2}
print("Différence b - a :", b.difference(a)) # {5,6}
print("Différence symétrique :", a.symmetric_difference(b))  # {1,2,5,6}

#  Toutes ces méthodes ont aussi une version "en place" : update(), intersection_update(), etc.
print("\nMise à jour de a avec b (intersection) :", a.intersection_update(b))  # a devient {3,4}
# affichera None car intersection_update ne retourne rien
print("a après intersection_update avec b :", a)  # affichera {3,4}
#intersection_update modifie a pour ne garder que les éléments communs avec b

# --- MÉTHODES UTILES ---

print("\nLongueur :", len(a))
print("Est-ce que 3 est dans a ?", 3 in a)

# --- CONVERSION LISTE → SET POUR SUPPRIMER DOUBLONS ---

liste_avec_doublons = [1, 2, 2, 3, 3, 3]
unique = set(liste_avec_doublons)
print("\nListe sans doublons :", list(unique))  # Conversion vers liste pour l’ordre

# --- BOUCLE ET COMPRÉHENSION ---

print("\nParcours d'un set donc les valeurs sont uniques :")
for x in unique:
    print(x)

# Comprehension de set
carres = {x**2 for x in range(5)}
print("Set des carrés :", carres)

# --- FROZENSET : SET IMMUTABLE ---
# frozenset est similaire à un set mais il est immuable en effet
# On ne peut pas ajouter ou supprimer des éléments d'un frozenset
f = frozenset({1, 2, 3})# création d'un frozenset avec les éléments 1, 2, 3 et des accolades
print("\nFrozenset :", f)
# f.add(4)  # ERREUR : frozenset est immuable

# --- COPIE / COMPARAISON DE SETS ---

s1 = {1, 2, 3}
s2 = s1.copy()
s2.add(4)
print("Original :", s1)
print("Copie modifiée :", s2)

# Test d’inclusion
print("\nInclusion s1 ⊆ s2 ?", s1.issubset(s2))
print("s2 contient s1 ?", s2.issuperset(s1))
print("s1 et s2 sont disjoints ?", s1.isdisjoint(s2))#affiche False car ils ont des éléments communs

