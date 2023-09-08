import mysql.connector

# Établir la connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Admin",
    database="quiz"
)

# Créer un curseur pour exécuter des requêtes SQL
cursor = db.cursor()

# Fonction pour afficher tous les joueur
def afficher_joueur():
    cursor.execute("SELECT * FROM joueur")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Fonction pour ajouter un joueur
def ajouter_joueur(nom):
    sql = "INSERT INTO joueur (nom) VALUES (%s)"
    values = (nom)
    cursor.execute(sql, values)
    db.commit()
    print("joueur ajouté avec succès")

# Fonction pour supprimer un joueur
def supprimer_joueur(id):
    sql = "DELETE FROM joueur WHERE id = %s"
    values = (id, )
    cursor.execute(sql, values)
    db.commit()
    print("joueur supprimé avec succès")

# Menu principal
while True:
    print("----- Système d'administration -----")
    print("1. Afficher les joueur")
    print("2. Ajouter un joueur")
    print("3. Supprimer un joueur")
    print("4. Quitter")
    choix = input("Choisissez une action : ")

    if choix == "1":
        afficher_joueur()
    elif choix == "2":
        nom = input("Nom : ")
        ajouter_joueur(nom)
    elif choix == "3":
        id = input("ID de l'joueur à supprimer : ")
        supprimer_joueur(id)
    elif choix == "4":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")

# Fermer la connexion à la base de données
cursor.close()
db.close()
