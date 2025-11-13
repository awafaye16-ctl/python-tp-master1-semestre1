
import math
print(dir(math))
#pour avoir des precisons sur une fonction
print(math.pi)  # Affiche la valeur de pi
print(math.sqrt(16))  # Affiche la racine carrée de 16
print(math.factorial(5))  # Affiche 5! (factorielle de 5)
print(math.pow(2, 3))  # Affiche 2^3 (2 à la puissance 3)
print(math.sin(math.pi / 2))  # Affiche le sinus de pi/2
print(help(math.cos))  # Affiche l'aide sur la fonction cos
#la difference entre random uniform et randint
import random
print(random.randint(1, 10))  # Retourne un entier aléatoire entre 1 et 10 inclus
print(random.uniform(1, 10))  # Retourne un flottant aléatoire entre 1 et 10
print(random.choice(['apple', 'banana', 'cherry']))  # Retourne un élément aléatoire d'une liste
print(random.sample([1, 2, 3, 4, 5], 3))  # Retourne une liste de 3 éléments uniques choisis 
# aléatoirement dans la liste
print(random.shuffle([1, 2, 3, 4, 5]))  # Mélange la liste en place
print(random.random())  # Retourne un flottant aléatoire entre 0.0 et 1.0
print(dir(random))  # Affiche les fonctions disponibles dans le module random

import numpy as np
print(np.array([1, 2, 3]))  # Crée un tableau NumPy à partir d'une liste
print(np.arange(0, 10, 2))  # Crée un tableau NumPy avec des valeurs de 0 à 10 (exclu) avec un pas de 2
#numpy est une bibliothèque puissante pour le calcul numérique en Python
# Elle permet de manipuler des tableaux multidimensionnels et de réaliser des opérations mathématiques sur un ensemble de données.


from scipy.integrate import quad 
print("Calcul de l'intégrale d'une fonction simple")
# Intégrale de x^2 entre 0 et 1
#ici on utilise la fonction quad de scipy pour calculer l'intégrale
#quad prend en paramètre la fonction à intégrer, les bornes inférieure et supérieure
# et retourne le résultat de l'intégrale ainsi qu'une estimation de l'erreur
# de l'intégration
resultat, erreur = quad(lambda x: x**2, 0, 1)
print("Résultat :", resultat)
print("Erreur estimée :", erreur)

# Calcul de l'intégrale de f(x) entre 0 et 1
# Ici, nous allons intégrer la fonction f(x) = x^3 entre 0 et 1

f = lambda x: x**3
resultat, erreur = quad(f, 0, 1)

print("Résultat :", resultat)
print("Erreur estimée :", erreur)

# Manipulations de tableaux
# 1.13.1 Tableaux de nombres numpy
b = np.array([[8,3,2,4],[5,1,6,0],[9,7,4,1]]) 
print(type(b)) # numpy.ndarray ici b est un tableau numpy
print("affichons le tableau",b) # tableau de taille (3,4) differents de matrices
# car il n'y a pas de type de données fixe alors que les matrices ont un type de données fixe exemple: int, float, etc.
print("affichons le type de données avec dtype",b.dtype) # datatype: int dt
#difference entre type et dtype est que type est une fonction python qui retourne le type d'un objet
# alors que dtype est un attribut de l'objet numpy.ndarray qui retourne le type de données du tableau
print("affichons la forme du tableau avec b.shape",b.shape) # (3,4)
c = np.array([[8,2],[5,6],[9,7]], dtype=complex)# ici on crée un tableau de nombres complexes pour montrer 
#que numpy permet de créer des tableaux de nombres complexes
print("affichons le type de données avec dtype",c.dtype) # datatype: complex
print("affichons un élément du tableau",c[0,0]) # 8+0j
#More than 2 dimensions:
d = np.array([[[8,3],[1,2]],
              [[5,1],[4,5]],
              [[9,7],[4,5]]])
