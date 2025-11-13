
saisir = input("Veiller saisir une liste d'entiers séparés par des virgules : ")
liste = [int(x) for x in saisir.split(",")] # liste = [int(x) for x in saisir.split(",")]

print("Liste :", liste) #print("liste:",liste)
print("\nListe avec index :") #print(f"index {i})
for i in range(len(liste)):
    print(f"Index {i} : {liste[i]}")
somme = sum(liste) 
print("\nSomme des éléments :", somme) 
multiples_de_3 = [x for x in liste if x % 3 == 0]
print("Multiples de 3 :", multiples_de_3)
print("Maximum :", max(liste))


print("Minimum :", min(liste))

nb_pairs = len([x for x in liste if x % 2 == 0])
print("Nombre d'entiers pairs :", nb_pairs)

somme_impairs = sum([x for x in liste if x % 2 != 0])
print("Somme des impairs :", somme_impairs)

B=[]
for i in range(10):
    C=int(input("saisir un nombre"))
    B.append(C)

