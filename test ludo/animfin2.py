import random
import time
import os
import emoji
import Cwin as win

# Fonction pour effacer l'écran (compatible avec Windows et Unix)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Création d'une classe pour les confettis
class Confetti:
    def __init__(self):
        self.x = random.randint(0, 39)
        self.y = random.randint(0, 9)
        self.color = random.choice(["\U0001F389"])

    def move(self):
        self.y += 1

# Liste de confettis
confettis = []

# Génération des confettis (augmenter le nombre pour plus de confettis)
for _ in range(100):  # Augmentez le nombre ici (par exemple, 200)
    confetti = Confetti()
    confettis.append(confetti)

# Boucle principale de l'animation
while True:
    clear_screen()

    # Créer une grille de 80x24 pour afficher les confettis
    grid = [[' ' for _ in range(40)] for _ in range(10)]

    # Mettre à jour la position des confettis
    for confetti in confettis:
        confetti.move()
        if confetti.y < 10:
            grid[confetti.y][confetti.x] = confetti.color

    # Afficher la grille
    for row in grid:
        print(''.join(row))

    # Vérifier si la position des confettis a dépassé la taille de la grille
    if all(confetti.y >= 24 for confetti in confettis):
        break  # Sortir de la boucle si tous les confettis sont tombés hors de la grille

    # Attendre un court moment avant de mettre à jour l'affichage
    time.sleep(0.1)

# Afficher la fonction win.win() à la fin
win.win()
