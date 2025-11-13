liste=[1,2,3,4,5,6,33,12,46]
new=[]
print(liste)
maxi=max(liste)
print(maxi)
paire=[s for s in liste if s%2!=0]
mul=[(i,j) for i in liste for j in liste if i!=j and i+j==maxi]
print(paire)
print(mul)#affiche les couples de nombres dont la somme est
#égale au maximum de la liste
#la fonction lambda pour doubler un nombre

#la fonction lamda pour doubler un nombre
doubler = lambda x: x*2
print("calcul du double",doubler (5))
additionner = lambda a,b:a+b
print("sommer deux nombre",additionner(3,4))
