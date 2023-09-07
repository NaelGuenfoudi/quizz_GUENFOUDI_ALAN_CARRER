import random
import time
import os
import emoji

# Fonction pour effacer l'écran (compatible avec Windows et Unix)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Création d'une classe pour les confettis
class Confetti:
    def __init__(self):
        self.x = random.randint(0, 79)
        self.y = random.randint(0, 23)
        self.color = random.choice(["\U0001F389"])

    def move(self):
        self.y += 1

# Liste de confettis
confettis = []

# Génération des confettis (augmenter le nombre pour plus de confettis)
for _ in range(200):  # Augmentez le nombre ici (par exemple, 200)
    confetti = Confetti()
    confettis.append(confetti)

# Boucle principale de l'animation
while True:
    clear_screen()

    # Créer une grille de 80x24 pour afficher les confettis
    grid = [[' ' for _ in range(100)] for _ in range(24)]

    # Mettre à jour la position des confettis
    for confetti in confettis:
        confetti.move()
        if confetti.y < 24:
            grid[confetti.y][confetti.x] = confetti.color

    # Afficher la grille
    for row in grid:
        print(''.join(row))

    # Attendre un court moment avant de mettre à jour l'affichage
    time.sleep(0.1)
