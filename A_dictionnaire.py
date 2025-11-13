# Création d’un dictionnaire avec des mots de la langue française comme clés et leur traduction 
# imaginaire comme valeurs
# un dictionnaire est une collection non ordonnée de paires clé-valeur
# chaque clé doit être unique et immuable (string, number, tuple immuable)
dictionnaire = {
    "bonjour": "hello",
    "maison": "house",
    "chat": "cat"
}
# POUR CONVERTIRE EN JSON
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)

# On peut aussi faire l’inverse avec json.loads() (charger une string JSON → objet Python) :
# z = json.loads(y)   # transforme la chaîne JSON en dict Python
# print(z["name"])    # John
# Donc :
# dumps = Python → JSON string
# loads = JSON string → Python


# Affichage de tous les éléments (paires clé-valeur) du dictionnaire
print("Contenu initial du dictionnaire :")
print(dictionnaire.items())  # d.items() retourne un objet dict_items (liste de tuples)
#laffichage sera ainsi bonjour: hello, maison: house, chat: cat

# Accès à une cle du dictionnaire par sa valeur 
print("\nTraduction de 'bonjour' : ", dictionnaire["bonjour"])
# Accès direct à la valeur associée à la clé "bonjour"
# Utilisation de .get() pour obtenir la valeur associée à une clé sans générer d'erreur si la clé n'existe pas
valeur = dictionnaire.get("chat")
print(f"\nTraduction de 'chat' : {valeur}")

# Tentative d'accès à une clé inexistante avec get (renvoie None sans erreur)
print("Traduction de 'chien' : ", dictionnaire.get("chien"))  # Ne lève pas d'erreur

# Tentative d'accès à une clé inexistante avec get (renvoie une valeur par défaut)
# Affichage de toutes les clés
print("\nClés présentes dans le dictionnaire :")
print(dictionnaire.keys())

# Affichage de toutes les valeurs
print("\nValeurs présentes dans le dictionnaire :")
print(dictionnaire.values())

# Mise à jour du dictionnaire avec de nouveaux mots
dictionnaire.update({
    "chien": "dog",
    "voiture": "car"
})
print("\nDictionnaire après ajout de nouveaux mots :",dictionnaire)
print(dictionnaire)
#donc update() permet d'ajouter ou de modifier des paires clé-valeur
# update fait 2 choses en meme temps :
# 1. Si la clé existe, elle est mise à jour avec la nouvelle valeur.
# 2. Si la clé n'existe pas, elle est ajoutée avec la valeur spécifiée.


# Création d’un nouveau dictionnaire avec des clés données, toutes associées à la même valeur
cles = ['pomme', 'banane', 'poire'] # liste de clés
# On peut utiliser dict.fromkeys() pour créer un dictionnaire avec des clés spécifiques
valeur_par_defaut = 'fruit'

nouveau_dictionnaire = dict.fromkeys(cles, valeur_par_defaut)
print("\nDictionnaire créé avec fromkeys :")
#dict ici represente le type dictionnaire car fromkeys est une methode de la classe dict
print(nouveau_dictionnaire) # affichera : {'pomme': 'fruit', 'banane': 'fruit', 'poire': 'fruit'}

print({'pomme': 'fruit', 'banane': 'fruit', 'poire': 'fruit'})

# ici on a un dictionnaire avec des clés spécifiques,
#  toutes initialisées à la même valeur 'fruit'
#donc fromkeys permet de créer un dictionnaire avec des clés spécifiques,
#  toutes initialisées à la même valeur

# Suppression d’un élément par sa clé avec pop()
# mot_supprime = dictionnaire.pop("chien")
print(f"\nSuppression de la clé 'chien', valeur supprimée : ",dictionnaire.pop("chien"))
#print("Dictionnaire après suppression de 'chien' :",mot_supprime)
print(dictionnaire)



#popitem() supprime et retourne une paire clé-valeur arbitraire (la dernière insérée dans les versions récentes de Python)
# Suppression du dernier élément  avec popitem()
derniere_entree = dictionnaire.popitem()
print(f"\nDernier élément supprimé avec popitem : {derniere_entree}")
print("Dictionnaire après suppression du dernier élément :")
print(dictionnaire)

print("touts les etemets du dictionnaire",dictionnaire.items())
print("les cles du dictionnaire",dictionnaire.keys())
print("les valeurs du dictionnaire",dictionnaire.values())
for i in dictionnaire:
  #for i in dictionnaire.keys():
    print("affichons les valeurs des dictionnaire",dictionnaire.values)
    print(f"clee{i} et valeur {dictionnaire[i]}")


# Vider complètement le dictionnaire 
dictionnaire.clear()

print("\nDictionnaire vidé avec clear :")

print(dictionnaire)
# affichage par comprehension de dictionnaire
dictionnaire_comp = {mot: mot[::-1] for mot in ['pomme', 'banane', 'poire']}
print("\nDictionnaire créé par compréhension de dictionnaire :")
print(dictionnaire_comp)# ici on crée un dictionnaire où chaque mot est la clé en commencant par sa valeur inversée
#comme par exemple 'pomme' devient 'emmop'

#les points essentiels sont :
# 1. Création et manipulation de dictionnaires en Python.
# 2. Accès aux valeurs par leur clé.
# 3. Méthodes courantes : keys(), values(), items(), get(), update(), pop(), etc.
# 4. Gestion des erreurs potentielles lors de l'accès aux clés.
# 5. Utilisation de compréhensions de dictionnaire pour des opérations concises.
# Ceci illustre l'utilisation pratique des dictionnaires en Python pour stocker et manipuler des paires clé-valeur.