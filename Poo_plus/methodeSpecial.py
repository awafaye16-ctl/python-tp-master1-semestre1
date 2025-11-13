class Personne:
    """Classe qui représente une personne"""

    def __init__(self, nom):
        self.nom = nom
    
    def __str__(self):
        return f"Personne: {self.nom}"
    
    def __repr__(self):
        return f"Personne(nom='{self.nom}')"

p = Personne("Awa")
print(str(p))   # Personne: Awa
print(repr(p))  # Personne(nom='Awa')
print(p.__dict__)  # {'nom': 'Awa'}

# __file__
# __doc__
# __module__
# __classe
# __name__
# __del__



class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Représentation
    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Addition
    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)
    
    # Comparaison
    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y
    
    # Longueur
    def __len__(self):
        return abs(self.x) + abs(self.y)

v1 = Vecteur(2, 3)
v2 = Vecteur(1, 4)

print(v1)            # (2, 3)
print(v1 + v2)       # (3, 7)
print(v1 == v2)      # False
print(len(v1))       # 5


class Panier:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)
    def __contains__(self, item): return item in self.items

p = Panier(["pomme", "banane"])
print(len(p))          # 2
print("banane" in p)   # True
