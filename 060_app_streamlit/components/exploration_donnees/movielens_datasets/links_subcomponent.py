from components.base_subcomponent import BaseSubcomponent

from data.links_dataframe import get_links_dataframe

class LinksSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Links"
        self.dataframe = get_links_dataframe()
        self.column_number = "3"
        self.row_number = "27 278"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Nous avons constaté que la colonne **tmdbId** comporte 252 valeurs manquantes soit 0,92%.
        """)

    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors du prétraitement nous supprimerons la colonne **tmdbId** qui ne nous servir pas, tandis que la colonne **movieId**
        pourra être reliée à nos autres datasets de movielens et la colonne **imdbId** sera à transformer afin d’avoir les identifiants complets et pouvoir relier notre dataset movielens avec le dataset imdb.
        """)
