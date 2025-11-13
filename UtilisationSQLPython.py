# Importation des bibliothéques nécessaires pour la connexion à MySQL
import mysql.connector # connecter python à mysql
from mysql.connector import errorcode # structurer le code et de filtrer les erreurs que pourrait nous ramener mysql


# Connexion à la base de données
config = {
    'user': 'root',
    'password': 'kostakorto', 
    'host': '127.0.0.1',
    'database': 'cinema',
    'raise_on_warnings': True
}

# Capturer des erreurs de connection
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("L'utilisateur ou le mot de passe n'est pas correct")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas")
    else:
        print("Erreur non gérée:", err)
    exit()

section = 1  # Modifiez cette valeur selon la section que vous souhaitez exécuter

#### Sélection/Afficher des informations de la BD ###
if section == 1:
    print("Affichage des informations")

    cursorSel = cnx.cursor() 
    selectAction = ("SELECT nom FROM roman WHERE nom LIKE %s") 
    selectValue = ('%' + "robot" + '%',) 
    cursorSel.execute(selectAction, selectValue)
    resultSelect = cursorSel.fetchall() 

    for i in resultSelect: 
        print(i[0])  
    cursorSel.close()
    



### Insertion d'une nouvelle entrée ###
if section == 2:
    # Insertion de la série Hunger Games
    data_serie = {   
        'codeSerie': 4,
        'nomSerie': "Hunger Games",
    }
    cursorInsert = cnx.cursor() 

    # requête classique pour ajouter des éléments dans la BD
    add_serie = ("INSERT INTO serie "
                "(code_serie, nom_serie) "
                "VALUES (%(codeSerie)s, %(nomSerie)s)") 
    

    cursorInsert.execute(add_serie, data_serie) 
    print(cursorInsert.rowcount, "séries insérées") 

    # liste des romans associés à la série Hunger Games
    romans = [
        "Hunger Games",
        "L'embrasement",
        "La révolte"]

    add_roman = ("INSERT INTO roman "
                "(code_ISBN, nom, auteur, annee, prix, code_serie) " 
                "VALUES (%(codeISBN)s, %(nomRoman)s, %(auteurRoman)s, %(anneeRoman)s, %(prixRoman)s, %(codeSerie)s)")
    isbn = 13
    for r in romans:
        data_roman = {
            'codeISBN': isbn,
            'nomRoman': r,
            'auteurRoman': 'Suzanne Collins',
            'anneeRoman': 2015,
            'prixRoman': 7.95,
            'codeSerie': 4,
        }

        cursorInsert.execute(add_roman, data_roman) 
        print(cursorInsert.rowcount, "romans insérés")

        isbn += 1

    cnx.commit()  
    cursorInsert.close() 

### Mise à jour de la BD ###
if section == 3:
    print("Mise à jour des informations")
    cursorUpdate = cnx.cursor()

    # Mettre à jour le nom de l'auteur Suzanne Collins par Suzanne C.
    update_query = "UPDATE roman SET auteur = %s WHERE auteur = %s"
    update_data = ('Suzanne Collins', 'Suzanne C.')  # par exemple

    cursorUpdate.execute(update_query, update_data)
    print(cursorUpdate.rowcount, "ligne(s) mise(s) à jour.")

    cnx.commit()
    cursorUpdate.close()


### Suppression d'informations de la BD ###
if section == 4:
    print("Suppression d'informations")
    cursorDel = cnx.cursor()
    deleteRoman = "DELETE FROM roman WHERE nom = %s"
    dataRoman = ('Neverwhere',)

    cursorDel.execute(deleteRoman, dataRoman)
    cnx.commit()

    print(cursorDel.rowcount, "romans supprimés")

    
    cnx.commit()
    cursorDel.close()

# Fermeture de la connexion
cnx.close()




