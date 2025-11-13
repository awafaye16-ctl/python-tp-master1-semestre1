#affichage de variable

a=2
print(f"le type de a est",type(a))
b=2.5
print(type(b)) 
c=True
d="Hello guys !"
print("les valeurs entres sont",a,", ",b,", ",c,"et",d)
print(f"autre maniere pour afficher  a={a},b={b},c={c} et d={d} ")
print("la somme de",a,"et",b,"est",a+b)
print("le type de: hello guys est ",type(d))
z=a**2+b  #a chapeau 2
print(z)
"""     """
print("la valeur boolean de a=b est :",a==b)
print("le resultat booleen de la 1er partie est :",not  16/2**+10 != 15%8*2)
print("le resultat de la deuxieme partie est :",    
      0.5**-2/2*5>=10**2**(1/2))
print("le resultat booleen des deux est:",not  16/2**+10 != 15%8*2    and   0.5**-2/2*5>=10**2**(1/2))

print("-------creation de variable et affectation de valeurs")
A=3
B=7
A=B       #A=7
B=A+5     #B=7+5=12
C=A+B     #C=7+12
C=B-A     #C=12-7 =5

print("la valeur de A est: ",A,", B est :",B,", C est :",C)
print("---------------")
A=1
B=2
A=B
B=A
print(A," ",B)
print("echange de deux variables m et n")
m=2
n=5
x=m
m=n
n=x
print("la nouvelle valeur de m est :", m ,"et la nouvelle valeur de n est :",n)
print("------saisir et affiche------")
"""nom=input("saisir votre nom:")
print(f"votre nom est{nom}")
prenom=input("saisir votre prenom:")
print(f"votre prenom est:{prenom}")
age=input("saisir votre age:")
print(f"votre age est:{age}")
print(f"Bonjour Mlle:{prenom} {nom} votre ages est {age}")

###=----le double de ce nombre-----------------
nombre =int(input('saisir un nombre :'))
print("le double de ce nombre est :",nombre*2)"""

###--------la somme de deux nombre-----------
nombre1=int(input('saisir un nombre:'))
nombre2=int(input('saisir un autre nombre :'))
print("le somme de ",nombre1,"et",nombre2,"est egale a",nombre1+nombre2)

###----Structure conditionnelles--------
print("les structures conditionnelles permettent dexecuter un bloc de code uniquement si une condition est vraie")
age=int(input('saisir votre age'))
if age >=18:
    print('vous etes majeur')
elif age<18:    
    print("vous etes mineur")
else:
     print("vous etes jeune")

###------------if......elif......else
note = int(input("Donner une note :"))
if note >=90:
    print("Excellent")
elif note >=75:
    print("Vous etes Tres bien")
elif note >=50 :
    print("Passable")
else:
    print("vous avez echoue")

##------------------------

print("------Conditions imbriquees--------")
age=int(input("donner votre age :"))
if age >=18:
    permis = input("Avez vous un permis ? true/false :")
    if permis == "true":
        print("Vous pouvez conduire")
    else:
        print("Vous devez obtenir un permi")
else:
      print("Vous etes tres jeune pour conduire")

print("----------match case------------")
moy = float(input("Donnez votre moyenne : "))

if moy < 10:
    print("Ajourné")
elif 10 <= moy < 12:
    print("Passable")
elif 12 <= moy < 14:
    print("Assez bien")
elif 14 <= moy < 16:
    print("Bien")
elif 16 <= moy <= 19:
    print("Très bien")
elif 19 < moy <= 20:
    print("Excellent")
else:
    print("Mention inconnue")

print("_______________________________________")
moy = float(input("Donnez votre moyenne : "))

match moy:
    case _ if moy < 10:
        print("Ajourné")
    case _ if 10 <= moy < 12:
        print("Passable")
    case _ if 12 <= moy < 14:
        print("Assez bien")
    case _ if 14 <= moy < 16:
        print("Bien")
    case _ if 16 <= moy <= 19:
        print("Très bien")
    case _ if 19 < moy <= 20:
        print("Excellent")
    case _:
        print("Mention inconnue")
liste=[1,2,3,4,5,6,7,8,9]
print(liste)