# 1. Création d'une liste avec saisie utilisateur
ma_liste = []
for i in range(6):
    valeur = int(input(f"Saisir un entier n°{i+1} : "))
    ma_liste.append(valeur)

print("\nListe initiale :", ma_liste)

# 2. Supprimer une plage d’éléments (ex: les 2ème à 4ème éléments, soit index 1 à 3)
del ma_liste[1:4] 
print("wwAprès suppression des éléments d'index 1 à 3 :", ma_liste)
del ma_liste[-1]#supprime le dernier élément
print("Après suppression du dernier élément :", ma_liste)
del ma_liste[1:3]#supprime les éléments d'index 1 à 2
print("Après suppression des éléments d'index 1 à 2 :", ma_liste)
# donc ici on utilise del pour supprimer une plage d'éléments
#pour supprimer un element spécifique, on peut utiliser ma_liste.remove(valeur)
# ou ma_liste.pop(index) pour supprimer l'élément à l'index spécifié
#del ma_liste[1:3] supprime les éléments d'index 1 à 2
#ici les elements de la liste sont supprimés de l'index 1 à l'index 3 (non inclus)
#donc les 2ème, 3ème et 4ème éléments sont supprimés

# 3. Tri avec sort() : tri en place
ma_liste.sort()
print("Liste triée avec sort() :", ma_liste)

# 4. Tri avec sorted() : retourne une nouvelle liste, sans modifier l’originale
nouvelle_liste = [7, 3, 9, 1]
liste_triee = sorted(nouvelle_liste)
print("\nListe d’origine (avant sorted) :", nouvelle_liste)
print("Liste triée avec sorted() :", liste_triee)
# la difference entre sort() et sorted() est que sort() modifie la liste d'origine,
#  tandis que sorted() retourne une nouvelle liste triée.
#sort() est une méthode de liste qui trie la liste en place,
# tandis que sorted() est une fonction qui prend un itérable et retourne une nouvelle liste

# 5. Utiliser enumerate() pour afficher les index et les valeurs
print("\nIndex et éléments de la liste triée avec sorted() :")
for index, valeur in enumerate(liste_triee):
    print(f"Index {index} → Valeur {valeur}")

# 6. Affichage du type de retour de enumerate()
# et conversion en liste
print("\nType de l’objet retourné par enumerate :", type(enumerate(liste_triee)))
# Converti en liste pour visualiser les index et valeurs

e = enumerate(liste_triee)
# ici e est un objet de type enumerate qui contient les index et les valeurs de la liste triée
# on peut le convertir en liste pour voir les index et les valeurs
# # on peut aussi utiliser list() pour convertir l'objet enumerate en liste
# et afficher les index et les valeurs de la liste triée
# exemple :
# [(0, 1), (1, 3), (2, 7), (3, 9)]
L=list(enumerate(liste_triee))
print("\nType de l’objet retourné par enumerate :", type(e))
print("Converti en liste :", list(e))
print("Liste des index et valeurs (avec enumerate) :", list(enumerate(liste_triee)))
print("Liste des index et valeurs (avec list(enumerate)) :", L)
# ici l'affichage de la liste est sous forme de liste de tuples (index, valeur)
# donc [(0, 1), (1, 3), (2, 7), (3, 9)]
# ainsi on peut voir les index et les valeurs de la liste triée
# finalement, on peut utiliser enumerate pour afficher les index et les valeurs de la liste triée
# de manière plus lisible et plus concise.

#les points essentiels sont :
# 1. Création d'une liste avec saisie utilisateur.
# 2. Suppression d'une plage d'éléments avec del.
# 3. Tri de la liste avec sort() et sorted().
# 4. Utilisation de enumerate() pour afficher les index et les valeurs.
# 5. Affichage du type de retour de enumerate() et conversion en liste.
# Ceci illustre l'utilisation pratique des listes en Python pour manipuler et analyser des données.