from tabulate import tabulate
import emoji
import theme as t
import mysql.connector

# Fonction pour afficher le joueur actuel depuis la base de données MySQL
#def afficher_joueur_actuel():
#    try:
#        # Connexion à la base de données
#        conn = mysql.connector.connect(
#            host="localhost",     # Adresse du serveur MySQL
#            user="utilisateur",   # Nom d'utilisateur MySQL
#            password="motdepasse", # Mot de passe MySQL
#            database="ma_base_de_donnees" # Nom de la base de données
#        )
#
#        # Création d'un curseur
#        cursor = conn.cursor()
#
#        # Exécution d'une requête pour récupérer le joueur actuel
#        cursor.execute("SELECT joueur_actuel FROM table_joueurs WHERE id = 1") # Adapter la requête à votre base de données
#
#        # Récupération du résultat
#        joueur_actuel = cursor.fetchone()
#
#        if joueur_actuel:
#            print(f"Le joueur actuel est : {joueur_actuel[0]}")
#        else:
#            print("Aucun joueur actuel trouvé")
#
#    except mysql.connector.Error as e:
#        print(f"Erreur de base de données : {e}")
#    finally:
#        # Fermeture de la connexion à la base de données
#        conn.close()

# Utilisation de la fonction
#afficher_joueur_actuel() 


# Fonction pour afficher le menu
def afficher_menu():
    print(tabulate([["----- Interface Simple -----\n1. Choix du theme \n2. Option 2\n3. Option 3\n4. Quitter"]], tablefmt='grid'))

# Fonctions pour les différentes options du menu
def option1():
    print("Vous avez choisi de changer de theme")
    t.afficher_theme()

def option2():
    print("Vous avez choisi l'option 2")

def option3():
    print("Vous avez choisi l'option 3")

# Boucle principale de l'interface
print(tabulate([["--- Ludo ---"]], tablefmt='grid'))
while True:
    afficher_menu()
    choix = input("Choisissez une option : ")

    if choix == "1":
        option1()
        break
    elif choix == "2":
        option2()
        break
    elif choix == "3":
        option3()
        break
    elif choix == "4":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
