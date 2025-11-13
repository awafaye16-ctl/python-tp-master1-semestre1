# Le polymorphisme :
# C’est le fait qu’un même nom de méthode (ici move) puisse avoir des comportements différents
# selon la classe de l’objet.
# Classe parent Vehicle → définit une méthode move() générique.
# Classe Car → hérite sans redéfinir, donc garde "Move!".
# Classe Boat → redéfinit (override) move() pour afficher "Sail!".
# Classe Plane → redéfinit aussi move() pour afficher "Fly!".
# 🔑 Le principe appliqué :
# 👉 Polymorphisme par redéfinition de méthode (override).
# Même appel x.move() → mais résultat dépend du type réel de l’objet (Car, Boat, Plane).


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()  