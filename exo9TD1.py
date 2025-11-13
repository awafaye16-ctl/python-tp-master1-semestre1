# Séquence donnée
sequence = "ACCGXXCXXGTATTGGATXTGT"
# Définir les bases d'ADN valides
bases_valides = ['A', 'C', 'G', 'T']
# Créer un dictionnaire pour compter les bases
compteur = {base: 0 for base in bases_valides} 
# initialisation à 0 par l'utilisation de la comprehension de dictionnaire
#base represent le caractere A,C,G ou T on fait donc une boucle pour chaque caractere dans bases_valides
# la comprehension de dictionnaire permet de creer un dictionnaire 
# avec chaque base comme clé et 0 comme valeur

# Compter le total de bases valides
total = 0
# Parcourir la séquence caractère par caractère
# b represent le caractere A,C,G ou T dans la sequence on compte chaque caractere si il est dans bases_valides
# et on incrémente le compteur correspondant
for b in sequence:
    if b in bases_valides:
        compteur[b] += 1
        total += 1

# Afficher les résultats
# base represent le caractere A,C,G ou T on verifie chaque caractere de la sequence si il est dans bases_valides
print("Distribution des bases (valeurs et pourcentage) :\n")
for base in bases_valides:
    nombre = compteur[base]
    pourcentage = (nombre / total) * 100 if total > 0 else 0
    print(f"{base} {nombre} - {pourcentage:.2f} %")
# ici le .2f permet d'afficher le pourcentage avec 2 décimales
# les points essentiels sont :
# 1. Initialisation du compteur avec une compréhension de dictionnaire.
# 2. Utilisation d'une boucle pour parcourir la séquence et compter les bases.
# 3. Calcul et affichage du pourcentage de chaque base.

