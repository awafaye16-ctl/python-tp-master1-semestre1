# // **Exercice_ZOO**
# // Nous allons représenter les animaux comme des objets Python, chaque espèce étant définie comme une classe distincte. 
# Tous les objets d'une classe particulière auront la même espèce et le même nombre de pattes, mais la couleur
#  variera d'une instance à l'autre. On peut ainsi créer un  mouton blanc, également récupérer des informations sur 
# l'animal à partir de l'objet en récupérant ses attributs(espece, couleur, nombre de pieds).
# // Si on convertit un animal en String, on pourra avoir tous ses détails(couleur, nombre de pieds,...).
# // Nous allons supposer que notre zoo contient quatre types d'animaux différents : des moutons,
# // loups, serpents et perroquets.
# // * Créez des classes pour chacun de ces
# // types d'animaux, de sorte que nous puissions imprimer chacun d'eux et obtenir un rapport sur leur couleur, leur espèce et
# // nombre de jambes.


# // Utiliser __name__ pour creer une variable name qui portera le nom de chaque classe.
# // Ajouter une documentation de la classe en utilisant docstring


# // Maintenant que nous avons créé des animaux, il est temps de les mettre en cage. Pour cet exercice, créez une classe Cage, 
# dans laquelle vous pouvez mettre un ou plusieurs animaux. Lorsque vous créez une nouvelle cage, vous lui attribuez un numéro
#  d'identification unique. (L'unicité
# // n'a pas besoin d'être imposé, mais cela vous aidera à faire la distinction entre les cages.)

# // Vous allez invoquer une methode **add_animals** sur la nouvelle cage, en passant un nombre quelconque d'animaux
# // qui sera mis dans la cage.

# // Vous définirez une méthode __repr__ afin que l'impression d'une cage n'imprime pas seulement l'ID de la cage, mais
#  également les details de chacun des animaux qu'elle contient.




# // Enfin, le moment est venu de créer notre objet Zoo. Il contiendra des objets en cage, et
# // ils contiendront à leur tour des animaux. Notre classe Zoo devra prendre en charge les éléments suivants
# // opérations :
# // * Étant donné un zoo z, nous devrions pouvoir imprimer toutes les
# // cages (avec leurs numéros d'identification) et les animaux à l'intérieur en appelant simplement print(z).

# // * Nous devrions pouvoir obtenir les animaux avec une couleur particulière en invoquant la
# // méthode z.animals_by_color. Par exemple, nous pouvons obtenir tous les animaux noirs en appelant z.animals_by_color('noir'). 
# Le résultat devrait être une liste
# // d'objets animaux.
# // * On devrait pouvoir obtenir les animaux avec un certain nombre de pattes en invoquant la méthode z.animals_by_legs. Par exemple,
#  nous pouvons obtenir tous les animaux à quatre pattes en appelant z.animals_by_legs(4). Le résultat devrait être une liste
# // d'objets animaux.
# // * Enfin, nous avons un donateur potentiel à notre zoo qui souhaite fournir des chaussettes à tous
# // des animaux. Ainsi, nous devons pouvoir invoquer z.number_of_legs() et
# // obtenez un décompte du nombre total de pattes pour tous les animaux de notre zoo.



# -----------------------------
# Classe mère Animal
# -----------------------------
class Animal():
    """
    Classe mère représentant un animal générique.
    Attributs :
        - espece : dérivée automatiquement du nom de la classe (Mouton, Loup, etc.)
        - couleur : couleur de l’animal (modifiable par setter)
        - nombre_de_pieds : nombre de pattes de l’animal (modifiable par setter)
    """

    def __init__(self, couleur, nombre_de_pieds):
        # Le nom de la classe devient l'espèce automatiquement
        self.__espece = self.__class__.__name__  
        # self.__class__.__name__ permet de recuperer le nom de la classe

        # Attributs protégés car on ne veut pas que l'utilisateur puisse les modifier
        #  directement donc on les met en double underscore
        # Ils sont modifiables uniquement via des setters ,donc les doubles underscore
        #  sont utilisés pour indiquer que ces attributs 
        # sont privés et ne doivent pas être accédés directement en dehors de la classe.
        self.__couleur = couleur
        self.__nombre_de_pieds = nombre_de_pieds

    # ---------- Getters ----------
    def getEspece(self):
        return self.__espece # on ne met pas de setter pour espece car on ne veut pas que l'utilisateur puisse modifier l'espece

    def getCouleur(self): # Couleur de l'animal donc modifiable
        return self.__couleur

    def getNombreDePieds(self):
        return self.__nombre_de_pieds

    # ---------- Setters ----------
    def setCouleur(self, couleur): # on peut changer la couleur avec un setter ici couleur est un parametre
        self.__couleur = couleur

    def setNombreDePieds(self, nombre_de_pieds):  # on peut changer le nombre de pattes avec un setter
        if nombre_de_pieds >= 0:  # on impose une regle : un animal ne peut pas avoir moins de 0 pattes
            self.__nombre_de_pieds = nombre_de_pieds

    # ---------- Affichage ----------
    def __str__(self):
        return f"Espèce: {self.__espece}, Couleur: {self.__couleur}, Nombre de pattes: {self.__nombre_de_pieds}"