d.shape # (3, 2, 2) #shape permet de connaître la taille de chaque dimension du tableau
#ici on a un tableau de 3 dimensions, avec 3 tableaux de 2 lignes et 2 colonnes
# On peut accéder à un élément du tableau en utilisant des indices pour chaque dimension
#exemple d[0,1,1] accède au élément de la première dimension, deuxième ligne, deuxième colonne
#ici on a 3 tableaux de 2 lignes et 2 colonnes
print("affichons le tableau :",d) # tableau de taille (3,2,2)
print("affichons le type de données avec dtype :",d.dtype) # datatype: int

print("affichons la forme du tableau avec d.shape :",d.shape) # (3, 2, 2)
print("affichons un élément du tableau :",d[0,0,0]) # 8
#Reshaping: permet de changer la forme du tableau sans changer les données
x = d.reshape(4,3) # tableau de taille (4,3) comme ceci 
#d= [[8,3,1],
#   [2,5,1],
#   [4,9,7],
#   [4,5]] ici on a sur cette ligne 2
# ici on a un tableau de 4 lignes et 3 colonnes
print("affichons le tableau reshaped :",x) # tableau de taille (4,3)
print("affichons la forme du tableau reshaped avec x.shape :",x.shape) # (4, 3)
print("affichons le type de données avec x.dtype :",x.dtype) # datatype: int
# On peut aussi utiliser reshape pour créer des tableaux unidimensionnels
d = np.arange(12) # crée un tableau de 0 à 11
print("affichons le tableau d :",d) # tableau de taille (12,)
d.reshape(12,1) # tableau de taille (12,1) ici on a un tableau de 12 lignes et 1 colonne
print("affichons le tableau reshaped avec d.reshape(12,1) :",d.reshape(12,1)) # tableau de taille (12,1)
print("affichons le type de données avec d.dtype :",d.dtype) # datatype: int
d.reshape(12,) # tableau unidimensionel de taille 12 ici on a un tableau de 12 éléments avec une
# seule dimension cest a une dimension constitue d'une seule ligne
np.insert(np.arange(4,9),3,17) # 4,5,6,17,7,8 # insère 17 à l'index 3 du tableau [4,5,6,7,8]
# comme ceci [4,5,6,17,7,8]
# On peut aussi utiliser insert pour insérer des éléments dans un tableau multidimensionnel
np.insert(np.array([[1, 2], [3, 4]]), 1, 5, axis=0) # insère 5 à l'index 1 de l'axe 0 (lignes)
# ici on a un tableau de 2 lignes et 2 colonnes, on insère 5 à la deuxième ligne
# ce qui donne [[1, 2], [5, 5], [3, 4]]
print("affichons le tableau après insert :",np.insert(np.array([[1, 2], [3, 4]]), 1, 5, axis=0)) # [[1, 2], [5, 5], [3, 4]]
# On peut aussi utiliser insert pour insérer des éléments dans un tableau multidimensionnel
print("affichons le tableau après insert :",np.insert(np.array([[1, 2], [3, 4]]), 1, 5, axis=1)) # [[1, 5, 2], [3, 5, 4]]
# axis=1 permet d'insérer 5 à la deuxième colonne


