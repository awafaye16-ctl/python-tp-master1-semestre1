class carnivore:
    def __init__(self,v):
        self.consV =v
    def devorer(self):
        print("Il peut devorer",self.consV,"gramme (s) de viande par jour")
    
class herbivore:
    def __init__(self,h):
        self.consH = h
    def brouter(self):
        print("il peut brouter",self.consH,"gramme (s) d'herbe par jour")

class omnivore(carnivore,herbivore):
    def __init__(self,v,h):
        carnivore.__init__(self,v)
        herbivore.__init__(self,h)

porc = omnivore(1500,1750)
porc.brouter()
porc.devorer()

om = omnivore("lion","tigre")
omnivore.mro() #pour verifier les enceintres de homnivores
# l'heritage implicite

####################################
class Parent:
    def greet(self):
        print("Bonjours",+self.getName())

class Fils(Parent):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

c=Fils(Awa)        
#si on fait un double inderscore alors lobjet est prive 
#double inderscore est prive il a simplement changer le nom 
#pour recuperer un peut mettre un getter ou un setter
#polymorphysme 
# interface
#l'aggregation ou la compositon

class Point:
    def __init__(self,a,b):
        self.a=a
        self.ord=b
point1 = Point(1,3)
point2 = Point(2,4)

#herityge,polymorphisme   
class Rectangle():
    def __init__(self,p1,p2):
         self.p1=p1
         self.p2=p2
    
    def aire(self):
        larg = self.p2.y-self.p2.x
        long = self.p2.x - self.p1.x
        return long*larg

 # avec un polygone on a une liste de ponit
liste=[p1,p2,p3,p4,p5]
pentagone=polygone(liste)
 

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
    
    #les 
