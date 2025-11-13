import math  # On importe le module math pour avoir accès à pi, sqrt, exp, etc.

# ----------------------------
# Fonction qui calcule n! (factorielle exacte)
# ----------------------------
def facto(n):
    """
    Calcule récursivement la factorielle de n : n! = n × (n-1) × ... × 1
    """
    if n == 0 or n == 1:    # Cas de base : 0! = 1 et 1! = 1
        return 1
    else:
        return n * facto(n - 1)  # Appel récursif : n! = n × (n-1)!

# ----------------------------
# Fonction qui calcule l'approximation de Stirling
# ----------------------------
def stirling(n):
    """
    Approximation de Stirling : n! ≈ sqrt(2πn) × (n/e)^n
    """
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

# ----------------------------
# Fonction qui calcule l'écart relatif en pourcentage
# entre la factorielle exacte et Stirling
# ----------------------------
def ecart_relatif(n):
    """
    Calcule l'écart relatif en % entre la factorielle exacte et celle de Stirling.
    """
    exact = facto(n)             # Valeur exacte de n!
    approx = stirling(n)         # Valeur approchée par Stirling
    ecart = abs(exact - approx) / exact * 100  # Pourcentage d'écart relatif
    return ecart
print("Comparaison entre Factorielle et Stirling (n = 1 à 10) :")
for n in range(1, 11):
    e = ecart_relatif(n)  # On calcule l'écart relatif pour chaque n
    print(f"n = {n:2d}  →  Écart relatif = {e:.5f} %")  # Affichage formaté
print("\nRecherche de la première valeur de n où l'écart < 0.1% (n = 10 à 50) :")
seuil = 0.1  # Seuil de précision : 0.1%

for n in range(10, 51):  # On teste tous les n de 10 à 50
    e = ecart_relatif(n)
    print(f"n = {n:2d}  →  Écart relatif = {e:.5f} %")
    
    if e < seuil:
        print(f"\n✅ À partir de n = {n}, l'écart est inférieur à 0.1%")
        break  # On s’arrête dès qu’on atteint un écart inférieur au seuil

## 🧪 **Objectif du programme :**




## 🧾 Le code complet avec **commentaires pédagogiques** :


import math  # On importe le module math pour avoir accès à pi, sqrt, exp, etc.

# ----------------------------
# Fonction qui calcule n! (factorielle exacte)
# ----------------------------
def facto(n):
    """
    Calcule récursivement la factorielle de n : n! = n × (n-1) × ... × 1
    """
    if n == 0 or n == 1:    # Cas de base : 0! = 1 et 1! = 1
        return 1
    else:
        return n * facto(n - 1)  # Appel récursif : n! = n × (n-1)!

# ----------------------------
# Fonction qui calcule l'approximation de Stirling
# ----------------------------
def stirling(n):
    """
    Approximation de Stirling : n! ≈ sqrt(2πn) × (n/e)^n
    """
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

# ----------------------------
# Fonction qui calcule l'écart relatif en pourcentage
# entre la factorielle exacte et Stirling
# ----------------------------
def ecart_relatif(n):
    """
    Calcule l'écart relatif en % entre la factorielle exacte et celle de Stirling.
    """
    exact = facto(n)             # Valeur exacte de n!
    approx = stirling(n)         # Valeur approchée par Stirling
    ecart = abs(exact - approx) / exact * 100  # Pourcentage d'écart relatif
    return ecart


# ## 🔽 Étape 1 : Afficher l’écart pour $n \in [1, 10]$

# ```python
# print("Comparaison entre Factorielle et Stirling (n = 1 à 10) :")
# for n in range(1, 11):
#     e = ecart_relatif(n)  # On calcule l'écart relatif pour chaque n
#     print(f"n = {n:2d}  →  Écart relatif = {e:.5f} %")  # Affichage formaté
# ```

# ### 💡 Pourquoi ?

# * Ce bloc nous montre à **quel point Stirling est précis** pour les petites valeurs de $n$.
# * En pratique, on constate que plus $n$ est petit, plus l’erreur est grande.

# ---

# ## 🔽 Étape 2 : Trouver **à partir de quelle valeur de $n$** l’écart devient < 0.1 %

# ```python
# print("\nRecherche de la première valeur de n où l'écart < 0.1% (n = 10 à 50) :")
# seuil = 0.1  # Seuil de précision : 0.1%

