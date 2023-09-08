import time

# Fonction pour afficher les vies
def afficher_vies(nb_vies):
    cœur = "\u2764\ufe0f"  # Code Unicode pour le cœur
    cœur_brisé = "\U0001F494"  # Code Unicode pour le cœur brisé

    while nb_vies >= 0:
        vies = cœur * nb_vies
        print("\r" + vies + cœur_brisé * (3 - nb_vies), end='')
        time.sleep(1)  # Attendre 1 seconde entre chaque transition
        nb_vies -= 1

    print()

    if nb_vies < 0:
        print("You lose")

# Utilisation de la fonction pour afficher 3 vies
afficher_vies(3)
