from components.base_component import BaseComponent
import streamlit as st

class IntroductionComponent(BaseComponent):
    def __init__(self):
        super().__init__("Introduction")

    def display(self):
        st.header(self.title)
        st.markdown(self.get_introduction(), unsafe_allow_html=True)
        st.markdown(self.get_imdb_datasets(), unsafe_allow_html=True)
        st.markdown(self.get_movilens_datasets(), unsafe_allow_html=True)
        st.markdown(self.get_dstrec_datasets(), unsafe_allow_html=True)

    def get_introduction(self):
        return ("""
        Ensuite, nous avons poursuivi avec la phase de prétraitement des données. Cette étape consiste à préparer les données et à garantir la pertinence des données en vue de construire le modèle de machine learning.
        Le prétraitement comprend diverses opérations telles que le nettoyage des données, la modification du typage des colonnes, la transformation de colonnes, etc.
        
        Le prétraitement des données a été réalisée au sein de plusieurs Jupyter Notebooks, chacun dédié à une phase spécifiques  : 

        """)

    def get_imdb_datasets(self):
        return ("""
        <h3>IMDb datasets</h3>
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:55%;">Fichier d’évaluation</th>
                    <th style="width:45%;">Fichier source</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>000_dstrec_preparation_title_basics.ipynb</td>
                    <td>title.basics.tsv | title.ratings.tsv</td>
                </tr>
                <tr>
                    <td>001_dstrec_preparation_name_basics.ipynb</td>
                    <td>name.basics.tsv</td>
                </tr>
                <tr>
                    <td>002_dstrec_preparation_title_principals.ipynb</td>
                    <td>title.principals.tsv | title_basics_tconst.csv</td>
                </tr>
                <tr>
                    <td>003_dstrec_transformation_title_principals.ipynb</td>
                    <td>title.principals.csv | name.basics.csv</td>
                </tr>
                <tr>
                    <td>004_dstrec_transformation_imdb.ipynb</td>
                    <td>title.principals.csv | title.basics.csv</td>
                </tr>
            </tbody>
        </table>
        """)
    
    def get_movilens_datasets(self):
        return ("""
        <h3>MovieLens 20M datasets</h3>
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:55%;">Fichier d’évaluation</th>
                    <th style="width:45%;">Fichier source</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>005_dstrec_transformation_movielens.ipynb</td>
                    <td>movies.csv | tags.csv | ratings.csv | links.csv</td>
                </tr>
                <tr>
                    <td>006_dstrec_transformation_movielens_with_directors.ipynb</td>
                    <td>movielens.csv</td>
                </tr>
            </tbody>
        </table>
        """)
    
    def get_dstrec_datasets(self):
        return ("""
        <h3>Dstrec datasets</h3>
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:55%;">Fichier d’évaluation</th>
                    <th style="width:45%;">Fichier source</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>007_dstrec_transformation_des_donnees.ipynb</td>
                    <td>imdb.csv | movielens.csv</td>
                </tr>
            </tbody>
        </table>
        """)