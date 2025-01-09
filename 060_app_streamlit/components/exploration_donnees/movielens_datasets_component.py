import streamlit as st

from components.base_component import BaseComponent
from components.exploration_donnees.movielens_datasets.movies_subcomponent import MoviesSubcompoment
from components.exploration_donnees.movielens_datasets.tags_subcomponenet import TagsSubcompoment
from components.exploration_donnees.movielens_datasets.rating_subcomponent import RatingSubcompoment
from components.exploration_donnees.movielens_datasets.links_subcomponent import LinksSubcompoment
from components.exploration_donnees.movielens_datasets.genome_scores_subcomponent import GenomeScoresSubcompoment
from components.exploration_donnees.movielens_datasets.genome_tags_subcomponent import GenomeTagsSubcompoment
from components.exploration_donnees.movielens_datasets.recap_movielens_datasets_subcomponent import RecapMovielensDatasetsSubcomponent

class MovielensDatasetsComponent(BaseComponent):
    def __init__(self):
        super().__init__("Exploration des données MovieLens 20M")
        self.movies = MoviesSubcompoment()
        self.tags = TagsSubcompoment()
        self.rating = RatingSubcompoment()
        self.links = LinksSubcompoment()
        self.genome_scores = GenomeScoresSubcompoment()
        self.genome_tags = GenomeTagsSubcompoment()
        self.recapMovielens = RecapMovielensDatasetsSubcomponent()
        self.chapters = {
            "Movies": self.movies,
            "Tags": self.tags,
            "Rating": self.rating,
            "Links": self.links,
            "Genome-scores": self.genome_scores,
            "Genome-tags": self.genome_tags,
            "Recap Movielens": self.recapMovielens
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
        Les datasets présents dans les données Movielens 20M n’ont pas posé de problème particulier lors de leur chargement, les données étaient lisibles et ne comportaient pas d’erreurs particulières. 
        """)


