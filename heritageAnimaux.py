# Classe de base pour tous les animaux
class Animal:
    def __init__(self, espece, couleur, nombre_de_pattes):
        self.espece = espece
        self.couleur = couleur
        self.nombre_de_pattes = nombre_de_pattes
#str pour formater laffichage en phrase comprehensible
    def __str__(self):
        return f"{self.espece} de couleur {self.couleur} avec {self.nombre_de_pattes} pattes."

    def set_espece(self, espece):
        self.espece = espece

    def set_couleur(self, couleur):
        self.couleur = couleur

    def set_nombre_de_pattes(self, nombre):
        self.nombre_de_pattes = nombre
    
    def get_espece(self):
        return self.espece
    def get_couleur(self):
        return self.couleur
    def get_nombre_de_pattes(self):
        return self.nombre_de_pattes

# 1. À quoi servent les getters et setters ?

# Un getter sert à récupérer la valeur d’un attribut privé.

# Un setter sert à modifier la valeur d’un attribut privé en contrôlant l’accès (validation, sécurité, règles métier).

#  Sans eux, on accède directement aux attributs (obj.attribut), mais cela brise l’encapsulation : on risque de modifier
#  un attribut n’importe comment.
#  Avec eux, on impose des règles (ex : un mouton doit toujours avoir 4 pattes, donc on empêche set_nombre_de_pattes(3)).
    
# class Animal:
#     def __init__(self, espece, couleur, nombre_de_pattes):
#         self.__espece = espece              # attribut privé
#         self.__couleur = couleur            # attribut privé
#         self.__nombre_de_pattes = nombre_de_pattes  # attribut privé

#     # --- Getters ---
#     def get_espece(self):
#         return self.__espece

#     def get_couleur(self):
#         return self.__couleur

#     def get_nombre_de_pattes(self):
#         return self.__nombre_de_pattes

#     # --- Setters ---
#     def set_couleur(self, couleur):
#         """On autorise le changement de couleur"""
#         self.__couleur = couleur

#     def set_nombre_de_pattes(self, nombre):
#         """On impose une règle : un animal ne peut pas avoir moins de 0 pattes"""
#         if nombre >= 0:
#             self.__nombre_de_pattes = nombre
#         else:
#             print("Erreur : un animal ne peut pas avoir un nombre négatif de pattes.")

#     def __str__(self):
#         return f"{self.__espece} de couleur {self.__couleur}, avec {self.__nombre_de_pattes} pattes."


# # --- Spécialisation : Mouton ---
# class Mouton(Animal):
#     def __init__(self, couleur):
#         super().__init__("Mouton", couleur, 4)
    
    





# p.dict permet de visualiser sous forme de dictionnaire

#  Sous-classes spécifiques
class Mouton(Animal):  
    """Classe représentant un mouton"""   
    # Docstring : explique que cette classe sert à créer des objets de type mouton

    def __init__(self, couleur):  
        # Constructeur : il est appelé lors de la création d'un objet mouton
        # Ici, on demande seulement la couleur en paramètre, car l'espèce ("Mouton") 
        # et le nombre de pattes (4) sont fixes et communs à tous les moutons.

        super().__init__("Mouton", couleur, 4)  
        # Appel du constructeur de la classe mère (Animal).
        # On transmet : 
        #  - "Mouton" comme espèce (fixe)
        #  - couleur (transmise par l’utilisateur)
        #  - 4 comme nombre de pattes (fixe pour tous les moutons)


class Loup(Animal):
    """Classe représentant un loup"""
    def __init__(self, couleur):
        super().__init__("Loup", couleur, 4)


class Serpent(Animal):
    """Classe représentant un serpent"""
    def __init__(self, couleur):
        super().__init__("Serpent", couleur, 0)


class Perroquet(Animal):
    """Classe représentant un perroquet"""
    def __init__(self, couleur):
        super().__init__("Perroquet", couleur, 2)


#  Classes pour régimes alimentaires
class Carnivore:
    def __init__(self, viande_par_jour):
        self.consommation_viande = viande_par_jour

    def devorer(self):
        print(f"Il peut dévorer {self.consommation_viande} gramme(s) de viande par jour.")


class Herbivore:
    def __init__(self, herbe_par_jour):
        self.consommation_herbe = herbe_par_jour

    def brouter(self):
        print(f"Il peut brouter {self.consommation_herbe} gramme(s) d'herbe par jour.")


# Exemple d’animal omnivore
class Porc(Carnivore, Herbivore, Animal):
    """Un porc est omnivore, donc mange viande + herbe"""
    def __init__(self, couleur, viande, herbe):
        Animal.__init__(self, "Porc", couleur, 4)
        Carnivore.__init__(self, viande)
        Herbivore.__init__(self, herbe)


# Création d'animaux
m1 = Mouton("blanc")
l1 = Loup("gris")
s1 = Serpent("vert")
p1 = Perroquet("rouge")
porc = Porc("rose", 1500, 1750)

# Affichage des animaux
print(m1)
print(l1)
print(s1)
print(p1)
print(porc)

# Comportements du porc omnivore
porc.brouter()
porc.devorer()
# m1.brouter()  # Mouton est herbivore
# l1.devorer()  # Loup est carnivore

