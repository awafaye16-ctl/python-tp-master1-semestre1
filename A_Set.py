# un set est une collection non ordonnée d'éléments uniques permettant des opérations ensemblistes
# les éléments d'un set doivent être immuables (nombres, chaînes, tuples immuables)
# on peut créer un set avec des accolades {} ou la fonction set() comme par exemple 
P={1,2,3}
S = set()
S.add(1)
S.add(2)
S.add(3)
print(S)  # affichera {1, 2, 3}
# On peut ajouter un élément
S.add(4)
print("Après ajout de 4 :", S)
# On peut aussi ajouter plusieurs éléments à la fois
S.update([4, 5, 6])
print("Après ajout de plusieurs éléments :", S)
# On peut supprimer un élément
S.remove(2)
print("Après suppression de 2 :", S)
# On peut aussi utiliser discard, pour supprimer sans lever d'erreur si l'élément n'existe pas
S.discard(10)  # ne fait rien, pas d'erreur
S.discard(3)  # supprime 3
print("Après discard de 10 et suppression de 3 :", S) # affichera {1, 4, 5, 6}
# On peut vider un set avec clear()
S.clear()
print("Après clear :", S) # affichera set()
# On peut vérifier l'appartenance
print("Est-ce que 3 est dans S ?", 3 in S)
# On peut faire des opérations ensemblistes
S2 = {4, 5, 6, 7}
print("Union de S et S2 :", S.union(S2))  # union affichera {4, 5, 6, 7}
#la difference entre union et intersection est que union combine les éléments des deux sets,
# tandis que intersection ne garde que les éléments communs
# On peut aussi utiliser l'opérateur |
print("Intersection de S et S2 :", S.intersection(S2))  # intersection affichera {4, 5, 6}
# On peut aussi faire la différence
print("Différence de S et S2 :", S.difference(S2))  # éléments dans S mais pas dans S2 affichera {1}
# On peut obtenir les éléments uniques d'une liste en utilisant un set
liste = [1, 2, 2, 3, 4, 4, 5]
elements_uniques = set(liste)
print("Éléments uniques de la liste :", elements_uniques)
# On peut convertir un set en liste
liste_from_set = list(S)
print("Set converti en liste :", liste_from_set)
# On peut aussi convertir une liste en set pour enlever les doublons
liste_avec_doublons = [1, 2, 2, 3, 4]
liste_sans_doublons = list(set(liste_avec_doublons))
print("Liste sans doublons :", liste_sans_doublons)
# On peut créer un set à partir d'une chaîne de caractères
chaine = "abracadabra"
set_from_string = set(chaine)
print("Set créé à partir de la chaîne :", set_from_string) # affichera {'a', 'b', 'c', 'd', 'r'}
# On peut aussi utiliser des compréhensions de set
set_comprehension = {c for c in chaine}
print("Set créé avec une compréhension :", set_comprehension)
# On peut vérifier si un set est un sous-ensemble d'un autre
print("S est-il un sous-ensemble c'est à dire < de S2 ?", S.issubset(S2))  # False
# On peut aussi vérifier si un set est un sur-ensemble d'un autre
print("S2 est-il un sur-ensemble c'est à dire > de S ?", S2.issuperset(S))  # True car S est vide
# On peut obtenir la taille d'un set
print("Taille de S :", len(S))
# On peut itérer sur les éléments d'un set
print("Élément de S :")
for element in S:
    print(element)
# On peut créer un set vide
S_vide = set()
print("Set vide :", S_vide)
# On peut vérifier si un set est vide
print("S est-il vide ?", len(S_vide) == 0)  # True
# On peut aussi utiliser la méthode clear() pour vider un set
S.clear()
print("Set S après clear :", S)  # S est maintenant vide
# On peut créer un set à partir d'une liste avec des doublons
liste_avec_doublons = [1, 2, 2, 3, 4]
liste_sans_doublons = set(liste_avec_doublons)
print("Liste sans doublons créée à partir d'un set :", liste_sans_doublons)
# On peut créer un set à partir d'une chaîne de caractères
chaine = "hello world"
set_from_string = set(chaine)
print("Set créé à partir de la chaîne :", set_from_string)
# On peut aussi utiliser des compréhensions de set
set_comprehension = {c for c in chaine}
print("Set créé avec une compréhension :", set_comprehension)



# Ici, le TDA "set" encapsule les données (éléments uniques) et fournit des opérations claires :
#  add(), remove(), union(), intersection(), etc.
# Le code utilisateur ne se soucie pas de savoir comment le set est implémenté en interne → il 
# utilise juste les méthodes.
# C’est l’avantage de l’abstraction et de la modularité des TDA.
# Exemple d'utilisation d'un set comme TDA
mon_set = set()
mon_set.add(1)
mon_set.add(2)
mon_set.add(3)
print("Mon set après ajouts :", mon_set)
mon_set.remove(2)
print("Mon set après suppression de 2 :", mon_set)
mon_set2 = {3, 4, 5}
print("Union de mon_set et mon_set2 :", mon_set.union(mon_set2))

#DONC TDA EST UNE ABSTRACTION DE DONNÉES QUI FOURNIT UNE INTERFACE CLAIRE POUR TRAVAILLER AVEC DES DONNÉES SANS SE SOUCIER DE L'IMPLEMENTATION INTERNE
# Par exemple, un set est un TDA qui encapsule une collection d'éléments uniques et fournit des opérations 
# ensemblistes.COMME ADD, REMOVE, UNION, INTERSECTION, DIFFERENCE, ETC.
# Le code utilisateur utilise simplement ces opérations sans se soucier de la façon dont le set est implémenté en interne.