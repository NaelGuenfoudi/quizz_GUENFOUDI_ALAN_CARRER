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

---------------------------------------------------------------

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `last_played` date DEFAULT NULL,
  `game_played` int(11) DEFAULT NULL,
  `admin` tinyint(1) NOT NULL,
  `best_scores` int(11) DEFAULT NULL,
  `registered_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `last_played`, `game_played`, `admin`, `best_scores`, `registered_at`) VALUES
(1, 'Alan', '$2b$12$Y24AzBPBY8gHYp/vAIAQWOn65S5I3XNzrI3qeOTQ4JRef/JmdYwvu', NULL, NULL, 1, NULL, '2023-09-06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;
