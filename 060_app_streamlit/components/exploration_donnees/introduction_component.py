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

    def get_introduction(self):
        return ("""
        En suivant le processus standard pour construire un modèle de ML : collecte des données, exploration des données, prétraitement des données, entraînement du modèle,
        et enfin évaluation et optimisation du modèle, nous avons commencé par la première étape en rassemblant les ensembles de données non commerciaux fournis par IMDb et
        l'ensemble de données MovieLens 20M, fournis par GroupLens, dans le dossier **00_data_source** de notre répertoire de projet **dstrec**.
        
        Ensuite, nous sommes passés à l’exploration des deux ensembles de données. Cette étape est importante dans le processus de construction d'un modèle de recommandation.
        Elle permet de comprendre la structure et les caractéristiques des données, d'identifier les tendances, les anomalies, et les relations entre les variables, ainsi que
        de préparer les données pour l'analyse et le développement du modèle.
        
        L’exploration des données a été réalisée au sein de plusieurs Jupyter Notebooks, chacun dédié à un fichier contenant des informations spécifiques sur les films :
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
                    <td>dstrec_evaluation_name_basics_data.ipynb</td>
                    <td>name.basics.tsv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_title_akas_data.ipynb</td>
                    <td>title.akas.tsv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_title_basics_data.ipynb</td>
                    <td>title.basics.tsv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_title_crew_data.ipynb</td>
                    <td>title.crew.tsv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_title_episode_data.ipynb</td>
                    <td>title.episode.tsv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_title_principals_data.ipynb</td>
                    <td>title.principals.tsv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_title_ratings_data.ipynb</td>
                    <td>title.ratings.tsv</td>
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
                    <td>dstrec_evaluation_movies_data.ipynb</td>
                    <td>movies.csv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_ratings_data.ipynb</td>
                    <td>ratings.csv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_tags_data.ipynb</td>
                    <td>tags.csv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_links_data.ipynb</td>
                    <td>links.csv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_genome_scores_data.ipynb</td>
                    <td>genome_scores.csv</td>
                </tr>
                <tr>
                    <td>dstrec_evaluation_genome_tags_data.ipynb</td>
                    <td>genome_tags.csv</td>
                </tr>
            </tbody>
        </table>
        """)