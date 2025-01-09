import streamlit as st
from components.base_subcomponent import BaseSubcomponent

class RecapMovielensDatasetsSubcomponent(BaseSubcomponent):
    def __init__(self):
        self.subtitle = "Récapitulatif de l’exploration des données MovieLens"

    def display(self):
        st.subheader(self.subtitle)
        st.markdown(self.get_content(), unsafe_allow_html=True)

    def get_content(self):
        return ("""
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th>Nom dataset</th>
                    <th>Nombre de col</th>
                    <th>Nombre de ligne</th>
                    <th>Colonne à extraire/supprimer/modifier</th>
                    <th>Colonne à garder</th>
                    <th>Commentaire</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Movies</td>
                    <td>3</td>
                    <td>27 278</td>
                    <td>/</td>
                    <td>movieId, title, genres</td>
                    <td>Base de prétraitement</td>
                </tr>
                <tr>
                    <td>Tags</td>
                    <td>4</td>
                    <td>465 564</td>
                    <td>timestamp, userId, tag</td>
                    <td>movieId</td>
                    <td>A retravailler</td>
                </tr>
                <tr>
                    <td>Rating</td>
                    <td>4</td>
                    <td>20 000 263</td>
                    <td>timestamp, userId, rating</td>
                    <td>movieId</td>
                    <td>A retravailler</td>
                </tr>
                <tr>
                    <td>Links</td>
                    <td>3</td>
                    <td>27 278</td>
                    <td>tmdbId, imdbId</td>
                    <td>movieId</td>
                    <td>A retravailler</td>
                </tr>
                <tr>
                    <td>Genome-scores</td>
                    <td>3</td>
                    <td>11 709 768</td>
                    <td>/</td>
                    <td>/</td>
                    <td>A exclure du ML</td>
                </tr>
                <tr>
                    <td>Genome-tags</td>
                    <td>2</td>
                    <td>1 128</td>
                    <td>/</td>
                    <td>/</td>
                    <td>A exclure du ML</td>
                </tr>
            </tbody>
        </table>
        """)

