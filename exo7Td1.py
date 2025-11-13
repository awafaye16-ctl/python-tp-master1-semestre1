for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Séquence d'origine contenant des lettres valides (A, C, T, G) et invalides (X)
sequence = 'ACCGXXCXXGTTACTGGGCXTTGT'

# Étape 1 : Séparation des séquences par les caractères invalides (X)
# On utilise split() pour découper la chaîne sur chaque 'X'
sous_sequences = sequence.split('X') # comme ici ACCG, C, GTT, ACTGGGC, TTGT

# Étape 2 : Filtrer uniquement les séquences qui contiennent A, C, T ou G (et non vides)
nucleotides_valides = ['A', 'C', 'T', 'G']
sequences_valides = []

# On parcourt les sous-séquences et on garde celles qui sont valides
for s in sous_sequences:
    if all(c in nucleotides_valides for c in s) and s != '': #ici on verifie si chaque caractere de s est dans nucleotides_valides
        sequences_valides.append(s)

# Étape 3 : Trier les séquences valides par ordre décroissant de longueur
sequences_triees = sorted(sequences_valides, key=len, reverse=True)

# Affichage final
print("Séquences valides triées par longueur décroissante :")
print(sequences_triees)
S = {1, 2, 3, 4, 5} 
print("Set S :", S)


# Ici, on a utilisé les fonctions de chaîne de caractères (split), les compréhensions de liste (all) et la fonction sorted avec un critère personnalisé (key=len) pour trier les séquences.
# Les points clés sont :
# 1. Découpage de la séquence initiale en sous-séquences.
# 2. Filtrage des sous-séquences pour ne garder que celles composées de lettres valides.
# 3. Tri des séquences valides par longueur décroissante.
# Ceci illustre l'utilisation pratique des chaînes de caractères, des listes et des fonctions intégrées en Python pour manipuler et analyser des données textuelles.
# Un set contient des éléments non ordonnés, uniques et non mutables (pas de liste ou dict dedans)

