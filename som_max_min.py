# EXERCICE 1
# Ecrire de deux maniéres une fonction qui accepte n’importe quel nombre de
# nombres et retourne les données suivantes: moyenne, min, max, somme:
#  Une qui utilise les fonctions built-in de python
#  Une autre qui ecrit les codes necessaires

# Supprimer une plage d’elements d’une liste en utilisant le slicing
# 2. Tri de list:
#  Utliser sort pour trier une liste
#  Utiliser sorted pour trier une liste
#  Quelle difference notez-vous entre les deux ?
# 1. Utiliser la fonction enumerate avec une liste. Regarder son type de retour


# EXERCICE 2
# Avec Python, définir la liste suivante :
# liste = [3,2,9,5,7,8,1,6,0]
# 1. Triez puis affichez la liste
# 2. Ajoutez l’élément 4 à la liste puis affichez la liste
# 3. Renversez et affichez la liste
# 4. Affichez l’indice de l’élément 7
# 5. Enlevez l’élément 8 et affichez la liste
# 6. Affichez la sous liste du 2e au 3e élément
# 7. Affichez la sous liste du début au 4e élément
# 8. Affichez le dernier élément en utilisant un indiçages négatif



# Parfait 👍, tes exercices sont centrés sur la **manipulation de listes** et les **fonctions built-in de Python**. Je vais corriger et détailler les solutions de manière complète.

# ---

# # ✅ EXERCICE 1

# ### 🔹 Partie 1 : Fonction qui accepte **n’importe quel nombre de nombres**

# 👉 **Avec les fonctions built-in :**

# ```python
# def stats_builtin(*args):
#     """Retourne moyenne, min, max et somme en utilisant les fonctions intégrées."""
#     moyenne = sum(args) / len(args)
#     return {"moyenne": moyenne, "min": min(args), "max": max(args), "somme": sum(args)}

# # Exemple
# print(stats_builtin(2, 5, 7, 10))
# # → {'moyenne': 6.0, 'min': 2, 'max': 10, 'somme': 24}
# ```

# 👉 **En codant les calculs à la main :**

# ```python
# def stats_manual(*args):
#     """Retourne moyenne, min, max et somme sans fonctions intégrées."""
#     total = 0
#     minimum = args[0]
#     maximum = args[0]

#     for val in args:
#         total += val
#         if val < minimum:
#             minimum = val
#         if val > maximum:
#             maximum = val
    
#     moyenne = total / len(args)
#     return {"moyenne": moyenne, "min": minimum, "max": maximum, "somme": total}

# # Exemple
# print(stats_manual(2, 5, 7, 10))
# # → {'moyenne': 6.0, 'min': 2, 'max': 10, 'somme': 24}
# ```

# ---

# ### 🔹 Supprimer une plage d’éléments avec **slicing**

# ```python
# ma_liste = [1, 2, 3, 4, 5, 6, 7]
# # Supprimer les éléments d’indice 2 à 4 (exclus)
# del ma_liste[2:5]
# print(ma_liste)  
# # → [1, 2, 6, 7]
# ```

# ---

# ### 🔹 Tri d’une liste : `sort()` vs `sorted()`

# ```python
# liste = [5, 2, 9, 1]

# # Avec sort() → trie la liste en place (modifie l’originale)
# liste.sort()
# print("Avec sort():", liste)  
# # → [1, 2, 5, 9]

# # Avec sorted() → retourne une nouvelle liste (l’originale reste intacte)
# liste2 = [5, 2, 9, 1]
# nouvelle = sorted(liste2)
# print("Original:", liste2)   
# # → [5, 2, 9, 1]
# print("Avec sorted():", nouvelle)  
# # → [1, 2, 5, 9]
# ```

# 👉 **Différence** :

# * `list.sort()` → modifie directement la liste.
# * `sorted(liste)` → crée une nouvelle liste triée sans modifier l’originale.

# ---

# ### 🔹 Utiliser `enumerate`

# ```python
# animaux = ["chat", "chien", "oiseau"]
# for index, valeur in enumerate(animaux):
#     print(index, valeur)

# # → 0 chat
# # → 1 chien
# # → 2 oiseau

# print(type(enumerate(animaux)))  
# # → <class 'enumerate'>
# ```

# ---

# # ✅ EXERCICE 2

# ```python
# liste = [3, 2, 9, 5, 7, 8, 1, 6, 0]

# # 1. Trier et afficher
# liste.sort()
# print("Liste triée :", liste)  
# # → [0, 1, 2, 3, 5, 6, 7, 8, 9]

# # 2. Ajouter l’élément 4
# liste.append(4)
# print("Après ajout de 4 :", liste)

# # 3. Renverser la liste
# liste.reverse()
# print("Renversée :", liste)

# # 4. Indice de l’élément 7
# print("Indice de 7 :", liste.index(7))

# # 5. Enlever l’élément 8
# liste.remove(8)
# print("Après suppression de 8 :", liste)

# # 6. Sous-liste du 2e au 3e élément (indices 1 à 2)
# print("Sous-liste [2e-3e] :", liste[1:3])

# # 7. Sous-liste du début au 4e élément
# print("Sous-liste [début-4e] :", liste[:4])

# # 8. Dernier élément avec indice négatif
# print("Dernier élément :", liste[-1])
# ```

# ---

# ✅ Ici tu as :

# * Des **fonctions statistiques** (version built-in et manuelle).
# * La **suppression avec slicing**.
# * Le **tri** avec `sort` et `sorted` (et leur différence).
# * L’utilisation de **enumerate**.
# * Des manipulations classiques de **liste** (ajout, suppression, index, slicing, renversement).

# ---