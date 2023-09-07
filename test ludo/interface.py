from tabulate import tabulate

# Fonction pour afficher le menu
def afficher_menu():
    print(tabulate([["----- Interface Simple -----\n1. Option 1\n2. Option 2\n3. Option 3\n4. Quitter"]], tablefmt='grid'))

# Fonctions pour les différentes options du menu
def option1():
    print("Vous avez choisi l'option 1")

def option2():
    print("Vous avez choisi l'option 2")

def option3():
    print("Vous avez choisi l'option 3")

# Boucle principale de l'interface
while True:
    afficher_menu()
    choix = input("Choisissez une option : ")

    if choix == "1":
        option1()
    elif choix == "2":
        option2()
    elif choix == "3":
        option3()
    elif choix == "4":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
