# Définition initiale de la liste
liste = [3, 2, 9, 5, 7, 8, 1, 6, 0]
print("Liste initiale :", liste)

# 1. Trier la liste (en place et avec copie)
# Méthode 1 : tri en place
liste.sort()
print("\n1a. Liste triée avec sort() (en place) :", liste)

# Remettre dans l'état initial pour montrer sorted()
liste = [3, 2, 9, 5, 7, 8, 1, 6, 0]
# Méthode 2 : tri avec sorted (copie)
liste_triee = sorted(liste)
print("1b. Liste triée avec sorted() (nouvelle liste) :", liste_triee)

# 2. Ajouter l'élément 4 à la liste
# Méthode 1 : append()
liste.append(4)
print("\n2a. Après ajout avec append(4) :", liste)

# Méthode 2 : insert() (par exemple à la fin)
liste.insert(len(liste), 4)
print("2b. Après ajout avec insert(len(liste), 4) :", liste)

# 3. Renverser la liste
# Méthode 1 : reverse()
liste.reverse()
print("\n3a. Liste inversée avec reverse() :", liste)

# Méthode 2 : slicing inversé
liste_inversee = liste[::-1]
print("3b. Liste inversée avec slicing [::-1] :", liste_inversee)
# donc le slicing [::-1] permet de renverser la liste en créant une nouvelle liste
# ainsi on peut renverser la liste sans modifier l'originale
# exemple de slicing inversé :
# liste = [1, 2, 3, 4, 5]
# liste_inversee = liste[::-1]

# 4. Afficher l’indice de l’élément 7
# Méthode : index()
indice_7 = liste.index(7)
print("\n4. Indice de l’élément 7 :", indice_7)
print("   Valeur à cet indice :", liste[indice_7])#affiche la valeur à l'indice 7

# 5. Enlever l’élément 8
# Méthode 1 : remove()
# remove() supprime la première occurrence de l'élément
# si l'élément n'existe pas, une exception ValueError est levée

liste.remove(8)
#donc remove(8) supprime la première occurrence de 8
# et si l'élément n'existe pas, une exception ValueError est levée
print("\n5a. Après suppression avec remove(8) :", liste)

# Méthode 2 : suppression par index avec del
# (On remet d'abord 8 à sa place pour l'exemple)
liste.insert(4, 8) #insert 8 à l'index 4
# Trouver l'index de 8
index_8 = liste.index(8) 
del liste[index_8]
# donc del liste[index] supprime l'élément à l'index spécifié
# et si l'index est hors limites, une exception IndexError est levée
print("5b. Après suppression avec del liste[index] :", liste)
# Méthode 3 : pop() (supprime et retourne l'élément exemple: pop(index))
# pop() supprime l'élément à l'index spécifié et le retourne comme valeur
# si aucun index n'est spécifié, pop() supprime et retourne le dernier élément
# donc pop() est utile pour supprimer un élément spécifique par son index
#exemple affichage de l'élément supprimé avec pop(index) (1er méthode)
index_8 = liste.index(2)  # Trouver l'index de 2
print("Index de l'élément 2 :", index_8)
# Supprimer l'élément 2 avec pop(index) et afficher l'élément supprimé
element_supprime = liste.pop(index_8)
print("5c. Après suppression avec pop(index) :", liste)
#2em méthode pour supprimer l'élément 8 avec pop(index)
# pop(index) supprime l'élément à l'index spécifié et le retourne
print("Élément supprimé :", element_supprime)
# donc pop(index) est utile pour supprimer un élément spécifique par son index
# et retourner l'élément supprimé

# (On remet d'abord 8 à sa place pour l'exemple)

liste.insert(4, 8)
element_supprime = liste.pop(index_8)
print("5c. Après suppression avec pop(index) :", liste)
print("   Élément supprimé :", element_supprime)

# donc pop() supprime l'élément à l'index spécifié et le retourne
# ou supprime le dernier élément si aucun index n'est spécifié

# 6. Afficher la sous-liste du 2e au 3e élément (indices 1 et 2)
sous_liste_2_3 = liste[1:3]
print("\n6. Sous-liste du 2e au 3e élément (index 1 à 2) :", sous_liste_2_3)

# 7. Afficher la sous-liste du début au 4e élément (index 0 à 3)
sous_liste_0_4 = liste[:4]
print("7. Sous-liste du début au 4e élément (index 0 à 3) :", sous_liste_0_4)

# 8. Afficher le dernier élément avec indice négatif
dernier = liste[-1]

print("8. Dernier élément avec indice négatif (-1) :", dernier)
print("autre méthode pour afficher le dernier élément avec indice len(liste)-1):",liste[len(liste)-1])
# 9. Afficher les 3 derniers éléments avec indices négatifs
trois_derniers = liste[-3:]
print("9. Trois derniers éléments avec indices négatifs (-3 à -1) liste[-3:] :", trois_derniers)
liste = [10, 20, 30, 40, 50,77, 60, 70, 80, 90]
print("les 3 premieres éléments avec slicing positif",liste[:3])
print("liste[-3:-1]",liste[-3:-1])
trois_premiers = liste[:-7]
print("   Trois premiers éléments avec indices négatifs (-7) :", trois_premiers)
print("   Liste inversée :", liste[::-1])
print("Liste des éléments :", liste)
# trois premiers  elements avec indices négatifs (-3 à -2) : [60, 70]
print("liste des 3 dernieres elements avec indices négatifs (-3 AAAà -2) :", liste[-3:])
#ou bien
print("liste des 3 premiers elements avec indices négatifs (-3 à -2) :", liste[ :3])
# liste des 3 premiers elements avec indices négatifs (-3 à -2) : [10, 20, 30]
print("liste des 3 premiers elements",liste[:3])
# liste des 3 premiers elements [10, 20, 30]


#les points essentiels sont :
# 1. Utilisation des méthodes de liste intégrées (sort, append, insert, reverse, index, remove, pop).
# 2. Utilisation du slicing pour accéder à des sous-listes.
# 3. Gestion des erreurs potentielles lors de la suppression d'éléments.
# Ceci illustre l'utilisation pratique des listes en Python pour manipuler et accéder aux 
# données de manière efficace.
# Définition de tuples
t1 = [1, 2, 3, 4, 2, 5]
t2 = ["a", "b", "c"]    
t3 = (True, False, True)
t4 = ()  # tuple vide
print("Tuple t1 :", t1)
# on peut retenir que un tuple est une collection ordonnée et immuable d'éléments
print("Tuple t2 :", t2) 
t6=zip(t1,t2)
print("le zip t6",t6)