#Opérations sur les tableaux de nombres numpy
print("______OPERATION SUR LES TABLEAUX_______")
X = np.arange(start=5,step=3,stop=16) # 5, 8,11,14 # crée un tableau de 5 à 16 avec un pas de 3
print("affichons le tableau X :",X) # tableau de taille (4,)donc 4 lignes et 1 colonne
#ici .ones, .zeros, .eye, .diag, .reshape, .transpose, .exp, .mean, etc.
# sont des fonctions de numpy qui permettent de créer des tableaux de nombres numpy exemples
# .ones crée un tableau rempli de 1, .zeros crée un tableau rempli de 0,
# .eye crée une matrice identité, .diag crée une matrice diagonale, .reshape permet de changer la forme du tableau,
# .transpose permet de transposer le tableau, .exp permet de calculer l'exponentielle de chaque élément du tableau,
# .mean permet de calculer la moyenne des éléments du tableau, etc.
A = np.ones((2,3)) # ici on a un tableau de 2 lignes et 3 colonnes rempli de 1
print("affichons le tableau A :",A) # tableau de taille (2,3)
B = X.reshape(2,2) #ici on a un tableau de 2 lignes et 2 colonnes ici on reshape le tableau X
# pour le transformer en tableau de 2 lignes et 2 colonnes reshape permet de changer la forme du tableau
# sans changer les données
print("affichons le tableau B :",B) # tableau de taille (2,2)
C = np.zeros((3,2)) # ici on a un tableau de 3 lignes et 2 colonnes rempli de 0
print("affichons le tableau C :",C) # tableau de taille (3,2)
D = np.eye(2) # matrice identité de taille 2x2 cest-à-dire une matrice carrée avec des 1 
#sur la diagonale et des 0 ailleurs .eyes permet de créer une matrice identité
# ici on a un tableau de 2 lignes et 2 colonnes rempli de 1
print("affichons le tableau D :",D) # matrice identité de taille (2,2)
print("affichons le type de données avec D.dtype :",D.dtype) # datatype: float64
# On peut aussi créer des tableaux de nombres numpy avec des fonctions mathématiques
np.diag([1,2]) # matrice diagonale cest-à-dire une matrice carrée avec des 1 sur la 
# diagonale et des 0 ailleurs comme ceci [[1,0],[0,2]]
print("affichons la matrice diagonale avec np.diag([1,2]) :",np.diag([1,2])) # [[1,0],[0,2]]
# ici on a un tableau de 2 lignes et 2 colonnes rempli de 1

E = C+np.ones(C.shape) # addition: même chose que C+1
print("affichons le tableau E :",E) # addition de C et d'un tableau de 1 de même forme que C
# ici on a un tableau de 3 lignes et 2 colonnes rempli de 1 cest-à-dire que chaque
# élément de C est additionné de 1 comme C est un tableau de 3 lignes et 2 colonnes 
# on ajoute 1 à chaque élément de C
print("affichons le type de données avec E.dtype :",E.dtype) # datatype: float64

# ici on a F qui est le produit élément par élément de B et D
# multiplication élément par élément: F[i,j] = B[i,j] * D[i,j] donc F est de même forme que B et D
# produit algébrique: J[i,j] = somme(B[i,k] * D[k,j]) pour k dans la dimension commune
# ici on a J qui est le produit algébrique de B et D
F = B*D # multiplication élément par élément
print("affichons le tableau F :",F) # multiplication élément par élément de B et D

J=np.dot(B,D) # produit algébrique
print("affichons le tableau J :",J) # produit algébrique de B et D
# ici on a J qui est le produit algébrique de B et D
#le .dot permet de faire le produit algébrique de deux tableaux
# le produit algébrique est la somme des produits des éléments de la première ligne de B
G = F.T # matrice transposée
print("affichons le tableau G :",G) # matrice transposée de F
# ici on a G qui est la matrice transposée de F
# la matrice transposée est obtenue en échangeant les lignes et les colonnes
# de F, c'est-à-dire que la première ligne de F devient la première colonne de G
# et la deuxième ligne de F devient la deuxième colonne de G, etc.
H = np.exp(G) # comme la plupart des fonctions, exp est appliquée élément par élément
print("affichons le tableau H :",H) # exponentielle de chaque élément de G
# ici on a H qui est l'exponentielle de chaque élément de G
# la fonction exp est appliquée élément par élément, c'est-à-dire que chaque élément de G
# est remplacé par son exponentielle, c'est-à-dire que chaque élément de G est remplacé par e^G[i,j]
# où e est la base du logarithme naturel (environ 2.71828)
# (sinon utilisez np.vectorize(my_function))
x = np.array([4, 2, 1, 5, 1, 10])
# x est un tableau de 6 éléments
# On peut trier les éléments d'un tableau avec la méthode sort
x.sort()
print("affichons le tableau x trié :",x) # [1, 1, 2, 4, 5, 10]
# On peut utiliser des conditions pour filtrer les éléments d'un tableau
# ici on utilise une condition pour filtrer les éléments de x
print("affichons les éléments de x supérieurs à 3 :",x[x>3]) # [4, 5, 10]
y=np.logical_and(x>=3, x<= 9, x!=1) # [T,F,F,T,F,F]
# ici on utilise la fonction logical_and pour créer un tableau de booléens
# qui indique si chaque élément de x est compris entre 3 et 9 inclus, et différent de 1
print("affichons les éléments de x compris entre 3 et 9 inclus et différent de 1 :",x[y]) # [4, 5]
# y est un tableau de booléens qui indique si chaque élément de x est compris entre 3 et 9 inclus, et différent de 1
# On peut utiliser ce tableau de booléens pour filtrer les éléments de x

