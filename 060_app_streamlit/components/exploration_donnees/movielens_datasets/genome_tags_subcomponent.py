from components.base_subcomponent import BaseSubcomponent

from data.genome_tags_dataframe import get_genome_tags_dataframe

class GenomeTagsSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Genome-tags"
        self.dataframe = get_genome_tags_dataframe()
        self.column_number = "2"
        self.row_number = "1 128"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Le dataset ne contient aucune valeur manquante ni aucune valeur dupliquée.
        """)

    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors du prétraitement nous n'utiliserons pas ce dataset non plus puisque nous utiliserons les tags du dataset tags comme indiqué précédemment.
        """)


