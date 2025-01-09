import streamlit as st
import numpy as np
from views.base_page import BasePage

class DemonstrationPage(BasePage):
    def __init__(self, df, t):
        super().__init__()
        self.header_title = "Démonstration du modèle sélectionné"
        self.df = df
        self.t = t 

    def display(self):
        st.markdown(self.get_header(self.header_title), unsafe_allow_html=True)
        self.machine_learning_model()

    def machine_learning_model(self):
        df = self.df
        t = self.t

        def recommend_movies(movie_title, num_recommendations=5):
            if movie_title not in df['title'].values:
                return "Ce film n'est pas dans la base de données."
            
            movie_index = df.index[df['title'] == movie_title].tolist()[0]
            similar_items, distances = t.get_nns_by_item(movie_index, num_recommendations * 2 + 1, include_distances=True)

            filtered_indices = []
            filtered_distances = []
            for idx, dist in zip(similar_items, distances):
                if idx != movie_index and len(filtered_indices) < num_recommendations and dist > 1e-6:
                    filtered_indices.append(idx)
                    filtered_distances.append(dist)
            
            max_distance = max(filtered_distances) if filtered_distances else 1
            similarity_scores = [1 - (np.log1p(d) / np.log1p(max_distance)) for d in filtered_distances]

            genres_target = df.loc[movie_index, 'Action':'Western'].astype(bool)
            filtered_movies = []
            filtered_scores = []
            for idx, score in zip(filtered_indices, similarity_scores):
                genres_recommend = df.loc[idx, 'Action':'Western'].astype(bool)
                if any(genres_target & genres_recommend):
                    filtered_movies.append(df['title'].iloc[idx])
                    filtered_scores.append(score)
                    if len(filtered_movies) >= num_recommendations:
                        break
            
            return list(zip(filtered_movies, filtered_scores))

        # Choisir un film pour obtenir des recommandations - Environnement Production
        # movie_title = st.selectbox("Choisissez un film pour les recommandations", df['title'].unique())
        
        # Choisir un film pour obtenir des recommandations - Environnement de Developpement
        index_star_trek = df[df['title'].str.contains('Jumanji', case=False)].index[0]
        start_index = max(index_star_trek - 250, 0)
        end_index = min(index_star_trek + 250 + 1, len(df))
        selected_movies = df['title'].iloc[start_index:end_index]


        movie_title = st.selectbox("Choisissez un film pour les recommandations", selected_movies.unique())
        num_recommendations = st.slider("Nombre de recommandations", 1, 10, 5)

        if st.button("Obtenir des recommandations"):
            recommendations = recommend_movies(movie_title, num_recommendations)
            if isinstance(recommendations, str):
                st.write(recommendations)
            else:
                st.write("Films recommandés :")
                for movie, score in recommendations:
                    # st.write(f"{movie} (Score: {score:.2f})") # Avec score si besoin
                    st.write(f"{movie}")

