# Cet exercice illustre les principes fondamentaux de la programmation orientée objet :
# encapsulation, composition et polymorphisme. La classe Point sert de brique de base pour
# construire des formes géométriques comme les rectangles et les polygones. La classe Rectangle
# montre une relation de composition (utilise deux objets Point), tandis que Polygone utilise
# une liste de points pour former une structure plus complexe. Chaque classe encapsule son propre 
# comportement (aire, périmètre, etc.), ce qui permet l’extension modulaire du code. Ce système met en
# évidence l’importance de la réutilisabilité du code et de l’organisation hiérarchique des objets.



# La représentation sous forme de chaîne d'un objet AVEC la __str__()méthode 
class Point:
    """Classe représentant un point dans un plan (x, y)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, other):
        """Distance entre deux points"""
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
class Rectangle:
    """Classe représentant un rectangle défini par deux points opposés"""
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def aire(self):
        """Calcule l'aire du rectangle"""
        largeur = abs(self.p2.x - self.p1.x)
        hauteur = abs(self.p2.y - self.p1.y)
        return largeur * hauteur

    def __str__(self):
        return f"Rectangle: coin 1 {self.p1}, coin 2 {self.p2}, aire = {self.aire()}"
class Polygone:
    """Classe représentant un polygone avec une liste de points"""
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError("Un polygone doit avoir au moins 3 points.")
        self.points = points

    def __str__(self):
        return "Polygone: " + " -> ".join(str(p) for p in self.points)

    def perimetre(self):
        """Calcule le périmètre du polygone"""
        perim = 0
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]  # retour au début
            perim += p1.distance(p2)
        return perim
# Création de points
p1 = Point(1, 1)
p2 = Point(4, 5)
p3 = Point(6, 2)
p4 = Point(3, -1)
p5 = Point(0, 2)

# Test du rectangle
rect = Rectangle(p1, p2)
print(rect)

# Test du polygone (pentagone)
points = [p1, p2, p3, p4, p5]
pentagone = Polygone(points)
print(pentagone)
print(f"Périmètre du pentagone : {pentagone.perimetre():.2f}")