# Maintenant que nous avons créé des animaux, nous allons les organiser dans des cages.
#MAintenant que nous avons creer des animaux, nous allons mettre en case
#creer une classe cage
#lors que lon creera une cage, on pourra lui attribuer un numero didentifiant unique
#et lui ajouter des animaux
class Cage:
    def __init__(self, id_cage):
        self.id_cage = id_cage
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def afficher_animaux(self):
        for animal in self.animaux:
            print(animal)

# #je veux maintenant creer une liste qui contiendra tous les animaux
# animaux = [m1, l1, s1, p1, porc]
# # Affichage de tous les animaux dans la liste
# print("\nListe des animaux :")
# for animal in animaux:
#     print(animal)

#creer une cage
print("\nCréation de la cage 1@@@@@@@@@@@@@@@")
cage1 = Cage(1)
# Ajouter des animaux à la cage
cage1.ajouter_animal(m1)
cage1.ajouter_animal(l1)
cage1.ajouter_animal(s1)
cage1.ajouter_animal(p1)
cage1.ajouter_animal(porc)  
# Afficher les animaux dans la cage
print("\nAnimaux dans la cage 1 :")
cage1.afficher_animaux()

#et je veux pouvoir ajouter nimporte quel nombre danimale 3,5,6 en utilisant les
#fonction a parametre variable 
#*animaux permet de passer un nombre variable d'arguments a la fonction
def ajouter_animaux(self, *animaux):
    for animal in animaux:
        self.animaux.append(animal)
#utilisation de getteur et setter pour modifier les attributs des animaux dans la cage
    

# Exemple d'ajout de plusieurs animaux
#__repr__permet de representer la cage adapter sa difference entre __str__ et __repr__ est que
# __str__ est utilisé pour l'affichage informel (en chaine de caractere de lobjet )et __repr__ cest 
# la representation de lobjet pour l'affichage formel ou le débogage
# exemple avec __repr__  : 
def __repr__(self):
    output = f"Cage {self.id_cage}:\n"
    output += "\n".join(str(animal) for animal in self.animaux) #output permet de representer la cage
    #.join permet de concatené les chaines de caracteres
    return output
loup2 = Loup("noir")
#ajout de plusieurs animaux
#cage1.ajouter_animaux(loup2,m1,s1)
# on doit pouvoir afficher les animaux selon leur couleur ,leur nombre et leur type
#Etant donne la structure de nos classes, nous pouvons filtrer les animaux par couleur, type et nombre.
#le zoo z
#creation de zoo l
#je veux compter la couleur des animaux dans chaque cas 
class zoo:

    def animal_by_color(self,couleur):
        liste=[]
        for case in self.case:
            for animal in case.animal:
                if animal.couleur == couleur:
                    liste.append(animal)
            return liste

        #.get_nombre_pattes permet de recuperer le nombre de pattes dun animal  pour filtrer les animaux par nombre de pattes
    def animal_by_leg(self,leg):
        liste=[]
        for case in self.case:
            for animal in case:
                if animal.get_nombre_pattes() == leg:
                    liste.append(animal)

        return liste
    def __dir__(self):
        return ['id_cage', 'animaux', 'ajouter_animal', 'afficher_animaux', 'ajouter_animaux', '__repr__']
    # par comprehension
#nombre de pattes dans un zoo
def nombre_pattes_zoo(self):
    return sum(animal.get_nombre_pattes() for case in self.cases for animal in case.animaux)

#__dir__ permet de lister les attributs et methodes d'une classe
def __dir__(self):
    return ['id_cage', 'animaux', 'ajouter_animal', 'afficher_animaux', 'ajouter_animaux', '__repr__']

# Ainsi, on peut filtrer les animaux par couleur, type et nombre de pattes en utilisant les méthodes définies.
# On peut aussi compter le nombre total de pattes dans le zoo en utilisant la méthode nombre_pattes_zoo.
# Cela permet une gestion flexible et efficace des animaux dans le zoo.
# Ce système met en évidence l’importance de la réutilisabilité du code et de l’organisation hiérarchique des objets.
# Parfait 👍 tu touches ici un concept important en **modélisation orientée objet** : les relations entre classes
# On distingue **généralisation/spécialisation**, **composition** et **agrégation**.
# ---
# ## ⚖️ Différences clés     
# - **Généralisation/spécialisation** : Relation "est un" (ex: un Chien est un Animal)
# - **Composition** : Relation "partie de" (ex: une Cage est composée d'Animaux)
# - **Agrégation** : Relation "a un" (ex: un Zoo a des Cages)
# ---
# 👉 En résumé :
# - La **généralisation** permet de définir des classes plus générales à partir de classes plus spécifiques.
# - La **composition** implique que les objets d'une classe sont constitués d'autres objets.
# - L'**agrégation** est une forme de relation où un objet "possède" d'autres objets, mais sans dépendance forte.
# Parfait 👍 tu touches ici un concept important en **modélisation orientée objet** : les relations entre classes   .
# DONC les point importants sont :
# 1. Généralisation / Spécialisation : "est un"
# 2. Composition : "partie de"
# 3. Agrégation : "a un"
#exemple de composition et d'agrégation dans le code heritagesPoints.py
# un point est un objet de base qui peut etre utilisé pour construire des formes plus complexes comme des rectangles et des polygones
# un rectangle est composé de deux points (relation de composition)
# un polygone utilise une liste de points pour former une structure plus complexe (relation d'agrégation)
# chaque classe encapsule son propre comportement (aire, périmètre, etc.), ce qui permet l’extension modulaire du code.