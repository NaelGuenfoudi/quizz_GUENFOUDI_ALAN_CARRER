-- Création de la table Joueur
CREATE TABLE Joueur (
    ID_Joueur INT PRIMARY KEY AUTO_INCREMENT,
    Nom VARCHAR(255) NOT NULL,
    Prenom VARCHAR(255),
    Email VARCHAR(255) UNIQUE NOT NULL
    -- d'autres champs si nécessaire
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
    ID_Joueur INT,
    ID_Question INT,
    ID_Reponse INT,
    Temps_Reponse INT NOT NULL, -- En secondes ou minutes
    Date_Reponse DATE NOT NULL,
    PRIMARY KEY (ID_Joueur, ID_Question),
    FOREIGN KEY (ID_Joueur) REFERENCES Joueur(ID_Joueur),
    FOREIGN KEY (ID_Question) REFERENCES Question(ID_Question),
    FOREIGN KEY (ID_Reponse) REFERENCES Reponse(ID_Reponse)
);

-- Création de la table Score
CREATE TABLE Score (
    ID_Joueur INT,
    Score_Total INT NOT NULL,
    Date_Score DATE NOT NULL,
    PRIMARY KEY (ID_Joueur, Date_Score),
    FOREIGN KEY (ID_Joueur) REFERENCES Joueur(ID_Joueur)
);
