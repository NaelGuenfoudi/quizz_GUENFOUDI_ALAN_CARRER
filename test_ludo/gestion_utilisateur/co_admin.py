import mysql.connector

# Établir la connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="quiz"
)

# Créer un curseur pour exécuter des requêtes SQL
cursor = db.cursor()

# Fonction pour vérifier les identifiants de l'administrateur
def verif_creds(username, password):
    sql = "SELECT * FROM administrateurs WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False

# Fonction pour l'interface de connexion
def interface_connexion():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    if verif_creds(username, password):
        print("Connexion réussie en tant qu'administrateur")
        # Ajoutez ici le code pour l'interface de l'administrateur
    else:
        print("Identifiants incorrects")

# Appel de l'interface de connexion
interface_connexion()

# Fermer la connexion à la base de données
cursor.close()
db.close()
