from components.base_subcomponent import BaseSubcomponent

from data.title_crew_dataframe import get_title_crew_dataframe

class TitleCrewSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Title crew"
        self.dataframe = get_title_crew_dataframe()
        self.visualisation ="Visualisation des valeurs nulles pour les colonnes writers et directors"
        self.image = "title_crew_proportion_of_zero_and_entered_values.png"
        self.column_number = "3"
        self.row_number = "10 143 819"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Nous avons relevé que ce jeu de données n’apporte potentiellement pas de plus-value pour le modèle de ML. Les colonnes censées fournir des informations supplémentaires
        sur les directeurs et les auteurs des films contiennent énormément de valeurs manquantes. Par exemple :
                
        * La colonne **directors** a plus de 38% de valeurs manquantes.
        * La colonne **writers** a plus de 44% de valeurs manquantes.
        
        Cette quantité importante de valeurs manquantes limite l'utilité de ces colonnes dans notre analyse.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        En conséquence, nous avons décidé de ne pas inclure ce dataset dans la phase de prétraitement des données.
        """)
