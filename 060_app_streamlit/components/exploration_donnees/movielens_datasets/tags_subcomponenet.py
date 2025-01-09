from components.base_subcomponent import BaseSubcomponent

from data.tags_dataframe import get_tags_dataframe

class TagsSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Tags"
        self.dataframe = get_tags_dataframe()
        self.column_number = "4"
        self.row_number = "465 564"
 
    def get_observation(self):
        return ("""
        **Observation :**    
        Les colonnes **userId, movieId et timestamp** ne contiennent aucune valeur nulle. La colonne **tag** contient 16 valeurs non renseignées,
        le taux de remplissage de cette variable est de 99,99%.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors de la phase de prétraitement nous procéderons à la suppression de la colonne **timestamp** qui ne nous sera pas utile pour la suite.
        Nous tenterons également de réduire le nombre de ligne en ne gardant qu’une ligne par film avec le tag le plus utilisé sans tenir compte des userId.
        """)
