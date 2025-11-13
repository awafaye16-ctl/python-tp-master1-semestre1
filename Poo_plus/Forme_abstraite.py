# Interface : Forme
# Méthode obligatoire : calculAire()
# Classes concrètes : TriangleRectang, Cercle, Rectangle
# Chacune doit définir comment calculer son aire.
# Une interface est un contrat (liste de méthodes à respecter).
# Elle ne décrit pas l’implémentation, juste l’obligation.
# En Python, on simule une interface avec une classe abstraite (abc.ABC).
# Différence avec une classe :
# Une classe peut créer des objets → ✅.
# Une interface ne peut pas être instanciée → ❌.
# Une classe peut avoir des attributs et des méthodes implémentées.
# Une interface ne définit que des signatures de méthodes (quoi faire, pas comment).


from abc import ABC, abstractmethod

# Définition de l'interface (classe abstraite en Python)
class Forme(ABC):
    @abstractmethod
    def calcul_aire(self):
        pass

# Implémentation concrète
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calcul_aire(self):
        return self.largeur * self.hauteur

class TriangleRectang(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def calcul_aire(self):
        return (self.base * self.hauteur) / 2

# Utilisation
formes = [Rectangle(4, 5), TriangleRectang(3, 6)]

for f in formes:
    print(f"Surface : {f.calcul_aire()}")
