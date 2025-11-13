# Liste simulée des logs comme dans l’image
logs = [
    "83.149.9.216 - - [17/May/2015:10:05:03 +0000] \"GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1\" 200 203023",
    "110.136.166.128 - - [17/May/2015:10:05:41 +0000] \"GET /favicon.ico HTTP/1.1\" 200 3638",
    "110.136.166.128 - - [17/May/2015:10:05:32 +0000] \"GET /images/jordan-80.png HTTP/1.1\" 200 6146"
]

# Créer un dictionnaire vide pour stocker le nombre de requêtes par adresse IP
Liste_adresse= {}

# Parcourir chaque ligne de log
for l in logs:
    ip = l.split()[0]  # L’adresse IP est toujours le premier élément de la ligne  
    # donc on utilise split() pour diviser la ligne en mots et on prend le premier mot
    # pour chaque adresse IP on verifie si elle est deja dans le dictionnaire Liste_adresse
    if ip in Liste_adresse:
        Liste_adresse[ip] += 1  # Si déjà présente, on incrémente
    else:
        Liste_adresse[ip] = 1   # Sinon, on initialise à 1

# Affichage du rapport
# ici on affiche chaque adresse IP avec le nombre de requêtes associées 
# items() permet d'obtenir les paires clé-valeur du dictionnaire
print("Rapport des requêtes par adresse IP :")
for ip, nbre in Liste_adresse.items():
    print(f"Adresse IP {ip} : {nbre}")


# Affichage du nombre total de requêtes
print("Nombre total de requêtes :", sum(Liste_adresse.values()))
# Affichage des adresses IP triées par ordre décroissant du nombre de requêtes
print("Adresses IP triées par ordre décroissant du nombre de requêtes :")
for ip, nbre in sorted(Liste_adresse.items(), key=lambda x: x[1], reverse=True):
    print(f"Adresse IP {ip} : {nbre}")
#plus simplement
# Affichage des adresses IP triées par ordre décroissant du nombre de requêtes
print("Adresses IP triées par ordre décroissant du nombre de requêtes :")
# utiliser enumerate pour afficher les index et les valeurs
for index, (ip, nbre) in enumerate(sorted(Liste_adresse.items(), key=lambda x: x[1], reverse=True)):
    print(f"Index {index} → Adresse IP {ip} : {nbre}")    
#sans utilser lamda


#ici les points essentiels sont :
# 1. Initialisation d’un dictionnaire vide pour compter les requêtes par IP.
# 2. Parcours de chaque ligne de log pour extraire l’adresse IP et mettre à jour le compteur.
# 3. Affichage du rapport final avec le total et le tri des adresses IP
# Ceci illustre l’utilisation pratique des dictionnaires en Python pour agréger et analyser des données structurées.
