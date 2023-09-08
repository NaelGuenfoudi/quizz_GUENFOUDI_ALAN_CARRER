from tabulate import tabulate
import sys
sys.path.append('../')
from gestion_utilisateur import connexion_inscription as coins
import emoji
import theme as t
import mysql.connector

# Fonction pour afficher le menu
def afficher_menu():
    print(tabulate([["----- Interface Simple -----\n1. Connexion/inscription \n2. Choix du theme \n3. Option d'administration\n4. Lancer la partie\n5. Quitter"]], tablefmt='grid'))

# Fonctions pour les différentes options du menu
def option1():
    print("Voulez vous vous inscrire ou vous connectez ?")
    coins.afficher_co_ins()
def option2():
    print("Vous avez choisi de changer de theme")
    t.afficher_theme()

def option3():
    print("Vous avez choisi l'option 3") #Afficher uniquement si l'utilisateur est admin

def option4():
    print("C'est parti !")

# Boucle principale de l'interface
#print(tabulate([["--- Ludo ---"]], tablefmt='grid')) Permet d'afficher le pseudo du joueur
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
        option4()
        break
    elif choix == "5":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