#l'affichage est sous la forme d'une chaine de caractere comme ca on peut l'afficher facilement exemple print(animal)
    def __repr__(self):
        return f"{self.__espece}({self.__couleur}, {self.__nombre_de_pieds} pattes)"
# __repr__ permet de representer l'objet sous forme de chaine de caractere pour le debogage et ___str___ pour l'affichage informel


# -----------------------------
# Sous-classes spécifiques
# -----------------------------
class Loup(Animal):
    """Classe représentant un Loup (toujours 4 pattes)."""
    def __init__(self, couleur):    # on passe seulement la couleur car le nombre de pattes est fixe pour un loup
        super().__init__(couleur, 4)  # on appelle le constructeur de la classe mère Animal avec la couleur et le nombre de pattes fixe (4)

class Mouton(Animal):
    """Classe représentant un Mouton (toujours 4 pattes)."""
    def __init__(self, couleur):   # seulement la couleur est variable
        super().__init__(couleur, 4) # on fixe le nbre de pattes

class Serpent(Animal):
    """Classe représentant un Serpent (0 patte)."""
    def __init__(self, couleur):
        super().__init__(couleur, 0)

class Perroquet(Animal):
    """Classe représentant un Perroquet (2 pattes)."""
    def __init__(self, couleur): #on cree un constructeur qui prend en parametre la couleur car le nombre de pattes est fixe pour un perroquet
        super().__init__(couleur, 2) # on appelle le constructeur de la classe mere Animal avec la couleur et le nombre de pattes fixe (2)


# -----------------------------
# Classe Cage
# -----------------------------
class Cage():
    """
    Une cage contient un ou plusieurs animaux.
    Chaque cage a un identifiant unique (id_cage).
    """

    def __init__(self, id_cage):
        self.id_cage = id_cage
        self.animals = []  # liste d'animaux dans la cage

    def add_animals(self, *args):
        """Ajoute un ou plusieurs animaux dans la cage."""
        # args est une liste de tous les animaux passés en paramètre c'est-à-dire *args permet de passer un 
        # nombre variable d'arguments à
        #  la fonction
        for i in args:
            self.animals.append(i)

    def __repr__(self):
        # Affiche l'id de la cage + les animaux à l'intérieur
        # output est une chaine de caractere qui contient l'id de la cage et les animaux
        #.join permet de concatener les elements d'une liste en une seule chaine de caractere avec un separateur
        #\t est un caractere d'echappement qui permet de faire une tabulation
        output = f'Cage {self.id_cage}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.animals)
        return output


# -----------------------------
# Classe Zoo
# -----------------------------
class Zoo():
    """
    Le zoo contient plusieurs cages.
    On peut :
        - afficher tout le zoo
        - chercher des animaux par couleur
        - chercher par nombre de pattes
        - compter le total de pattes
    """

    def __init__(self): 
        self.cages = []

    def add_cages(self, *cages):  #*cages permet de passer un nombre variable d'arguments a la fonction add_cages
        """Ajoute une ou plusieurs cages au zoo."""
        for o in cages:
            self.cages.append(o)

    def __repr__(self):
        return '\n'.join(str(one_cage) for one_cage in self.cages) 
    # Affiche toutes les cages du zoo comme ça print(zoo) 
    # affiche tout le zoo la difference est que __str__ est utilisé pour l'affichage informel (en chaine de caractere
    #  de lobjet )et __repr__ cest 
    # la representation de lobjet pour l'affichage formel ou le débogage
    # Exemple avec __str__
    #print(m1)  
    # → Mouton (blanc, 4 pattes)

    # Exemple avec __repr__
    #print(repr(m2))  
    # → Animal('Mouton', 'noir', 4)

    def animals_par_couleur(self, couleur):
        """Retourne tous les animaux d’une couleur donnée."""
        return [one_animal for one_cage in self.cages 
                for one_animal in one_cage.animals 
                if one_animal.getCouleur() == couleur]
      #ici on fait une comprehension de liste pour recuperer les animaux de la couleur 
        # donnee en parametre puis on utilise la methode getCouleur pour recuperer la couleur de l'animal le principe est simple : 
        # on compare la couleur de l'animal avec la couleur donnee

    def animals_par_pieds(self, nombre_de_pieds):
        """Retourne tous les animaux avec un certain nombre de pattes."""
        return [one_animal for one_cage in self.cages  # ici on selectionne d'abord une cage puis on selectionne un animal dans cette cage
                for one_animal in one_cage.animals
                if one_animal.getNombreDePieds() == nombre_de_pieds] # on utilise la methode getNombreDePieds pour recuperer le nombre de pattes de l'animal
        # puis on compare le nombre de pattes de l'animal avec le nombre de pattes donnee en parametre donc getNombreDePieds est un getter
        #utilise pour recuperer le nombre de pattes de l'animal

    def nombre_de_pieds(self):
        """Retourne le nombre total de pattes de tous les animaux du zoo."""
        return sum(one_animal.getNombreDePieds() 
                   for one_cage in self.cages 
                   for one_animal in one_cage.animals)
     # ici on fait une comprehension de liste pour recuperer le nombre de pattes de chaque animal
        # puis on utilise la fonction sum pour faire la somme de tous les nombres de pattes


