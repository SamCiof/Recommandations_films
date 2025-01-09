from components.base_subcomponent import BaseSubcomponent

from data.title_rating_dataframe import get_title_rating_dataframe

class TitleRatingSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Title rating"
        self.dataframe = get_title_rating_dataframe()
        self.visualisation ="Visualisation de la distribution de la note moyenne des films"
        self.image = "title_rating_bloxplot_of_average_scores.png"
        self.column_number = "3"
        self.row_number = "1 439 968"
 
    def get_observation(self):
        return ("""
        **Observation :**      
        Nous avons relevé que le jeu de données ne contenait pas de valeurs dupliquées et ne possédait pas de valeurs manquantes,
        et qu’il nous permet de connaître les notes attribuées aux films par les utilisateurs.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors de la phase de prétraitement des données, aucune action spécifique n'est nécessaire pour ce dataset jusqu'à la phase de fusion entre IMDb et MovieLens.
        """)
    