x[y] # [4, 5]
print("affichons les éléments de x compris entre 3 et 9 inclus et différent de 1 :",x[y]) # [4, 5]
# On peut aussi utiliser des fonctions de numpy pour filtrer les éléments d'un tableau
print("affichons les éléments de x supérieurs à 3 avec np.where(x>3) :",np.where(x>3)) # (array([3, 4, 5]),)
# np.where retourne les indices des éléments de x qui sont supérieurs à 3
# ici .mean, .std, .var, .min, .max, .argmin, .argmax, etc.
# sont des fonctions de numpy qui permettent de calculer la moyenne, l'écart type,variance,
# minimum, maximum, indice du minimum, indice du maximum, etc. des éléments d'un tableau
print("affichons la moyenne de x avec np.mean(x) :",np.mean(x)) # 3.3333333333333335
print("affichons l'écart type de x avec np.std(x) :",np.std(x)) # 2.581988897471611
print("affichons la variance de x avec np.var(x) :",np.var(x)) # 6.666666666666667
print("affichons le minimum de x avec np.min(x) :",np.min(x)) # 1
print("affichons le maximum de x avec np.max(x) :",np.max(x)) # 10
print("affichons l'indice du minimum de x avec np.argmin(x) :",np.argmin(x)) # 0
print("affichons l'indice du maximum de x avec np.argmax(x) :",np.argmax(x)) # 5

print("affichons la proportion d'éléments de x supérieurs à 1.96 :",np.mean(np.random.randn(1000)>1.96))
# ici on utilise la fonction random.randn pour générer 1000 nombres aléatoires
# suivant une loi normale centrée réduite, puis on calcule la proportion d'éléments de x
# supérieurs à 1.96 en utilisant la fonction mean
# qui calcule la moyenne des éléments de x supérieurs à 1.96
# ici on utilise la fonction random.randn pour générer 1000 nombres aléatoires


# 13.3 Algèbre linéaire avec numpy
print("______ALGEBRE LINEAIRE AVEC NUMPY_______")
A = [[2, 1, 1], [4, 3, 0]] # matrice de taille (2,3)
B = [[1, 2], [12, 0]] # matrice de taille (2,2)
# On peut créer des matrices avec numpy en utilisant la fonction matrix
print("affichons la matrice A :",np.matrix(A)) # matrice de taille (2,3)
print("affichons la matrice B :",np.matrix(B)) # matrice de taille (2,2) ou bien (2,2)
print("affichons la matrice sans utiliser matrix :",np.array(A)) # matrice de taille (2,3) comme ceci
print("affichons la matrice sans utiliser matrix :", B) # ici on a B qui est une matrice de taille (2,2)
C = [[1, 2], [12, 0], [-1, 2]]# matrice de taille (3,2)
D = [[1, 2,-4], [2, 0, 0], [1, 2, 3]] # matrice de taille (3,3)
E = np.bmat([[A, B], [C, D]]) # block matrix permet de créer une matrice à partir de blocs
print("affichons la matrice E :",E) # matrice de taille (5,5) on aura comme blocs A, B, C et D affichés comme suit: 
# [[2, 1, 1, 1, 2], 
#  [4, 3, 0, 12, 0],
#  [1, 2, -4, 2, 0],
#  [12, 0, 1, 2, 3],
#  [-1, 2, 3, 0, 0]]

