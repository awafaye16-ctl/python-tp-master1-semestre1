A=[]
for i in range(4):
    C=int(input("saisir un nombre: "))
    A.append(C)
# Affichage des éléments de la liste A
print("Les nombres saisis sont:")
for k in range (len(A)):
    print(f"{k}: {A[k]}")
#ou bien enumerate qui affiche index +valeur
for i, value in enumerate(A):
    print(f"{i}: {value}")
#additionner tous les elemets de la liste A
somme = 0
for i in range(len(A)):
    somme += A[i]
print(f"La somme des nombres saisis est: {somme}")
#ou bien
somme = sum(A)
print(f"La somme des nombres saisis est: {somme}")
#une nouvelle liste B qui contient les cube des éléments de A

B = []
for i in range(len(A)):
    B.append(A[i] ** 3)
    
#ou bien par compréhension de liste
B = [x ** 3 for x in A]
# Affichage des éléments de la liste B
print("Les cubes des nombres saisis sont:", B)
# Affichage des éléments de la liste A qui sont multiples de 3
print("Les nombres de A qui sont multiples de 3:")
for i in range(len(A)):
    if A[i] % 3 == 0:
        print(A[i])
#ou bien par compréhension de liste
multiples_de_3 = [x for x in A if x % 3 == 0]
print("Les nombres de A qui sont multiples de 3:", multiples_de_3)
# ou bien avec filter
#filter est une fonction qui prend en argument une fonction et un itérable
# et qui renvoie un itérable contenant les éléments pour lesquels la fonction retourne True
#sous forme de liste
#filter est souvent utilisé avec une fonction lambda
multiples_de_3 = list(filter(lambda x: x % 3 == 0, A))
print("Les nombres de A qui sont multiples de 3:", multiples_de_3)  
# Affichage des éléments de la liste A qui sont pairs
print("Les nombres de A qui sont pairs:")   
for i in range(len(A)):
    if A[i] % 2 == 0:
        print(A[i])
# ou bien par compréhension de liste
pairs = [x for x in A if x % 2 == 0]    
print("Les nombres de A qui sont pairs:", pairs)
# une nuvelle liste C qui contient les éléments de A qui sont pairs elvevés au cube
C = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        C.append(A[i] ** 3)
# ou bien par compréhension de liste
C = [x ** 3 for x in A if x % 2 == 0]
# Affichage des éléments de la liste C  
print("Les cubes des nombres de A qui sont pairs:", C)
# Affichage des éléments de la liste A qui sont impairs
# Affichage du maximum et du minimum de la liste A
entier_max = max(A)
entier_min = min(A)
print("Le nombre maximum de A est:", entier_max)
print("Le nombre minimum de A est:", entier_min)
# ou bien
entier_max = sorted(A)[-1] #ici on utilise sorted pour faire le tri des éléments de A et le -1 permet de recupérer
#le maximum de A car sorted(A) renvoie une liste triée 
# et [-1] renvoie le dernier élément de cette liste
print("le dernier element de A est:", entier_max)
# donc sorted(A) renvoie une liste triée
# et sorted(A)[-1] renvoie le dernier élément de cette liste triée

entier_min = sorted(A)[0]
# donc sorted(A)[0] renvoie le premier élément de cette liste triée
print("Le nombre maximum de A est:", entier_max)
print("Le nombre minimum de A est:", entier_min)
# ou bien
entier_max = A[0]
entier_min = A[0]
for i in range(1, len(A)):
    if A[i] > entier_max:
        entier_max = A[i]
    if A[i] < entier_min:
        entier_min = A[i]
print("Le nombre maximum de A est:", entier_max)
print("Le nombre minimum de A est:", entier_min)
#compter le nombre d'éléments de A impairs
compteur_impairs = 0
for i in range(len(A)):
    if A[i] % 2 != 0:
        compteur_impairs += 1
# somme des éléments de A qui sont impairs
somme_impairs = 0
for i in range(len(A)):
    if A[i] % 2 != 0:
        somme_impairs += A[i]
print("La somme des éléments de A qui sont impairs est:", somme_impairs)
# ou bien par compréhension de liste
compteur_impairs = sum(1 for x in A if x % 2 != 0)
print("Le nombre d'éléments de A qui sont impairs est:", compteur_impairs)
# ou bien par compréhension de liste
compteur_impairs = len([x for x in A if x % 2 != 0])
print("Le nombre d'éléments de A qui sont impairs est:", compteur_impairs)
# ou bien avec filter   
compteur_impairs = len(list(filter(lambda x: x % 2 != 0, A)))
print("la somme des éléments de A qui sont impairs est:", sum(filter(lambda x: x % 2 != 0, A)))
# ou bien avec version plus concise
compteur_impairs = sum(x for x in A if x % 2 != 0)
print("Le nombre d'éléments de A qui sont impairs est:", compteur_impairs)


# Ici, on a utilisé des listes, des boucles, des conditions, des fonctions intégrées (sum, max, min, sorted, 
# filter) et des compréhensions de liste pour manipuler et analyser les données.
# Les points clés sont :
# 1. Création et affichage de listes.
# 2. Calcul de la somme, du maximum et du minimum.
# 3. Gestion des erreurs potentielles lors de la suppression d'éléments.
# 4. Filtrage des éléments selon des critères spécifiques (multiples de 3, pairs, impairs).
# 5. Utilisation de compréhensions de liste pour des opérations concises.   
# Ceci illustre l'utilisation pratique des listes en Python pour manipuler et analyser des données numériques.
#tuple et conversion
# Création d'un tuple
mon_tuple = (1, 2, 3, 4, 5)
print("Mon tuple :", mon_tuple)