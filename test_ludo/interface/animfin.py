import turtle
import random

# Configuration de la fenêtre
screen = turtle.Screen()
screen.title("Feux d'artifice")
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.tracer(2)

# Création d'une classe pour les particules de feu d'artifice
class FireworkParticle(turtle.Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()

    def explode(self):
        self.shapesize(stretch_wid=5, stretch_len=10)

        # Animation de l'explosion
        for _ in range(10):
            self.color(random.choice(["red", "orange", "yellow", "white", "blue"]))
            self.forward(5)
            self.right(random.randint(0, 360))

        # Cacher la particule après l'explosion
        self.hideturtle()

# Liste de particules de feux d'artifice
particles = []

# Génération des particules de feux d'artifice
def generate_firework():
    particle = FireworkParticle(random.choice(["red", "orange", "yellow", "white", "blue"]))
    particle.goto(0, -200)
    particle.setheading(random.randint(80, 100))
    particles.append(particle)

# Boucle principale de l'animation
while True:
    screen.update()
    # Génération d'un nouveau feux d'artifice
    if random.randint(0, 100) < 5:
        generate_firework()

    # Animation des particules de feu d'artifice
    for particle in particles:
        particle.forward(20)
        particle.right(random.randint(-15, 15))

        # Vérifier si la particule est hors de l'écran
        if particle.ycor() >= 300 or particle.xcor() >= 400 or particle.xcor() <= -400:
            particle.explode()
            particles.remove(particle)

turtle.done()
