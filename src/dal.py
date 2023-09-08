import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser

def read_db_config(filename='conf.ini', section='MySQL'):
        parser = ConfigParser()
        parser.read(filename)
        
        db_config = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db_config[param[0]] = param[1]
        else:
            raise Exception(f'Section {section} not found in the {filename} file')
        
        return db_config

  
def create_connection():
        db_config = read_db_config()
        try:
            connection = mysql.connector.connect(**db_config) # Utilisation de ** pour envoyer les paramètres de connexion contenus dans db_confi
            
            return connection
        except Error as e:
            print("Error connecting to MySQL:", e)
            return None
        
def select_query(query, params=None):
    # Assuming DataBas_connection() is a function that gives a database connection.
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # If no params are passed, we'll default to an empty tuple
        params = params or ()
        cursor.execute(query)

        # We might want to decide if we need to fetch data based on query type
        results = cursor.fetchall()
        return results
       

    except Exception as e:
        print(f"Error executing query: {e}")
        # In the case of an error, you might want to return None or raise the error, depending on your requirements.
        return None

    finally:
        if conn.is_connected():
            conn.close()


def getAllPlayersData():
    """
    Récupère les données de tous les joueurs.

    Retour:
        list: Liste de tuples contenant les données des joueurs.
    """
    players_data = select_query('select * from joueur')
    return players_data

def getTextQuestionId(idQuestion):
    return select_query(f'select Texte from question where ID_Question={idQuestion}')[0][0]

def getAllQuestionData():
    """
    Récupère toutes les données des questions.

    Retour:
        list: Liste de tuples contenant les données des questions.
    """
    questions_data= select_query('select * from Question ')
    return questions_data

def getGoodResponseForQuestion(idQuestion):
    """
    Récupère la bonne réponse pour une question donnée.

    Args:
        idQuestion (int): L'identifiant de la question.

    Retour:
        list: Liste contenant le tuple de la bonne réponse.
    """
    return select_query(f"select ID_Reponse from Reponse where Est_Correcte=true and ID_Question={idQuestion}")[0][0]

def getAllTheme():
    """
    Récupère tous les thèmes.

    Retour:
        list: Liste de tuples contenant l'ID et le nom des thèmes.
    """
    return select_query('select ID_THEME,Nom from Theme')

def getAllLevel():
    """
    Récupère tous les niveaux disponibles.

    Retour:
        list: Liste de tuples contenant l'ID et le nom des niveaux.
    """
    return [(1, "Niveau facile"), (2, "Niveau dur"), (3, "Niveau expert")]

def getQuestionsOfThemeAndLevel(idTheme, idLevel):
    """
    Récupère les questions selon un thème et un niveau donnés.

    Args:
        idTheme (int): L'identifiant du thème.
        idLevel (int): L'identifiant du niveau.

    Retour:
        list: Liste de tuples contenant l'ID et le texte des questions.
    """
    query = f'select ID_Question, Texte from Question where ID_Theme={idTheme} and ID_Level={idLevel}'    
    return select_query(query)

def getReponsesForQuestion(idQuestion):
    query =f'select ID_Reponse,Texte from Reponse where ID_Question={idQuestion}'
    return select_query(query)

def get_password_from_username(username):
    """
    Récupère le mot de passe d'un utilisateur depuis la base de données.

    Args:
        username (str): Nom d'utilisateur.

    Returns:
        str: Mot de passe associé ou None si non trouvé.
    """
    query = f"SELECT password FROM user WHERE username='{username}'"
    return select_query(query)

def is_admin(username):
    query=f'select admin from user where username=username'
def is_user(username):
    """
    Vérifie si un utilisateur existe dans la base de données.

    Args:
        username (str): Nom d'utilisateur.

    Returns:
        bool: True si l'utilisateur existe, False sinon.
    """
    query = f"SELECT username FROM user WHERE username='{username}'"
    result = select_query(query)
    return True if result else False

def get_all_usernames():
    """
    Récupère tous les noms d'utilisateurs de la base de données.

    Returns:
        list: Liste des noms d'utilisateurs.
    """
    query = "SELECT username FROM user"
    return select_query(query)

def main():
    print(select_query('select * from Question where ID_Question=3'))
    reponses=getReponsesForQuestion(3)
    print(reponses[0][0])
main()




    








