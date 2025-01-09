import pandas as pd
from sklearn.preprocessing import MaxAbsScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import TruncatedSVD
from annoy import AnnoyIndex
import streamlit as st

@st.cache_resource
def load_data_and_model():
    df = pd.read_csv("data/dstrec.csv")

    # Calcul du Weighted Average Rating (WAR)
    C = df['averageRating'].mean()
    m = df['numVotes'].quantile(0.90)

    def weighted_average_rating(x, m=m, C=C):
        v = x['numVotes']
        R = x['averageRating']
        return (v / (v + m) * R) + (m / (m + v) * C)

    df['weightedAverageRating'] = df.apply(weighted_average_rating, axis=1)
    df = df.drop(['imdbId'], axis=1)

    # Préparation des colonnes catégorielles et numériques
    categorical_features = ['director', 'actor_actress', 'producer']
    numeric_features = [col for col in df.columns if col not in categorical_features + ['title']]

    # Transformation des colonnes numériques et catégorielles
    numeric_transformer = MaxAbsScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ],
        sparse_threshold=0.5)

    # Application des transformations
    content_features = preprocessor.fit_transform(df.drop('title', axis=1))

    # Normalisation des caractéristiques
    scaler = MaxAbsScaler()
    scaled_features = scaler.fit_transform(content_features)

    # Réduction dimensionnelle avec TruncatedSVD
    fixed_components = 100
    svd = TruncatedSVD(n_components=fixed_components)
    reduced_features = svd.fit_transform(scaled_features)

    # Indexation des films avec Annoy
    f = reduced_features.shape[1]
    t = AnnoyIndex(f, 'euclidean')
    for i in range(len(reduced_features)):
        t.add_item(i, reduced_features[i])
    t.build(10)

    return df, t
