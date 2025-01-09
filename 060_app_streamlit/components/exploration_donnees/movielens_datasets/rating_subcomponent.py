from components.base_subcomponent import BaseSubcomponent

from data.rating_dataframe import get_rating_dataframe

class RatingSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Rating"
        self.dataframe = get_rating_dataframe()
        self.column_number = "4"
        self.row_number = "20 000 263"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Le dataset ne contient aucune valeur manquante ni aucune valeur dupliquée.
        """)

    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors du prétraitement comme précédemment nous supprimons la colonne **timestamp**.
        Nous ferons également une moyenne des notes obtenues par film pour réduire également le nombre de lignes et améliorer la lisibilité de notre dataset final.
        """)
    