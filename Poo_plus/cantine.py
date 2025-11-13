FileErreur = ValueError('File vide')

def nouvelle_file():
    # Création de la file (une liste vide)
    return []

def enfile(L, e):
    # Enfilement = ajouter un élément à la fin de la file
    L.append(e)

def defile(L):
    # Défiler = retirer l’élément en tête de file
    if L == []:
        raise FileErreur
    L.pop(0)

def tete(L):
    # Accéder à l’élément en tête de file sans le retirer
    return L[0]

# def vider_file():
#     # Vérifier si la file est vide
#     return L == []   # ⚠️ problème ici : L n'est pas défini !
def vider_file(L):
    return L == []


# from file import nouvelle_file, enfile, defile, tete, vider_file

# Création d'une file
cantine = nouvelle_file()

# Trois étudiants arrivent
enfile(cantine, "Alice")
enfile(cantine, "Bob")
enfile(cantine, "Charlie")

print("Tête de file :", tete(cantine))  # Alice

# On sert les étudiants dans l'ordre d'arrivée
while not vider_file(cantine):
    print("Servir :", tete(cantine))
    defile(cantine)

# enfile(L, e) → ajoute à la fin (comme une personne qui se met au bout d’une queue).

# defile(L) → enlève le premier élément (la personne en tête est servie en premier).

# tete(L) → permet de voir qui est en tête sans la retirer.

# vider_file(L) → teste si la file est vide.

# C’est donc une structure FIFO (le premier arrivé est le premier servi).