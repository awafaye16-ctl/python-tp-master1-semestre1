# Ici, le TDA "pile" encapsule les données (elements) et fournit des opérations claires : empiler() et depiler().

# Le navigateur ne se soucie pas de savoir si la pile est implémentée avec une liste, un tableau ou autre → il utilise juste les méthodes.

# C’est l’avantage de l’abstraction et de la modularité des TDA.
class Pile:
    """Implémentation d'une pile (stack) avec TDA."""
    def __init__(self):
        self.elements = []

    def empiler(self, element):
        """Ajoute un élément en haut de la pile."""
        self.elements.append(element)

    def depiler(self):
        """Retire et retourne le dernier élément empilé."""
        if not self.est_vide():
            return self.elements.pop()
        return None

    def est_vide(self):
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)


# Utilisation dans un navigateur
pile_retour = Pile()
pile_suivant = Pile()

# Je visite des pages
pile_retour.empiler("Page A")
pile_retour.empiler("Page B")
pile_retour.empiler("Page C")

print("Historique :", pile_retour)

# Je fais "Retour"
page_actuelle = pile_retour.depiler()
pile_suivant.empiler(page_actuelle)

print("Retour à :", pile_retour.depiler())  # Page B
