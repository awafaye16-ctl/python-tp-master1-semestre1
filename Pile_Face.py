# Définition d'une erreur spécifique pour pile vide
PileErreur = ValueError('Pile vide')

def nouvelle_pile():
    """Crée une pile (ici représentée par une liste)."""
    return []

def empile(L, e):
    """Empile un élément e dans la pile L."""
    L.append(e)

def depile(L):
    """Dépile l’élément au sommet de la pile et le retourne."""
    if L == []:
        raise PileErreur
    return L.pop()

def sommet(L):
    """Retourne l’élément au sommet de la pile sans le retirer."""
    if L == []:
        raise PileErreur
    return L[-1]   # plus lisible que L[len(L)-1]

def est_vide(L):
    """Vérifie si la pile L est vide."""
    return L == []


#from pile import *

# Créer une pile
p = nouvelle_pile()

# Empiler
empile(p, 10)
empile(p, 20)
empile(p, 30)

print("Sommet :", sommet(p))   # affiche 30
print("Dépile :", depile(p))   # enlève et retourne 30
print("Pile vide ?", est_vide(p))  # False
