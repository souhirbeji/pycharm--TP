import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


animelist = pd.read_csv('anime.csv')

# Vérifier les valeurs manquantes et les corriger
animelist['genre'] = animelist['genre'].fillna('Unknown')
animelist['type'] = animelist['type'].fillna('Unknown')
animelist['rating'] = animelist['rating'].fillna(animelist['rating'].mean())

# Créer une nouvelle colonne pour indiquer la catégorie de la note (low, high)
def rating_category(x):
    if x <= 7:
        return 'Low'  # Low Rating: 1 <= rating <= 7
    else:
        return 'High'  # High Rating: 7 < rating <= 10

# Appliquer la fonction pour créer la nouvelle colonne
animelist['rating_category'] = animelist['rating'].apply(rating_category)

# Décomposer la colonne 'genre'
genres_split = animelist['genre'].str.split(', ', expand=True)

# Créer une colonne pour chaque genre
genre_dummies = genres_split.apply(pd.Series.value_counts, axis=1).fillna(0)

# Combiner ces nouvelles colonnes avec l'animelist original
animelist = pd.concat([animelist, genre_dummies], axis=1)

# Créer une variable pour l'arbre de décision
# Utiliser 'type' et les genres comme caractéristiques
X = animelist[['type'] + genre_dummies.columns.tolist()]  # Inclure 'type' et les genres

# Convertir 'type' en variables binaires (dummies)
X = pd.get_dummies(X, columns=['type'], drop_first=True)  # Drop 'Unknown' pour éviter la multicolinéarité

# Cible : 'rating_category' (Low, High)
y = animelist['rating_category']

# Créer et entraîner un arbre de décision avec un critère d'entropie et une profondeur augmentée
clf = DecisionTreeClassifier(max_depth=3, criterion='entropy', random_state=42)
clf.fit(X, y)

# Visualiser l'arbre de décision
plt.figure(figsize=(15, 10))
plot_tree(clf, feature_names=X.columns, class_names=['Low Rating', 'High Rating'], filled=True)
plt.show()
