

# =============================
# parent.py
# =============================

# 📌 Définition d’une classe Parent
# Une classe est un modèle qui définit des attributs et des méthodes.
class Parent:
    # Une méthode est une fonction définie dans une classe
    def greet(self):
        # Ici, la méthode affiche un message simple
        print("Hello World")

class Enfant(Parent):
    pass
# =============================
# child.py
# =============================

# On importe la classe Parent pour pouvoir l’hériter
#from parent import Parent

# 📌 Définition d’une classe Enfant (Child) qui hérite de Parent
class Child(Parent):
    
    # Redéfinition de la méthode greet()
    def greet(self):
        print("Ici le fils")   # Spécifique à la classe enfant

        # 📌 Appel de la méthode greet() de la classe Parent
        # grâce à super()
        super().greet()

        # Ajout d’un nouveau comportement après l’appel du parent
        print("Au revoir")


# =============================
# test.py
# =============================

# On importe les classes pour les utiliser
# from parent import Parent
# from child import Child

# 📌 Point d’entrée du programme en Python
if __name__ == "__main__":

    # Instanciation de la classe Parent
    print("=== Utilisation de Parent ===")
    p = Parent()
    p.greet()   # Affiche "Hello World"

    print("\n---\n")

    # Instanciation de la classe Child
    print("=== Utilisation de Child ===")
    c = Child()
    c.greet()