# -----------------------------
# Classe Crieur (polymorphisme)
# -----------------------------
class Crieur:
    """Interface : tout animal qui hérite de Crieur doit implémenter crier()."""
    def crier(self): 
         # ici on ne met pas de corps a la methode car c'est une interface .Une interface est une classe
                         # qui ne contient que des methodes abstraites cest a dire des methodes sans corps 
        pass


class MoutonCrieur(Mouton, Crieur):
    def crier(self):
        print("Je bêle gaiement")
    def beler(self):
        print("Bêêê")


class PerroquetCrieur(Perroquet, Crieur):
    def crier(self):
        print("Je croasse")
    def croasser(self):
        print("Croa")


# Classe générique pour faire crier un animal (duck typing)
class FaireCri:
    def __init__(self, animal):
        self.animal = animal
    def fairecrier(self):
        self.animal.crier()


# -----------------------------
# Exemple d’utilisation
# -----------------------------
if __name__ == "__main__":
    # Création d’animaux
    loup = Loup('noir')
    mouton = Mouton('blanc')
    serpent = Serpent('vert')
    perroquet = Perroquet('rouge')

    # Cages
    c1 = Cage(1)
    c1.add_animals(mouton)
    c2 = Cage(2)
    c2.add_animals(loup, serpent, perroquet)

    # Zoo
    z = Zoo()
    z.add_cages(c1, c2)
    print(z)  # Affiche tout le zoo

    print(z.animals_par_couleur('blanc'))   # recherche par couleur
    print(z.animals_par_pieds(4))           # recherche par nb de pattes
    print(z.nombre_de_pieds())              # total pattes
    # ✅ Utilisation du SETTER pour corriger une erreur
    print("Correction : le mouton a perdu une patte 😅")
    mouton.setNombreDePieds(3)
    print(z.nombre_de_pieds())              # total pattes
    print("le loup est devenu blanc")
    loup.setCouleur('blanc')
    print(z.animals_par_couleur('blanc'))   # recherche par couleur

    print("\n--- Polymorphisme avec Crieur ---")
    # Polymorphisme avec Crieur
    m = MoutonCrieur("blanc")
    p = PerroquetCrieur("vert")
    fc = FaireCri(m)
    fc.fairecrier()
    fc = FaireCri(p)
    fc.fairecrier()

    
# ## Repondez aux questions ci-dessous

# 1. Qu’est-ce qu’une **classe** ?
#une classe 


# 2. Qu’est-ce qu’un **objet** ?
# 3. Que contient le **corps** d’une classe ?
# 4. Comment **définit-on** une classe ?
# 5. Comment définir une **classe vide** ?
# 6. Qu’est-ce que `pass` ?
# 7. Comment **instancier** (invoquer) une classe ?
# 8. Comment **accéder à l’objet** créé par une classe ?
# 9. Si `class_name()` est une classe et que `a = class_name()`, `b = class_name()`, **a et b ont-ils la même adresse** ?
# 10. Dans la même idée, si l’on fait `a = b`, **a et b ont-ils la même adresse** ?
# 11. Comment vérifier si **deux variables pointent le même objet** ?
# 12. Qu’est-ce qu’une **méthode constructeur** ?
# 13. Que signifie `__init__(self)` ?
# 14. Comment **accéder à une propriété** d’une classe ?
# 15. Peut-on **modifier la valeur** d’une propriété de classe (d’instance) ?
# 16. Comment **définir la valeur initiale** d’une propriété de classe ?
# 17. Quel est l’**objectif du module `copy`** ?
# 18. Que sont les **méthodes dunder** (*double underscore*) ?
# 19. À quoi servent les méthodes **`__repr__`** et **`__str__`** ?
# 20. Qu’est-ce que la méthode **`__getattr__`** ?
# 21. Qu’est-ce que la **bibliothèque `tabulate`** ?
# 22. Comment utiliser **`len()`** dans une classe ? Quelles sont les **limitations** ?
# 23. Comment **implémenter la notation d’indexation** dans une classe ?
# 24. En quoi un **dataframe Pandas** diffère-t-il d’une simple **classe** ?
# 25. Qu’est-ce que la méthode **`__iter__`** dans une classe ?
# 26. Qu’est-ce que **`yield`** ?
# 27. Comment **résoudre le problème de renommage d’une colonne** dans une classe ?
# 28. Que sont les **méthodes statiques** ? Expliquez avec un exemple.
# 29. Qu’est-ce qu’une **méthode de classe** (*classmethod*) ? Expliquez avec un exemple.
# 30. Expliquez la **propriété d’héritage** d’une classe avec un exemple.
