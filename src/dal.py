import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
from datetime import date
from datetime import datetime

def read_db_config(filename='src/db/conf.ini', section='MySQL'):
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

def update_query(query, params=None):
    """
    Exécute une requête UPDATE dans la base de données.

    Args:
        query (str): La requête SQL à exécuter.
        params (tuple, optional): Les paramètres pour la requête.

    Returns:
        int: Le nombre de lignes affectées par la requête.
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        params = params or ()
        cursor.execute(query, params)
        conn.commit()
        return cursor.rowcount

    except Exception as e:
        print(f"Error executing update query: {e}")
        return None

    finally:
        if conn.is_connected():
            conn.close()

def delete_query(query, params=None):
    """
    Exécute une requête DELETE dans la base de données.

    Args:
        query (str): La requête SQL à exécuter.
        params (tuple, optional): Les paramètres pour la requête.

    Returns:
        int: Le nombre de lignes affectées par la requête.
    """
    return update_query(query, params)  # La logique pour DELETE est la même que pour UPDATE

def insert_query(query, params=None):
    """
    Exécute une requête INSERT dans la base de données.

    Args:
        query (str): La requête SQL à exécuter.
        params (tuple, optional): Les paramètres pour la requête.

    Returns:
        int: L'ID de la nouvelle ligne insérée.
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        params = params or ()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid

    except Exception as e:
        print(f"Error executing add query: {e}")
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

def getGoodResponseForQuestion(id_question):
    """
    Récupère la bonne réponse pour une question donnée.

    Args:
        idQuestion (int): L'identifiant de la question.

    Retour:
        list: Liste contenant le tuple de la bonne réponse.
    """
    return select_query(f"select ID_Reponse from Reponse where Est_Correcte=true and ID_Question={id_question}")[0][0]

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

def getQuestionsOfTheme(idTheme, nbQuestion):
    """
    Récupère un nombre de question donné en fonction du thème,si l'id du thème est 0, le jeu sera générique.

    Args:
        idTheme (int): L'identifiant du thème.
        nbQuestion (int): Nombre de questions à récupérer.

    Retour:
        list: Liste de tuples contenant l'ID et le texte des questions.
    """
    if(idTheme!=0):
        query = f'select ID_Question, Texte from Question where ID_Theme={idTheme}  ORDER BY RAND() limit {nbQuestion}'    
    else:
        query = f'select ID_Question, Texte from Question  ORDER BY RAND() limit {nbQuestion}'  
    
    return select_query(query)

def get_id_question_for_text(text_question):
    """
    Récupère l'ID de la question basé sur le texte de la question.

    Args:
        text_question (str): Le texte de la question.

    Retour:
        int: L'ID de la question, ou None si la question n'est pas trouvée.
    """
    query = f"SELECT ID_Question FROM Question WHERE Texte = '{text_question}'"
    results = select_query(query)
    
    if results:
        return results[0][0]  # Retourne le premier ID trouvé
    else:
        return None


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
    result = select_query(query)

    # Check if the result is not empty and return the password
    if result and len(result) > 0:
        return result[0][0]
    else:
        return None


def is_admin(username):
    query=f"select admin from user where username='{username}'"
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

def update_password(username, new_password):
    """
    Met à jour le mot de passe d'un utilisateur.

    Args:
        username (str): Le nom d'utilisateur.
        new_password (str): Le nouveau mot de passe.

    Returns:
        int: Le nombre de lignes affectées par la mise à jour.
    """
    query = "UPDATE users SET password = %s WHERE username = %s"
    params = (new_password, username)
    return update_query(query, params)

import bcrypt

def insert_user(username, password, is_admin):
    """
    Insère un nouvel utilisateur dans la base de données.

    Args:
        username (str): Le nom d'utilisateur.
        password (str): Le mot de passe en clair.
        is_admin (bool): Si l'utilisateur est un administrateur.

    Returns:
        int: L'ID de la nouvelle ligne insérée ou None en cas d'erreur.
    """
    
    # Hacher le mot de passe avec bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Construire la requête SQL
    query = """
    INSERT INTO User (username, password, is_admin)
    VALUES (%s, %s, %s)
    """
    
    # Exécuter la requête avec les paramètres
    return insert_query(query, (username, hashed_password.decode('utf-8'), int(is_admin)))


def delete_user(username):
    """
    Supprime un utilisateur de la base de données.

    Args:
        username (str): Le nom d'utilisateur à supprimer.

    Returns:
        int: Le nombre de lignes affectées par la suppression.
    """
    query = "DELETE FROM users WHERE username = %s"
    params = (username,)
    return delete_query(query, params)

def set_admin(username):
    """
    Attribue le rôle d'administrateur à un utilisateur.

    Args:
        username (str): Le nom d'utilisateur.

    Returns:
        int: Le nombre de lignes affectées par la mise à jour.
    """
    query = "UPDATE users SET admin = 1 WHERE username = %s"
    params = (username,)
    return update_query(query, params)

def remove_admin(username):
    """
    Retire le rôle d'administrateur d'un utilisateur.

    Args:
        username (str): Le nom d'utilisateur.

    Returns:
        int: Le nombre de lignes affectées par la mise à jour.
    """
    query = "UPDATE users SET admin = 0 WHERE username = %s"
    params = (username,)
    return update_query(query, params)
    
def get_id_reponse_for_text(text_response):
    """
    Récupère l'ID de la réponse basé sur le texte de la réponse.

    Args:
        text_response (str): Texte de la réponse.

    Returns:
        int: ID de la réponse ou None si non trouvé.
    """
    query = f"SELECT ID_Reponse FROM Reponse WHERE Texte='{text_response}'"
    result = select_query(query)  # Supposons que select_query est une fonction que vous avez définie pour exécuter des requêtes SELECT.
    
    if result:
        return result[0][0]  # Retourne le premier élément du premier tuple.
    return None

def get_point_question(id_question):
    query=f"SELECT Niveau_Complexite from Question where ID_Question={id_question}"
    return int(select_query(query)[0][0])

def get_time_question(id_question):
    query=f'select Temps_Imparti from Question where ID_Question={id_question}'
    return int(select_query(query)[0][0])

def get_id_user_from_username(username):
    """
    Récupère l'ID de l'utilisateur à partir de son nom d'utilisateur.
    """
    query = f"SELECT id_user FROM User WHERE username = '{username}'"
    result = select_query(query)
    if result:
        return result[0][0]
    else:
        return None

def add_new_score(username, score, global_time, id_theme):
    """
    Ajoute un nouveau score pour un utilisateur donné.
    """
    user_id = get_id_user_from_username(username)
    if user_id is None:
        print("Nom d'utilisateur non trouvé.")
        return

    
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        query = f"INSERT INTO Score (id_user, Score_Total, temps_game, Date_Score, id_theme) VALUES ({user_id}, {score}, {global_time}, '{current_date}', {id_theme})"
        insert_query(query)
        print(f"Score ajouté pour {username}.")
    except:
        print(f"Erreur lors de l'ajout du score")
def get_highscores(nb_scores):
    query=f"select * from Score order by Score_Total limit {nb_scores}"
    return select_query(query)





    








