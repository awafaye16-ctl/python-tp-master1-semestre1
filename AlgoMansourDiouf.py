# On commence notre programme

# ----------------------------
# 1. Entrer les informations de base
# ----------------------------

salaire_base = float(input("Entrez le salaire de base : "))
prime_technicite = float(input("Entrez la prime de technicité : "))
prime_transport = float(input("Entrez la prime de transport : "))
prime_enfant = float(input("Entrez la prime pour un enfant : "))
nombre_enfants = int(input("Entrez le nombre d'enfants : "))
jours_travailles = int(input("Entrez le nombre de jours travaillés (max 26) : "))

# ----------------------------
# 2. Calcul de la prime des enfants
# ----------------------------
prime_des_enfants = prime_enfant * nombre_enfants

# ----------------------------
# 3. Calcul du taux de travail
# ----------------------------
taux_travail = jours_travailles / 26

# ----------------------------
# 4. Calcul du salaire brut
# ----------------------------
salaire_brut = (salaire_base + prime_technicite + prime_transport + prime_des_enfants) * taux_travail

# ----------------------------
# 5. Calcul de l'impôt (2%) et de la CNSS (26,5%)
# ----------------------------
taux_impot = 0.02     # 2% en décimal
taux_cnss = 0.265     # 26,5% en décimal

valeur_impot = taux_impot * salaire_brut
valeur_cnss = taux_cnss * salaire_brut

# ----------------------------
# 6. Calcul du salaire net
# ----------------------------
salaire_net = salaire_brut - valeur_impot - valeur_cnss

# ----------------------------
# 7. Affichage des résultats
# ----------------------------
print("\n--- Résultats ---")
print("Salaire brut :", round(salaire_brut, 2), "FCFA")
print("Valeur de l'impôt :", round(valeur_impot, 2), "FCFA")
print("Valeur de la CNSS :", round(valeur_cnss, 2), "FCFA")
print("Salaire net :", round(salaire_net, 2), "FCFA")



Mansour DIOUF
12:35
IDE Pycharm
Installer Python
Version Community
Abdoul Salam Diallo
12:39
# Demande des entrées utilisateur
salaire_base = float(input("Entrez le salaire de base : "))
jours_travailles = int(input("Entrez le nombre de jours travaillés : "))
nombre_enfants = int(input("Entrez le nombre d’enfants : "))
prime_technicite = float(input("Entrez la prime de technicité : "))
prime_transport = float(input("Entrez la prime de transport : "))
prime_enfant = float(input("Entrez le montant de la prime par enfant : "))

# Calcul des valeurs
taux_travail = jours_travailles / 26

# Calcul des valeurs
taux_travail = jours_travailles / 26
prime_enfants = prime_enfant * nombre_enfants
salaire_brut = (salaire_base + prime_technicite + prime_transport + prime_enfants) * taux_travail
Abdoul Salam Diallo
12:40
# Calcul des taxes
impot = 0.02 * salaire_brut
cnss = 0.265 * salaire_brut

# Calcul du salaire net
salaire_net = salaire_brut - impot - cnss
# Affichage du résultat
print(f"Le salaire net est : {salaire_net:.2f} FCFA")
print(f"prime_enfants est : {prime_enfants}")
print(f"taux_travailt est : {taux_travail}")
print(f"salaire_brut est : {salaire_brut}")
print(f"L'impot  est : {impot}")
print(f"Le cnss est : {cnss}")