# ici on a E qui est une matrice de taille (5,5) composée des blocs A, B, C et D
# cest-à-dire que E est une matrice de 5 lignes et 5 colonnes 5 car elle est composée de 4 blocs de 
# taille (2,3), (2,2), (3,2) et (3,3) 
print("affichons le type de E :",type(E)) # <class 'numpy.matrix'>
# E est une matrice de type numpy.matrix
F = np.matrix(np.random.randn(5,5)) # matrice aléatoire de taille (5,5)
print("affichons la matrice aleatoire de taille (5,5) F :",F) # matrice de taille (5,5)
H = F*E # produit algébrique
print("affichons le produit algébrique de F et E :",H) # produit algébrique de F et E
# ici on a H qui est le produit algébrique de F et E cest-à-dire que H est une matrice de taille (5,5)
# obtenue en multipliant F et E, c'est-à-dire que chaque élément de H est obtenu en multipliant les éléments de la ligne i de F
# par les éléments de la colonne j de E, puis en faisant la somme de ces produits
# exemple : H[0,0] = F[0,:] * E[:,0] ou H[0,0] = np.dot(F[0,:], E[:,0])
# On peut aussi utiliser la fonction dot pour faire le produit algébrique
print("affichons le produit algébrique de F et E avec np.dot(F,E) :",np.dot(F,E)) # produit algébrique de F et E
# ici on a le même résultat que H, c'est-à-dire que np.dot(F,E) est équivalent à F*E
# On peut aussi utiliser la fonction matmul pour faire le produit algébrique
print("affichons le produit algébrique de F et E avec np.matmul(F,E) :",np.matmul(F,E)) # produit algébrique de F et E

B5 = np.linalg.matrix_power(B,5) # puissance de la matrice B
print("affichons la puissance de la matrice B à la puissance 5 :",B5) # puissance de la matrice B
# ici on a B5 qui est la matrice B élevée à la puissance 5, c'est-à-dire que chaque élément de B5 
# est obtenu en multipliant les éléments de la ligne i de B par les éléments de la colonne j de B,
# puis en faisant la somme de ces produits
# .linalg.matrix_power permet de calculer la puissance d'une matrice
Bm1 = np.linalg.inv(B) # inverse de la matrice B
print("affichons l'inverse de la matrice B :",Bm1) # inverse de la matrice B
# .linalg.inv permet de calculer l'inverse d'une matrice
# l'inverse d'une matrice est une matrice telle que le produit de la matrice par son inverse donne la matrice identité
# c'est-à-dire que B * Bm1 = I, où I est la matrice identité
# On peut aussi utiliser la fonction inv pour faire l'inverse d'une matrice
print("affichons l'inverse de la matrice B avec np.linalg.inv(B) :",np.linalg.inv(B)) # inverse de la matrice B
# ici on a le même résultat que Bm1, c'est-à-dire que np.linalg.inv(B) est équivalent à Bm1
dB = np.linalg.det(B) # determinant de la matrice B
print("affichons le determinant de la matrice B :",dB) # determinant de la matrice B
# .linalg.det permet de calculer le déterminant d'une matrice
# le déterminant d'une matrice est un nombre qui permet de savoir si la matrice est inversible ou non
# si le déterminant est différent de 0, la matrice est inversible, sinon la matrice n'est pas inversible
# inversible veut dire qu'il existe une matrice inverse telle que le produit de la matrice par son inverse donne la matrice identité
# c'est-à-dire que B * Bm1 = I, où I est la matrice identité

# .linalg.solve permet de résoudre un système d'équations linéaires
# ici on a un système d'équations linéaires de la forme Ax = b,cest-à-dire que A est
# une matrice de coefficients,
# x est un vecteur de variables et b est un vecteur de constantes
# On peut résoudre ce système d'équations linéaires en utilisant la fonction solve
# utile pour résoudre des systèmes d'équations linéaires
# exemple : A = [[2, 1], [4, 3]], b = [3, 12]
# On peut résoudre ce système d'équations linéaires en utilisant la fonction solve  
x = np.linalg.solve(B,[3,12])#solves B*x=[[3],[12]]
# ici on 3 est le résultat de la première équation et 12 est le résultat de la deuxième équation
print("affichons la solution du système d'équations linéaires B*x=[[3],[12]] :",x) 
# solution du système d'équations linéaires B*x=[[3],[12]]
# exemple : B = [[1, 2], [12, 0]], x = [3, 12]
#la procedure est la même que pour la résolution d'un système d'équations linéaires
# exemple de resolution 2x + 3y = 12 et 4x + 5y = 24
#ce système d'équations linéaires peut être résolu en utilisant la fonction solve comme suit:
# A = [[2, 3], [4, 5]], b = [12, 24]

