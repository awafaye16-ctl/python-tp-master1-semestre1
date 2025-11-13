
 ###########  EXO ZOO-CASE-ANIMEAUX    #######
#espece,couleurs

class animaux:
    def __init__(self,esp,patte):
        self.esp=esp
        self.patte=patte
        
class mouton(animaux):
    def __init__(self, esp, patte, couleur):
        super().__init__(esp, patte, couleur)
        self.couleur=couleur
    def get_Espece(self,esp):
        self.esp=esp
    def get_Patte(self,patte):
        self.patte=patte
    def get_Couleur(self,couleur):
        self.couleur=couleur
    

    def set_Espace(self,esp):
        self.esp=esp

    def set_patte(self,patte):
        self.patte=patte
    def set_Couleur(self,couleur):
        self.couleur=couleur
    



# En conclusion, cette lecture offre une compréhension fondamentale des objets et des classes en Python,
# concepts essentiels de la programmation orientée objet. Les classes servent de modèles pour la création 
# d'objets, encapsulant leurs attributs et méthodes. Les objets représentent des entités du monde réel et
# possèdent leur propre état et comportement. L'exemple de code structuré présenté dans cette lecture met'
# ' en évidence les éléments clés d'une classe, notamment ses attributs, le constructeur permettant 
# d'initialiser les attributs d'instance et les méthodes d'instance définissant les fonctionnalités '
# 'spécifiques à l'objet.
