from components.base_subcomponent import BaseSubcomponent

from data.movies_dataframe import get_movies_dataframe

class MoviesSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Movies"
        self.dataframe = get_movies_dataframe()
        self.column_number = "3"
        self.row_number = "27 278"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Le dataset ne contient aucune valeur manquante ni aucune valeur dupliquée.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Ce jeu de données contient des éléments essentiels pour notre système de données,
        nous le gardons donc pour le prétraitement des données. La colonne **movieId** nous permettra d’ailleurs de le relier aux autres datasets de movielens.
        """)
