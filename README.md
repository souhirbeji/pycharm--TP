
Description du Projet
Ce projet utilise un arbre de décision pour classifier les animes en deux catégories de notes : Low (note ≤ 7) et High (note > 7), basé sur leurs genres et types. Le modèle est entraîné avec un dataset d'animes, où les données manquantes sont traitées, et les genres sont transformés en variables binaires pour chaque anime.

Étapes Principales :
Chargement des Données : Lecture des données à partir d'un fichier CSV.
Prétraitement : Remplacement des valeurs manquantes dans les colonnes genre, type et rating.
Création de la Categorie de Note : Attribution de catégories Low ou High selon la note de l'anime.
Transformation des Genres : Conversion des genres multiples en colonnes binaires.
Entraînement du Modèle : Utilisation d'un DecisionTreeClassifier pour classifier les animes en Low ou High.
Visualisation : Affichage de l'arbre de décision pour comprendre comment le modèle fait ses prédictions.
Conclusion
Ce projet montre l'application d'un arbre de décision pour prédire la catégorie de la note d'un anime. Le modèle est interprétable grâce à la visualisation de l'arbre, permettant de comprendre l'impact des genres et types sur la classification. 
Résultats et Interprétation
L'arbre de décision nous montre comment les différentes catégories de genres influencent la prédiction de la note d'un anime. 
Par exemple, certains genres peuvent avoir un impact plus important sur la classification dans la catégorie High, tandis que d'autres genres pourraient être plus associés à la catégorie Low.