# for n in range(10, 51):  # On teste tous les n de 10 à 50
#     e = ecart_relatif(n)
#     print(f"n = {n:2d}  →  Écart relatif = {e:.5f} %")
    
#     if e < seuil:
#         print(f"\n✅ À partir de n = {n}, l'écart est inférieur à 0.1%")
#         break  # On s’arrête dès qu’on atteint un écart inférieur au seuil
# ```

# ### 💡 Pourquoi ?

# * On cherche ici **à valider la précision de Stirling** pour les grands $n$.
# * On vérifie à **partir de quelle valeur** l’approximation devient **suffisamment bonne** pour une utilisation pratique.

# ---

# ## ✅ Résumé des principes utilisés :

# | Élément                             | Principe                | Raison d’utilisation                                 |
# | ----------------------------------- | ----------------------- | ---------------------------------------------------- |
# | `factorielle`                       | Définition exacte $n!$  | Base de comparaison                                  |
# | `stirling(n)`                       | Formule d’approximation | Réduit le calcul pour grands $n$                     |
# | `abs(exact - approx) / exact * 100` | Écart relatif           | Mesure la précision en %                             |
# | `for n in range(...)`               | Parcours d’entiers      | Tester tous les cas                                  |
# | `break`                             | Contrôle de boucle      | Arrêter à la première valeur satisfaisant le critère |

# ---
# Très bonne question, Awa. Poser **l’objectif réel** d’un exercice est **essentiel** pour aller au-delà de la mécanique et comprendre **pourquoi on fait ce qu’on fait**.

# ---

# ## 🎯 Objectif de l'exercice

# Cet exercice a **deux objectifs principaux** :

# ---

# ### 🔹 1. **Objectif mathématique : Comprendre la formule de Stirling**

# * **Stirling** donne une **approximation de la factorielle** $n!$, surtout utile quand $n$ est **grand**.
# * La factorielle $n!$ croît **extrêmement vite** (exponentiellement), ce qui rend son calcul exact difficile pour de grands $n$ (ex : $100!$).

# 👉 La **formule de Stirling** :

# $$
# n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n
# $$

# te permet d’**éviter le calcul exact** de la factorielle, en la remplaçant par une **formule fermée** plus simple et plus rapide à évaluer.

# #### ✅ Ce qu’on cherche à vérifier :

# * À partir de **quelle valeur de $n$** cette approximation est **suffisamment précise** (ex. : moins de 0,1 % d’erreur).

# ---

# ### 🔹 2. **Objectif algorithmique : maîtriser le calcul, la programmation et la précision**

# Tu dois :

# * Écrire une fonction de **calcul exact** (factorielle),
# * Écrire la fonction d’**approximation** (Stirling),
# * Comparer les deux avec un **écart relatif en %**,
# * Et déterminer jusqu’où l’approximation est **fiable**.

# 👉 C’est un **exercice de modélisation et d’analyse numérique** :
# Quand une approximation est-elle **acceptable** ? Comment **quantifier l’erreur** ?

# ---

# ## 📌 Pourquoi utilise-t-on Stirling ?

# ### ⚙️ En pratique :

# * On **n’a pas toujours besoin de la valeur exacte** de $n!$, surtout si $n$ est grand.
# * Stirling est très utile :

#   * En **probabilités** (ex : loi binomiale, loi de Poisson)
#   * En **analyse asymptotique** (limites, comportements à l’infini)
#   * En **complexité algorithmique** (analyse de l’ordre de grandeur)
#   * En **statistiques** (formules liées aux combinaisons ou aux entropies)

# ---

# ## 🔍 Exemple concret d’utilisation :

# ### ➤ Loi binomiale :

# $$
# P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
# $$

# Quand $n$ est grand, calculer $\binom{n}{k}$ exactement est **trop coûteux**
# → On remplace les factoriels avec **Stirling**.

# ---

# ## ✅ Résumé

# | Élément             | Objectif                                          |
# | ------------------- | ------------------------------------------------- |
# | Formule de Stirling | Approximée rapide de $n!$ pour grands $n$         |
# | Écart relatif       | Mesurer la précision de l’approximation           |
# | Programmation       | Implémenter les formules et visualiser les écarts |
# | Utilité             | Probabilités, analyse, statistiques, complexité   |

# ---

# Souhaites-tu un exemple d’application **concrète en probabilités**, ou une démonstration plus avancée de la formule de Stirling ?
# ```python