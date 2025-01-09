from components.base_subcomponent import BaseSubcomponent

from data.genome_scores_dataframe import get_genome_scores_dataframe

class GenomeScoresSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Genome-scores"
        self.dataframe = get_genome_scores_dataframe()
        self.column_number = "3"
        self.row_number = "11 709 768"
 
    def get_observation(self):
        return ("""
        **Observation :**     
        Le dataset ne contient aucune valeur manquante ni aucune valeur dupliquée.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors du prétraitement nous n'utiliserons pas ce dataset au vu de son contenu si voulons conserver une ligne par film nous ne garderons pas tous les tags de chaque film.
        """)
    


