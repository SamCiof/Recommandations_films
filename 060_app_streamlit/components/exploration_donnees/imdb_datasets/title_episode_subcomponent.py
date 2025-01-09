from components.base_subcomponent import BaseSubcomponent

from data.title_episode_dataframe import get_title_episode_dataframe

class TitleEpisodeSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Title episode"
        self.dataframe = get_title_episode_dataframe()
        self.column_number = "4"
        self.row_number = "8 258 774"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Nous avons constaté que le pourcentage des **tconst** des lignes de la colonne **titleType** contenant la valeur **tvEpisode** du dataset **title.basics** étaient présents à 99.97% dans ce jeu de données.
        En outre, cela nous a permis de confirmer que le jeu de données **title.episode** contenait exclusivement des informations sur les épisodes de séries de l'ensemble IMDb.
        """)

    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors de la phase de prétraitement des données, nous extrairons directement les données liées aux épisodes des séries à partir de **title.basics**, sans avoir besoin du jeu de données **title.episode**.
        """)
