#import A_liste
#print("la fonction dir ",dir(A_liste))
#print("la fonction help",help(A_liste))


#  Un programme principal saisit une chaîne d'ADN valide et une
# séquence d'ADN valide (valide signifie qu'elles ne sont pas vides et
# sont formées exclusivement d'une combinaison arbitraire
# de "a", "t", "g" ou "c").
#  Écrire une fonction valide qui renvoie True si la saisie est valide,
# False sinon.


#  Écrire une fonction saisie qui effectue une saisie valide et renvoie
# la valeur saisie sous forme d'une chaîne de caractères.

# def saisie():
#     while True:
#         valeur = input("Entrez une valeur : ").strip()  # on supprime les espaces autour
#         if valeur:  # si la chaîne n’est pas vide
#             return valeur
#         else:
#             print("❌ Saisie invalide ! Veuillez entrer une valeur non vide.")
# n = saisie()
# print("Vous avez saisi :", n, "de type", type(n))

#   strip permet de supprimer les espaces avant et après la saisie

#  Écrire une fonction proportion qui reçoit deux arguments, la
# chaîne et la séquence et qui retourne la proportion de séquence
# dans la chaîne (c'est-à-dire son nombre d'occurrences).
#  Le programme principal appelle la fonction saisie pour la chaîne et
# pour la séquence et affiche le résultat.
#  Utiliser la fonction count des string


#  Ecrire un algorithme python qui permet de determiner si une chaine de caractére
# est un palindrome
def est_palindrome(chaine):
    # On compare la chaîne avec son inverse
    return chaine == chaine[::-1]

# Test de la fonction
chaine_test = "radarwe"
print("La chaîne est un palindrome :", est_palindrome(chaine_test))

#  Ecrire de deux maniéres une fonction qui accepte n’importe quel nombre de
# nombres et retourne les données suivantes: moyenne, min, max, somme:
#  Une qui utilise les fonctions built-in de python
#  Une autre qui ecrit les codes necessaires

def statistiques_builtin(*nombres):
    moyenne = sum(nombres) / len(nombres) if nombres else 0
    minimum = min(nombres) if nombres else None
    maximum = max(nombres) if nombres else None
    somme = sum(nombres)
    return moyenne, minimum, maximum, somme

def statistiques_manuel(*nombres):
    if not nombres:
        return 0, None, None, 0

    # Calculs manuels
    somme = 0
    minimum = nombres[0]
    maximum = nombres[0]
    for n in nombres:
        somme += n
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    moyenne = somme / len(nombres)
    return moyenne, minimum, maximum, somme

#test des fonctions
nombres_test = [10, 5, 8, 20, 15]
print("Statistiques avec built-in :", statistiques_builtin(*nombres_test))
print("Statistiques avec manuel :", statistiques_manuel(*nombres_test))



# crire un module nommé "perimetre" qui implémente les périmètres des figures suivantes :
# • Rectangle = (long + larg) * 2
# • Carré = cote * 4
# • Cercle = 2 * pi * rayon

def perimetre_rectangle(longueur, largeur):
    return 2 * (longueur + largeur)

def perimetre_carre(cote):
    return 4 * cote
import math

def perimetre_cercle(rayon):
    return 2 * math.pi * rayon

# Tester les fonctions
print("Périmètre du rectangle (5, 10) :", perimetre_rectangle(5, 10))
print("Périmètre du carré (4) :", perimetre_carre(4))
print("Périmètre du cercle (3) :", perimetre_cercle(3))     




#  Créez un fichier appelé my_simple_math.py avec deux fonctions : mult(a, b),
# add(a, b), qui divisent et additionnent les deux nombres respectivement.
#  Ajoutez deux autres fonctions appelées test_mult et test_add qui testeront les deux
# fonctions ci-dessus en utilisant assert.
#  Ajoutez du code qui exécutera les tests si quelqu'un exécute python
# my_simple_math.py exécutant le fichier comme s'il s'agissait d'un script.
#  Créez un autre fichier appelé use_my_simple_math.py qui utilisera les fonctions du
# module my_simple_math pour calculer 2 + 5 * 7
#  Assurez-vous que lorsque vous exécutez python use_my_simple_math.py, les tests
# ne s'exécuteront pas.

# 147Python, UIDT / SES / MSDA / M. BOUSSO - M. DIOUF
# '''Concaténation'''
# t1 = (9,8,7,6,5)
# t2 = (4,3,2,1,0)
# t3 = t1 + t2
# print(t3) # Le résultat sera (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
# '''Réplication'''
# t4 = 2*t1
# print(t4) # Le résultat sera (9, 8, 7, 6, 5, 9, 8, 7, 6, 5)
# '''Hétérogénéité'''
# t5 = (3,6,"modou",True,3.14)
# print(t5) # Le résultat sera (3, 6, 'modou', True, 3.14)
# '''Tuple de tuple'''
# t6 = ((1,2,3),(4,5,6),(7,8,9))
# print(t6) # Le résultat sera ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# '''Accés indicé'''
# print(t6[2][1]) # Le résultat sera 8
# '''Accés aux tailles'''
# print(len(t6)) # Le résultat sera 3
# print(len(t6[2])) # Le résultat sera 3



# Ecrire un programme en Python qui demande à l’utilisateur de saisir une liste
# d’entiers puis à l’aide d’un parcours itératif effectue les actions suivantes :
# 1. Afficher la liste
# 2. Afficher la liste en colonne de manière à afficher l’index et son contenu
# 3. Additionner tous les éléments de la liste
# 4. Créer une nouvelle liste qui sera le multiple (3) de tous les éléments de la liste
# 5. Obtenir le plus grand entier de la liste
# 6. Obtenir le plus petit entier de la liste
# 7. Compter le nombre des entiers pairs présents dans la liste
# 8. Calculer la somme de tous les nombres impairs de la liste



# 1. Supprimer une plage d’elements d’une liste en utilisant le slicing
# 2. Tri de list:
#  Utliser sort pour trier une liste
#  Utiliser sorted pour trier une liste
#  Quelle difference notez-vous entre les deux ?
# 1. Utiliser la fonction enumerate avec une liste. Regarder son type de retour