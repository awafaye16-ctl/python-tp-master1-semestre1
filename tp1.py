B=('awa','pouye','wert',3,3,3)

print(B[1:3]) #affiche le 2e et 3e
print(B[-2:]) #affichiche les 2 derniers
 
for i in range (len(B)):
    print(B[i])


#l'indice negatif commence par -long du tuple
print("de la groite vers la droite")  
for i in range(1,len (B)+1):
    print(B[-i])    

#Pour creer une matrice on peut mettre tuple de tuple
t=((12,13),(12,13),(12,13),("test","tete",6),(8,4,5))    
print(6 in t[1] )#true or false   

## QUELQUES FONCTIONS ESSENTIELLES
import collections
c=collections.Counter(t) # Counter({(12, 13): 1, ('test', 'tete', 6): 1, (8, 4, 5): 1})
print(c)
d=range(2,1000,100) # start stop step
print(list(d))
for i in d:
    print(i)
#del et pop avec pop on peut recuperer lelement 
#Index recherche un element a lindice donnee
#remove supprime l'element par valeur
l=[2,3,4,4,4]
l1=l.remove(4)
print(l) #Supprime le 1er 4
for i in range(len(l)):  #incdice si tu veux utiliser pop
    if l[i]==4:
        l.pop(i)
print(l)
## refactory consiste a mettre de la qualite du code 
#optimiser le code processeur(puissance de calcul) et memoire 