# 1.14 Analyse spectrale avec numpy
print("______ANALYSE SPECTRALE AVEC NUMPY_______")
#analyse spectrale est une méthode mathématique qui permet d'étudier les propriétés
# d'un signal en le décomposant en une somme de sinusoïdes
# On peut calculer les valeurs propres et les vecteurs propres d'une matrice avec numpy
# les valeurs propres sont les scalaires associés à une matrice carrée
# les vecteurs propres sont les vecteurs associés à une matrice carrée
# On peut calculer les valeurs propres et les vecteurs propres d'une matrice avec la fonction eigvals
# ou la fonction eig de numpy
A = [[1, 2], [12, 3]] # matrice de taille (2,2)
print("affichons la matrice A :",np.array(A)) # matrice de taille (2,2)
x = np.linalg.eigvals(A) # eigenvalues permet de calculer les valeurs propres d'une matrice
print("affichons les valeurs propres de la matrice A :",x) # valeurs propres cest-à-dire les scalaires associés à la matrice A
#scalaires veut dire que les valeurs propres sont des nombres réels ou complexes et donc
# elles peuvent être utilisées pour étudier les propriétés de la matrice A
#exemple : A = [[1, 2], [12, 3]], les valeurs propres sont les scalaires associés à la matrice A
# est un nombre réel ou complexe qui permet de savoir si la matrice A est inversible ou non
# si les valeurs propres sont différentes de 0, la matrice A est inversible,ou sinon la matrice A n'est pas inversible
# la difference entre eigenvalues et eigenvectors est que les valeurs propres sont des scalaires 
# associés à une matrice carrée alors que les vecteurs propres sont des vecteurs associés à une matrice carrée
valp , vectp = np.linalg.eig(A) # ici on a valp qui est un tableau de valeurs propres et vectp qui est un tableau de vecteurs propres combinés
# .linalg.eig permet de calculer les valeurs propres et les vecteurs propres d'une matrice 
print("affichons les valeurs propres de la matrice A avec np.linalg.eig(A) :",valp) # valeurs propres de la matrice A
print("affichons les vecteurs propres de la matrice A avec np.linalg.eig(A) :",vectp) # vecteurs propres de la matrice A
# valp Ce sont des scalaires λ, qui indiquent par combien chaque vecteur propre est
#  dilaté ou contracté par la transformation associée à A
#valp[i] est une valeur propre λᵢ (la direction du vent)
#vectp[:, i] est le vecteur propre vᵢ associé à λᵢ (l'inclinaison de la flèche)
#La relation vérifiée est : Avᵢ = λᵢvᵢ


#Hermitian matrices methods:
S = [[1, 2], [2, 3]]
y = np.linalg.eigvalsh(S) # .linalg.eigvalsh permet de calculer les valeurs propres d'une matrice hermitienne
print("affichons les valeurs propres de la matrice hermitienne S :",y) # valeurs propres de la matrice hermitienne S
# une matrice hermitienne est une matrice carrée complexe qui est égale à sa propre transposée conjuguée
# c'est-à-dire que S est une matrice hermitienne si S = S.H
# valeurs propres de la matrice hermitienne S : [ -0.23606798   4.23606798]
# valeurs propres de la matrice hermitienne S avec np.linalg.eigh(S) : [ -0.23606798   4.23606798]
# affichons les vecteurs propres de la matrice hermitienne S avec np.linalg.eigh(S) : 
#[[-0.85065081  0.52573111]
# [ 0.52573111  0.85065081]] 
# ici on a des valeurs negatives et positives, ce qui est normal pour une matrice hermitienne
# car les valeurs propres d'une matrice hermitienne peuvent être réelles ou complexes




# H est la transposée conjuguée de S, c'est-à-dire que H est obtenue en échangeant les lignes et les colonnes de S
# et en prenant le conjugué de chaque élément de S
 # eigenvalues and eigenvectors:
