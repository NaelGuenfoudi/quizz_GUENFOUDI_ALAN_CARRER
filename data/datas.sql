-- Insérer des données dans la table Theme
-- Insérer des données dans la table Theme
INSERT INTO Theme (ID_Theme, Nom) VALUES
    (1, 'Cinéma'),
    (2, 'Histoire'),
    (3, 'Science'),
    (4, 'Littérature'),
    (5, 'Art'),
    (6, 'Géographie');


-- Insérer des données dans la table Question
INSERT INTO Question (ID_Question, ID_Theme, Texte, Niveau_Complexite, Temps_Imparti)
VALUES
    (1, 1, "Quel réalisateur est derrière le film 'Pulp Fiction'?", 1, 30),
    (2, 1, "Dans quel film Leonardo DiCaprio joue-t-il le rôle de Jack Dawson?", 1, 30),
    (3, 1, "Quel est le nom du vaisseau spatial dans 'Alien'?", 2, 40),
    (4, 1, "Quel acteur joue le rôle de Tony Stark, alias Iron Man, dans l'univers cinématographique Marvel?", 1, 20),
    (5, 1, "Quel est le premier film de la trilogie 'Le Seigneur des Anneaux' réalisé par Peter Jackson?", 1, 25),
    (6, 1, "Quel film d'animation met en scène des jouets qui prennent vie lorsqu'ils ne sont pas observés par les humains?", 1, 30),
    (7, 1, "Quel personnage de fiction est un archéologue et aventurier, connu pour rechercher des artefacts historiques?", 2, 35),
    (8, 1, "Quel est le nom du vaisseau spatial piloté par Han Solo dans 'Star Wars'?", 2, 25),
    (9, 1, "Dans quel film Tom Hanks joue-t-il le rôle de Forrest Gump?", 1, 30),
    (10, 1, "Quel réalisateur est derrière le film 'Les Dents de la mer'?", 2, 20),
    (11, 1, "Dans quel film le personnage Maximus interprété par Russell Crowe dit-il 'Mon nom est Maximus Decimus Meridius, commandant en chef des armées du Nord, général des légions Felix, fidèle serviteur du vrai empereur Marc Aurèle. Père d'un fils assassiné, époux d'une femme assassinée et j'aurai ma vengeance, dans cette vie ou dans l'autre.'?", 3, 45),
    (12, 2, "Quel élément chimique a le numéro atomique 79 et est connu pour sa couleur jaune brillante utilisée dans les bijoux?", 3, 35),
    (13, 3, "Qui est l'auteur du roman '1984'?", 3, 30),
    (14, 4, "Quel artiste néerlandais du XVIIe siècle est célèbre pour ses peintures de paysages, de scènes bibliques et sa technique de la lumière?", 3, 40),
    (15, 5, "Quelle rivière est la plus longue du monde, mesurant environ 6 650 kilomètres et traversant de nombreux pays en Afrique?", 3, 50);
-- Continuez ainsi pour toutes les questions

-- Insérer des données dans la table Reponse
INSERT INTO Reponse (ID_Reponse, ID_Question, Texte, Est_Correcte)
VALUES
    (1, 1, "Martin Scorsese", false),
    (2, 1, "Quentin Tarantino", true),
    (3, 1, "Joel Coen", false),
    (4, 2, "Inception", false),
    (5, 2, "Titanic", true),
    (6, 2, "Shutter Island", false),
    (7, 3, "Nostromo", true),
    (8, 3, "Serenity", false),
    (9, 3, "Falcon", false),
    (10, 4, "Robert Downey Jr.", true),
    (11, 4, "Chris Evans", false),
    (12, 4, "Mark Ruffalo", false),
    (13, 5, "Le Seigneur des Anneaux : La Communauté de l'Anneau", true),
    (14, 5, "Le Seigneur des Anneaux : Les Deux Tours", false),
    (15, 5, "Le Seigneur des Anneaux : Le Retour du Roi", false),
    (16, 6, "Toy Story", true),
    (17, 6, "Monstres et Cie", false),
    (18, 6, "Cars", false),
    (19, 7, "Indiana Jones", true),
    (20, 7, "James Bond", false),
    (21, 7, "Lara Croft", false),
    (22, 8, "Millennium Falcon", true),
    (23, 8, "Star Destroyer", false),
    (24, 8, "USS Enterprise", false),
    (25, 9, "Forrest Gump", true),
    (26, 9, "La Ligne verte", false),
    (27, 9, "Rain Man", false),
    (28, 10, "Steven Spielberg", false),
    (29, 10, "George Lucas", false),
    (30, 10, "James Cameron", true),
    (31, 11, "Braveheart", false),
    (32, 11, "300", false),
    (33, 11, "Gladiator", true),
    (34, 12, "Argent", false),
    (35, 12, "Or", true),
    (36, 12, "Cuivre", false),
    (37, 13, "George Orwell", true),
    (38, 13, "Aldous Huxley", false),
    (39, 13, "Ray Bradbury", false),
    (40, 14, "Johannes Vermeer", false),
    (41, 14, "Rembrandt", false),
    (42, 14, "Johannes Vermeer", false),
    (43, 15, "Nil", false),
    (44, 15, "Amazone", false),
    (45, 15, "Fleuve Congo", false),
    (46, 15, "Nil", true);
-- Continuez ainsi pour toutes les réponses
