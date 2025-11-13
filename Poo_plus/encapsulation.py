# =============================
# rectangle.py
# =============================

# Définition d’une classe Rectangle
class Rectangle:
    def __init__(self, long, larg):
        # Attributs protégés (par convention, avec un seul _underscore)
        self._long = long
        self._larg = larg

    def surface(self):
        """
        📌 Calcule et retourne la surface du rectangle.
        """
        return self._long * self._larg
# =============================
# pave.py
# =============================

# Importation de Rectangle
from rectangle import Rectangle

# Classe Pavé qui hérite de Rectangle
class Pave(Rectangle):
    def __init__(self, long, larg, haut):
        # Appel du constructeur de Rectangle
        super().__init__(long, larg)

        # Attribut privé (double underscore)
        self.__haut = haut

    def volume(self):
        """
        📌 Calcule le volume du pavé.
        Volume = surface * hauteur
        """
        return self.surface() * self.__haut

    # Getter pour accéder à la hauteur
    def get_haut(self):
        return self.__haut

    # Setter pour modifier la hauteur
    def set_haut(self, valeur):
        if valeur > 0:
            self.__haut = valeur
        else:
            print("Erreur : la hauteur doit être positive")
# =============================
# test.py
# =============================

from rectangle import Rectangle
from pave import Pave

if __name__ == "__main__":
    # Création d’un rectangle
    r = Rectangle(4, 6)
    print("Surface du rectangle :", r.surface())  # 24

    print("\n---\n")

    # Création d’un pavé
    p = Pave(3, 5, 10)
    print("Volume du pavé :", p.volume())  # 150

    # Tentative d’accès direct à __haut (va échouer car privé)
    try:
        print(p.__haut)
    except AttributeError as e:
        print("Erreur :", e)

    # Accès correct via le getter
    print("Hauteur du pavé (via getter) :", p.get_haut())

    # Modification via le setter
    p.set_haut(15)
    print("Nouveau volume :", p.volume())


# Encapsulation = cacher les données sensibles.
# _attribut = protégé (par convention).
# __attribut = privé (réellement masqué).
# Pour manipuler un attribut privé → utiliser des getters et setters.