valp , vectp = np.linalg.eigh(S) # .linalg.eigh permet de calculer les valeurs propres et les vecteurs propres d'une matrice hermitienne
print("affichons les valeurs propres de la matrice hermitienne S avec np.linalg.eigh(S) :",valp) # valeurs propres de la matrice hermitienne S
print("affichons les vecteurs propres de la matrice hermitienne S avec np.linalg.eigh(S) :",vectp) # vecteurs propres de la matrice hermitienne S

#SVD:
#U → matrice orthogonale (vecteurs propres des colonnes de A·Aᵗ)
#s → valeurs singulières (scalaires positifs, racines carrées des valeurs propres de AᵗA)
#V → matrice orthogonale (vecteurs propres des lignes de A)
U,s,V=np.linalg.svd(A) #.linalg.svd permet de calculer la décomposition en valeurs singulières (SVD) d'une matrice
print("affichons la matrice U de la SVD de A :",U) # matrice U de la SVD de A
print("affichons la matrice S de la SVD de A :",s) # matrice S de la SVD de A
print("affichons la matrice V de la SVD de A :",V) # matrice V de la SVD de A
Ap = np.matrix(U)*np.diag(s)*V # on a Ap qui est la matrice A reconstruite à partir de la SVD
print("affichons la matrice Ap reconstruite à partir de la SVD de A :",Ap) # matrice Ap reconstruite à partir de la SVD de A
# Ap est la matrice A reconstruite à partir de la SVD, c'est-à-dire que Ap est obtenue en multipliant la matrice U par la matrice S
# et la matrice V, c'est-à-dire que Ap = U*S*V
print("affichons la différence entre A et Ap :",A-Ap)# pour vérifier que la matrice A est bien reconstruite à partir de la SVD
# ici on a la différence entre A et Ap, c'est-à-dire que A - Ap




 #Copie de tableaux numpy
print("______COPIE DE TABLEAUX NUMPY_______")
x = np.array([[8,3,2],[5,1,0],[9,7,1]]) # tableau de taille (3,3)
print("affichons le tableau x :",x) # tableau de taille (3,3
y = x # y est une référence à x, c'est-à-dire que y pointe vers le même objet que x
print("affichons le tableau y :",y) # tableau de taille (3,3
x[0,0]+=1 # on ajoute 1 à l'élément (0,0) de x
print("affichons le tableau x après avoir ajouté 1 à l'élément (0,0) :",x) # tableau de taille (3,3)
print("affichons le tableau y après avoir ajouté 1 à l'élément (0,0) de x :",y) # tableau de taille (3,3)
# ici on a x et y qui sont des références au même objet, c'est-à-dire que y pointe vers le même objet que x
x[0,0]-y[0,0] # on soustrait l'élément (0,0) de y de l'élément (0,0) de x
z=x.copy() # z est une copie de x, c'est-à-dire que z pointe vers un nouvel objet qui est une copie de x
print("affichons le tableau z :",z) # tableau de taille (3,3)
x[0,0]+=1 # on ajoute 1 à l'élément (0,0) de x
print("affichons le tableau x après avoir ajouté 1 à l'élément (0,0) :",x) # tableau de taille (3,3)
x[0,0]-z[0,0] # on soustrait l'élément (0,0) de z de l'élément (0,0) de x
print("affichons le tableau z après avoir ajouté 1 à l'élément (0,0) de x :",z) # tableau de taille (3,3)

 #1.15 Boucles vs programmation matricielle
print("______BOUCLES VS PROGRAMMATION MATRICIELLE_______")
from time import time    #bibliothèque pour mesurer le temps d'exécution pour les performances
n = int(1e7) 
# ici on crée une variable n qui vaut 10^7, c'est-à-dire 10 millions
# On va comparer deux méthodes pour calculer la somme des inverses des entiers de 1 à n
# La somme des inverses des entiers de 1 à n est égale à la fonction gamma d'Euler
# La fonction gamma d'Euler est définie comme suit :
# gamma(n) = somme(1/i) pour i de 1 à n

