import turtle
import random

# Configuration de la fenêtre
screen = turtle.Screen()
screen.title("Animation de confettis")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

# Création d'une classe pour les confettis
class Confetti(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        self.penup()
        self.speed(0)
        self.turtlesize(stretch_wid=0.2, stretch_len=0.2)
        self.goto(random.randint(-400, 400), random.randint(-300, 300))
        self.setheading(random.randint(0, 359))
        self.gravity = 0.1

    def move(self):
        self.sety(self.ycor() - self.gravity)
        self.gravity += 0.1

# Liste de confettis
confettis = []

# Génération des confettis
for _ in range(100):
    confetti = Confetti()
    confettis.append(confetti)

# Boucle principale de l'animation
while True:
    screen.update()

    # Animation des confettis
    for confetti in confettis:
        confetti.move()

        # Vérifier si le confetti touche le sol
        if confetti.ycor() <= -300:
            confetti.sety(-300)
            confetti.gravity = 0

turtle.done()

