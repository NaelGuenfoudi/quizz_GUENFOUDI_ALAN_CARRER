-- Création de la table Joueur
CREATE TABLE User (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255),
    is_admin TINYINT(1)
    
);

-- Création de la table Theme
CREATE TABLE Theme (
    ID_Theme INT PRIMARY KEY AUTO_INCREMENT,
    Nom VARCHAR(255) NOT NULL
);

-- Création de la table Question
CREATE TABLE Question (
    ID_Question INT PRIMARY KEY AUTO_INCREMENT,
    ID_Theme INT,
    Texte VARCHAR(1000) NOT NULL,
    Niveau_Complexite INT NOT NULL, -- 1 pour facile, 2 pour moyen, 3 pour difficile, etc.
    Temps_Imparti INT NOT NULL, -- En secondes ou minutes
    FOREIGN KEY (ID_Theme) REFERENCES Theme(ID_Theme)
);

-- Création de la table Reponse
CREATE TABLE Reponse (
    ID_Reponse INT PRIMARY KEY AUTO_INCREMENT,
    ID_Question INT,
    Texte VARCHAR(500) NOT NULL,
    Est_Correcte BOOLEAN NOT NULL, -- TRUE si c'est la bonne réponse, FALSE sinon
    FOREIGN KEY (ID_Question) REFERENCES Question(ID_Question)
);

-- Création de la table Donne
CREATE TABLE Donne (
    id_user
 INT,
    ID_Question INT,
    ID_Reponse INT,
    Temps_Reponse INT NOT NULL, -- En secondes ou minutes
    Date_Reponse DATE NOT NULL,
    PRIMARY KEY (id_user
, ID_Question),
    FOREIGN KEY (id_user
) REFERENCES User(id_user
),
    FOREIGN KEY (ID_Question) REFERENCES Question(ID_Question),
    FOREIGN KEY (ID_Reponse) REFERENCES Reponse(ID_Reponse)
);

-- Création de la table Score
CREATE TABLE Score (
    id_user
 INT,
    Score_Total INT NOT NULL,
    Date_Score DATE NOT NULL,
    PRIMARY KEY (id_user
, Date_Score),
    FOREIGN KEY (id_user
) REFERENCES User(id_user
)
);

