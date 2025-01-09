import streamlit as st

from components.base_subcomponent import BaseSubcomponent

class RecapImdbDatasetsSubcompoment(BaseSubcomponent):
    def __init__(self) :
        self.subtitle = "Récapitulatif de l’exploration des données IMDb"

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
                    <th>Colonne à extraire</th>
                    <th>Colonne à garder</th>
                    <th>Commentaire</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Name basics</td>
                    <td>6</td>
                    <td>13 508 117</td>
                    <td>birthYear, deathYear, primaryProfession, knownForTitles</td>
                    <td>nconst, primaryName</td>
                    <td>A retravailler</td>
                </tr>
                <tr>
                    <td>Title akas</td>
                    <td>8</td>
                    <td>48 459 150</td>
                    <td>/</td>
                    <td>/</td>
                    <td>A exclure du ML</td>
                </tr>
                <tr>
                    <td>Title basics</td>
                    <td>9</td>
                    <td>10 790 736</td>
                    <td>originalTitle, isAdult, startYear, endYear, runtimeMinutes</td>
                    <td>tconst, titleType, primaryTitle, genres</td>
                    <td>A retravailler <br> titleType : uniquement: ”movie”</td>
                </tr>
                <tr>
                    <td>Title crew</td>
                    <td>3</td>
                    <td>10 143 819</td>
                    <td>/</td>
                    <td>/</td>
                    <td>A exclure du ML</td>
                </tr>
                <tr>
                    <td>Title episode</td>
                    <td>4</td>
                    <td>8 258 774</td>
                    <td>/</td>
                    <td>/</td>
                    <td>A exclure du ML</td>
                </tr>
                <tr>
                    <td>Title principals</td>
                    <td>6</td>
                    <td>85 883 465</td>
                    <td>job, characters, ordering</td>
                    <td>tconst, nconst, category</td>
                    <td>A retravailler</td>
                </tr>
                <tr>
                    <td>Title rating</td>
                    <td>3</td>
                    <td>1 439 968</td>
                    <td>/</td>
                    <td>tconst, averageRating, numVotes</td>
                    <td></td>
                </tr>
            </tbody>
        </table>
        """)