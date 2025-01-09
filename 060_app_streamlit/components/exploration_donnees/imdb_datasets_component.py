import streamlit as st

from components.base_component import BaseComponent
from components.exploration_donnees.imdb_datasets.name_basics_subcomponent import NameBasicsSubcompoment
from components.exploration_donnees.imdb_datasets.title_akas_subcomponent import TitleAkasSubcompoment
from components.exploration_donnees.imdb_datasets.title_basics_subcomponent import TitleBasicsSubcompoment
from components.exploration_donnees.imdb_datasets.title_crew_subcomponent import TitleCrewSubcompoment
from components.exploration_donnees.imdb_datasets.title_episode_subcomponent import TitleEpisodeSubcompoment
from components.exploration_donnees.imdb_datasets.title_principals_subcomponent import TitlePrincipalsSubcompoment
from components.exploration_donnees.imdb_datasets.title_rating_subcomponent import TitleRatingSubcompoment
from components.exploration_donnees.imdb_datasets.recap_imdb_datasets_subcomponent import RecapImdbDatasetsSubcompoment

class ImdbDatasetsComponent(BaseComponent):
    def __init__(self):
        super().__init__("Exploration des données IMDb")
        self.name_basics = NameBasicsSubcompoment()
        self.title_akas = TitleAkasSubcompoment()
        self.title_basics = TitleBasicsSubcompoment()
        self.title_crew = TitleCrewSubcompoment()
        self.title_episode = TitleEpisodeSubcompoment()
        self.title_principals = TitlePrincipalsSubcompoment()
        self.title_rating = TitleRatingSubcompoment()
        self.recapImbd = RecapImdbDatasetsSubcompoment()
        self.chapters = {
            "Name basics": self.name_basics,
            "Title akas": self.title_akas,
            "Title basics": self.title_basics,
            "Title crew": self.title_crew,
            "Title episode": self.title_episode,
            "Title principals": self.title_principals,
            "Title rating": self.title_rating,
            "Recap IMDb": self.recapImbd
        }

    def display(self):
        st.header(self.title)
        st.markdown(self.get_load_data(), unsafe_allow_html=True)

        tabs = st.tabs(list(self.chapters.keys()))

        for tab, (chapter, component) in zip(tabs, self.chapters.items()):
            with tab:
                component.display()


    def get_load_data(self):
        return ("""
        ### Chargement des données
        Lors du chargement des données de l’ensemble IMDb, nous nous sommes heurté à une volumineuse quantité de données, dépassant les 85 millions de lignes dans le jeu de données **title.principals**.
        Après plusieurs essais, nous avons opté pour l’utilisation du paramètre **low_memory** et, si nécessaire, du paramètre **nrows**, ce qui nous a permis d’analyser une partie représentative des données
        tout en garantissant une analyse efficace sans ralentir le serveur.
        """)


