# Etant donné une liste de chaines de caractéres séparées par des espaces, construire une seule
# liste constituée de tous les mots apparaissant de maniére unique:
# lines = [ 'grape banana mango',
# 'nut orange peach',
# 'apple nut banana apple mango' ]
# fruits = ['grape', 'nut', 'orange', 'peach', 'apple', 'banana', 'mango']


# Liste de phrases contenant des mots de fruits
lines = [
    'grape banana mango',           # ligne 1
    'nut orange peach',             # ligne 2
    'apple nut banana apple mango'  # ligne 3 (avec des doublons : "nut", "apple", "banana", "mango")
]

# Liste des fruits valides à considérer
fruits = ['grape', 'nut', 'orange', 'peach', 'apple', 'banana', 'mango']

# Étape 1 : Initialiser un ensemble (set) pour stocker des mots uniques
unique_words = set()

# Étape 2 : Parcourir chaque ligne de texte dans lines
for line in lines:
    mots = line.split()  # transforme la ligne en liste de mots, ex: "grape banana mango" → ["grape", "banana", "mango"]

    # Pour chaque mot dans la ligne découpée
    for mot in mots:
                             # mots est une liste de mots dans la ligne courante comme ["grape", "banana", "mango"]
        if mot in fruits:  # Vérifie si le mot est bien un fruit connu
            unique_words.add(mot)  # Ajoute le mot à l'ensemble (pas de doublon dans un set)

# Étape 3 : Convertir le set en liste pour pouvoir le trier ou l'afficher
resultat = list(unique_words)

# Affichage des mots uniques non triés (ordre arbitraire car set)
print("Liste des mots uniques présents dans lines :", resultat)

# Trier la liste par ordre alphabétique croissant (A → Z) par defaut cest par ordre croissant
resultat_trie = sorted(resultat, reverse=False)
print("Liste des mots uniques triés :", resultat_trie)

# Afficher le nombre de mots uniques trouvés
print("Nombre de mots uniques :", len(resultat_trie))

# Affichage de la liste triée en ordre inverse (Z → A)
print("Liste des mots uniques triés en ordre inverse [::-1] :", resultat_trie[::-1])  # méthode slicing
print("Liste des mots uniques triés en ordre inverse :", sorted(resultat_trie, reverse=True))  # méthode sorted 
# affiche la liste triée en ordre inverse (Z → A)

# Tri spécial : trier selon l'ordre alphabétique inversé de chaque mot (utile pour des cas spécifiques)
print("Liste des mots uniques triés par mot inversé :", sorted(resultat_trie, key=lambda x: x[::-1]))
# Exemple de tri selon la longueur des mots (du plus court au plus long)
print("Liste des mots uniques triés par longueur :", sorted(resultat_trie, key=len))
# Exemple de tri selon la longueur des mots (du plus long au plus court)
print("Liste des mots uniques triés par longueur (inverse) :", sorted(resultat_trie, key=len, reverse=True))


#donc les points essentiels sont :
# 1. Utilisation d'un set pour stocker des mots uniques (élimination des doublons).
# 2. Parcours de chaque ligne et découpage en mots avec split().
# 3. Filtrage des mots pour ne garder que ceux présents dans la liste des fruits.
# 4. Conversion de l'ensemble en liste pour le tri et l'affichage.
# 5. Utilisation de sorted() et de différentes clés de tri pour afficher les résultats selon divers critères.
# Ceci illustre l'utilisation pratique des sets et des listes en Python pour manipuler et analyser 
# des données textuelles.