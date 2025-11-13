###########  EXO ZOO-CASE-ANIMAUX    #######

class Animal:
    """Classe de base représentant un animal générique"""
    def __init__(self, espece, nb_pattes):
        self._espece = espece        # attributs protégés (encapsulation)
        self._nb_pattes = nb_pattes

    # --- Getters ---
    def get_espece(self):
        return self._espece

    def get_nb_pattes(self):
        return self._nb_pattes

    # --- Setters ---
    def set_espece(self, espece):
        self._espece = espece

    def set_nb_pattes(self, nb_pattes):
        if nb_pattes >= 0:
            self._nb_pattes = nb_pattes
        else:
            print("Erreur : le nombre de pattes doit être positif !")

    # --- Méthodes génériques ---
    def manger(self):
        print(f"Le {self._espece} mange.") #ici self._espece 

    def dormir(self):
        print(f"Le {self._espece} dort.")


# -------------------------------------------------------
# Classe dérivée : Mouton (hérite de Animal)
# -------------------------------------------------------
class Mouton(Animal):
    """Classe représentant un mouton, héritant de la classe Animal"""
    def __init__(self, couleur):
        super().__init__("Mouton", 4)  # héritage : un mouton a 4 pattes
        self._couleur = couleur

    # --- Getters / Setters ---
    def get_couleur(self):
        return self._couleur

    def set_couleur(self, couleur):
        self._couleur = couleur

    # --- Méthodes spécifiques au mouton ---
    def manger(self):
        print(f"Le {self._espece} mange de l'herbe.")

    def dormir(self):
        print(f"Le {self._espece} dort dans la bergerie.")

    def bleat(self):
        print(f"Le {self._espece} bêle doucement 🐑.")


# -------------------------------------------------------
# Classe Zoo : composition (contient plusieurs animaux)
# -------------------------------------------------------
class Zoo:
    """Classe représentant un zoo contenant plusieurs animaux"""
    def __init__(self, nom):
        self.nom = nom
        self.animaux = []

    def ajouter_animal(self, animal):
        """Ajoute un animal au zoo"""
        self.animaux.append(animal)

    def afficher_animaux(self):
        """Affiche tous les animaux du zoo"""
        print(f"\n=== {self.nom} ===")
        for a in self.animaux:
            print(f"Espèce : {a.get_espece()}, Couleur : {getattr(a, '_couleur', 'N/A')}, Pattes : {a.get_nb_pattes()}")


# -------------------------------------------------------
# Exemple d’utilisation
# -------------------------------------------------------

mouton1 = Mouton("blanc")
mouton2 = Mouton("noir")

zoo1 = Zoo("Zoo de Dakar")
zoo1.ajouter_animal(mouton1)
zoo1.ajouter_animal(mouton2)

zoo1.afficher_animaux()

# Actions spécifiques
mouton1.manger()
mouton1.dormir()
mouton1.bleat()

# Exemple d'utilisation du setter
print("\nChangement de couleur du mouton 2...")
mouton2.set_couleur("gris")
zoo1.afficher_animaux()