# Methode 1. Boucle for
t1 = time()
gamma1=sum([1./i for i in range(1,n+1)])- np.log(n) # le logarithme naturel de n
# ici on utilise une boucle for pour calculer la somme des inverses des entiers de 1 à n
# on utilise la fonction sum pour calculer la somme des inverses des entiers de 1 à n
# on utilise la fonction log de numpy pour calculer le logarithme naturel de n dans le but 
# de comparer les deux méthodes
# on soustrait le logarithme naturel de n à la somme des inverses des entiers de 1 à n
# pour obtenir le résultat final ici lobjectif est de calculer la fonction gamma d'Euler
# on utilise la fonction time pour mesurer le temps d'exécution de la méthode 1
# 1./i calcule l'inverse de i, c'est-à-dire 1/i
# range(1,n+1) génère une séquence d'entiers de 1 à n inclus
# np.log(n) calcule le logarithme naturel de n .np renvoie le module numpy
# on utilise la fonction time pour mesurer le temps d'exécution de la méthode 1

t2 = time()
temps1 = t2- t1
# Methode 2. Numpy
t1 = time()
gamma2=np.sum(1. / np.arange(1,n+1))- np.log(n)
t2 = time()
temps2 = t2 - t1 
print("Facteur de gain: ", temps1/temps2) # ici on calcule le facteur de gain entre les deux méthodes
# le facteur de gain est le rapport entre le temps d'exécution de la méthode 1
# et le temps d'exécution de la méthode 2
# cest-à-dire que si le facteur de gain est supérieur à 1, la méthode 2 est plus rapide que la méthode 1
# si le facteur de gain est inférieur à 1, la méthode 1 est plus rapide

#Remarque 1.1 Eviter si possible boucles et tests en Python.
# car les opérations sur les tableaux numpy sont généralement plus rapides
# que les boucles et les tests en Python.
# Remarque 1.2. Utiliser les fonctions numpy pour les opérations sur les tableaux

#Boucles vs programmation matricielle (meilleur programme)
from timeit import timeit

N = 300
setup = """

n = int(1e5)
"""
code_boucle = """
np.sum([1. / i for i in range(1, n)])- np.log(n)
"""
time_boucle=timeit(code_boucle ,setup=setup ,number=N)
code_numpy = """
np.sum(1. / np.arange(1, n))- np.log(n)
"""
time_numpy=timeit(code_numpy ,setup=setup ,number=N)
print("Facteur : {}".format(time_boucle/time_numpy))
#1.16 Variables aléatoires
#1.16.1 Génération de variables aléatoires continues avec numpy
#import numpy.random as npr
my_sample = npr.multivariate_normal(mean=paramètres, cov=taille_du_tableau)
— npr.rand(d1,d2,...) : tableau d1 ×d2×,... de v.a.i. unif. sur [0,1]
— npr.uniform(low=a,high=b,size=n) : v.a.i. unif. sur [a,b[ (size=n peut être rem
placé par size=(d1,d2,...), comme partout dans ce qui suit)
— npr.randn(d1,d2,...) : tableau d1 ×d2×,... de v.a.i. N (0,1)
— npr.multivariate_normal(mean=V,cov=C,size=n) : vecteurs aléatoires indé
pendants de loi N (V,C) rangés dans un tableau de taille n×N, où N est la taille de
V et N ×N celle de C
 — npr.exponential(scale=s,size=n) : v.a.i. exponentielles de moyenne s
 Beaucoup d’autres exemples sur
 http ://docs.scipy.org/doc/numpy/reference/routines.random.html
 1.16.2 Génération de variables aléatoires discrètes avec numpy
 import numpy.random as npr
 my_sample = npr.ma_loi(param\‘etres, taille_du_tableau)
 — npr.randint(low=a,high=b,size=n) : v.a. unif. sur [a,b[
 — npr.choice([a1,...,an],p=[p1,...,pn],size=n) : tirages indép. dans [a1,...,an] de
 loi [p1,...,pn]
 — npr.permutation(mon_urne) : permutation de mon_urne
 — npr.binomial(N,p,size=n)
 