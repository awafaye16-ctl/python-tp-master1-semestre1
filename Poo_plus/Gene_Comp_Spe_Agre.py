# <!-- 

# ## 1️⃣ Généralisation

# 👉 Définir une classe **plus générale** qui regroupe les éléments communs (attributs, méthodes) de plusieurs classes.
# ➡️ C’est une sorte de **factorisation**.

# ### Exemple en Python

# ```python
# class Mathematicien:
#     def __init__(self, nom, grade):
#         self.nom = nom
#         self.grade = grade

#     def travailler(self):
#         print(f"{self.nom} travaille sur un problème mathématique.")
# ```

# Ici, `Mathematicien` est une classe **générale** qui contient les attributs communs (`nom`, `grade`).

# ---

# ## 2️⃣ Spécialisation

# 👉 Créer une **classe dérivée** (héritage) à partir d’une classe générale, en l’adaptant à un cas particulier.
# ➡️ On ajoute des attributs/méthodes spécifiques.

# ### Exemple en Python

# ```python
# class Statistien(Mathematicien):  # spécialisation
#     def travailler(self):
#         print(f"{self.nom} analyse des données statistiques.")

# class Numericien(Mathematicien):  # spécialisation
#     def travailler(self):
#         print(f"{self.nom} résout des équations numériques.")
# ```

# ➡️ `Statistien` et `Numericien` **spécialisent** la classe `Mathematicien`.
# Ils héritent des attributs (`nom`, `grade`) mais redéfinissent `travailler`.

# ---

# ## 3️⃣ Composition

# 👉 Une classe est construite **à partir d’autres classes** (relation "A a un B").
# ➡️ Contrairement à l’héritage, la composition décrit une **relation de possession** plutôt qu’une relation "est un".

# ### Exemple en Python

# ```python
# class Ordinateur:
#     def __init__(self, marque):
#         self.marque = marque

#     def demarrer(self):
#         print(f"L'ordinateur {self.marque} démarre.")


# class Mathematicien:
#     def __init__(self, nom, grade, ordinateur):
#         self.nom = nom
#         self.grade = grade
#         self.ordinateur = ordinateur  # Composition : le mathématicien A un ordinateur

#     def travailler(self):
#         print(f"{self.nom} travaille avec son ordinateur {self.ordinateur.marque}.")
#         self.ordinateur.demarrer()
# ```

# ➡️ Ici, `Mathematicien` **possède** un `Ordinateur`.

# * Relation d’héritage → **est un** : `Statistien est un Mathematicien`.
# * Relation de composition → **a un** : `Mathematicien a un Ordinateur`.

# ---

# ## ⚖️ Différences clés

# | Concept            | Définition                                                  | Exemple relation                       |
# | ------------------ | ----------------------------------------------------------- | -------------------------------------- |
# | **Généralisation** | Créer une classe mère qui regroupe les éléments communs     | `Mathematicien`                        |
# | **Spécialisation** | Adapter une classe générale à un cas particulier (héritage) | `Statistien` hérite de `Mathematicien` |
# | **Composition**    | Une classe est constituée d’autres objets                   | `Mathematicien` a un `Ordinateur`      |

# ---

# 👉 En résumé :

# * **Généralisation** = abstraction commune.
# * **Spécialisation** = raffinement particulier (héritage).
# * **Composition** = construction par inclusion d’objets (has-a).
# Parfait 👍 tu touches ici un concept important en **modélisation orientée objet** : les relations entre classes.
# On distingue **généralisation/spécialisation**, **composition** et **agrégation**.

# ---

# ## 1. Généralisation / Spécialisation

# * **Généralisation** : remonter les attributs et méthodes communs dans une classe mère.
# * **Spécialisation** : créer des classes filles plus spécifiques qui héritent de la classe mère.

# 📌 Exemple en Python :

# ```python
# class Mathematicien:  # Classe générale
#     def __init__(self, nom, grade):
#         self.nom = nom
#         self.grade = grade

# class Statistien(Mathematicien):  # Spécialisation
#     def analyser_donnees(self):
#         return f"{self.nom} analyse les données statistiques."

# class Numericien(Mathematicien):  # Spécialisation
#     def simuler(self):
#         return f"{self.nom} fait une simulation numérique."
# ```

# 👉 Ici, `Mathematicien` est la **généralisation**.
# `Statistien` et `Numericien` sont des **spécialisations**.

# ---

# ## 2. Composition

# La **composition** est une relation *forte* entre deux classes :

# * Une classe **contient** une autre.
# * Si l’objet contenant est détruit, les objets contenus le sont aussi.

# 📌 Exemple :

# ```python
# class Moteur:
#     def __init__(self, puissance):
#         self.puissance = puissance

# class Voiture:
#     def __init__(self, marque, puissance_moteur):
#         self.marque = marque
#         self.moteur = Moteur(puissance_moteur)  # Composition forte

# ma_voiture = Voiture("Toyota", 120)
# ```

# 👉 Ici, **la voiture *possède* un moteur**.
# Si la `Voiture` est détruite, son `Moteur` est détruit aussi.
# On parle de **relation "fait partie de"** (*part-of*).

# ---

# ## 3. Agrégation

# L’**agrégation** est une relation *faible* :

# * Une classe **référence** une autre, mais sans la posséder totalement.
# * Les objets peuvent exister indépendamment.

# 📌 Exemple :

# ```python
# class Professeur:
#     def __init__(self, nom):
#         self.nom = nom

# class Universite:
#     def __init__(self, nom):
#         self.nom = nom
#         self.professeurs = []  # Agrégation

#     def ajouter_professeur(self, prof):
#         self.professeurs.append(prof)

# # Création indépendante
# prof1 = Professeur("Dr. Diop")
# prof2 = Professeur("Mme. Sow")

# # L'université agrège les professeurs
# ucad = Universite("UCAD")
# ucad.ajouter_professeur(prof1)
# ucad.ajouter_professeur(prof2)
# ```

# 👉 Ici, `Professeur` peut exister **sans** `Université`.
# L’université ne "possède" pas le professeur, elle l’agrège.
# On parle de **relation "a un"** (*has-a*).

# ---

# ## 🔑 Différences en résumé :

# * **Généralisation/Spécialisation** → Héritage (relation *est-un*).
# * **Composition** → Contenance forte (relation *fait partie de*).
# * **Agrégation** → Contenance faible (relation *a un*).

# ---

# Veux-tu que je te fasse un **schéma UML simple** pour comparer visuellement les trois (héritage, composition, agrégation) ? -->
