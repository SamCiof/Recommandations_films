from components.base_subcomponent import BaseSubcomponent
import streamlit as st
from data.name_basics_dataframe import get_name_basics_dataframe

class NameBasicsSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Name basics"
        self.dataframe = get_name_basics_dataframe()
        self.visualisation ="Visualisation de la colonne primaryProfession"
        self.image = "name_basics_top_ten_most_common_professions.png"
        self.column_number = "6"
        self.row_number = "13 508 117"
 
    def get_observation(self):
        return ("""
        **Observation :**     
        Nous avons constaté qu'il ne contenait pas de valeurs dupliquées. Bien que ce jeu de données possédait de nombreuses valeurs manquantes, les colonnes **nconst** et **primaryName**, qui nous intéressaient particulièrement, ont moins de 0.0005% de valeurs manquantes.
        En outre, nous avons observé que les valeurs de la colonne **knownForTitles** n’étaient pas suffisamment explicites pour être exploitées dans les étapes suivantes de notre analyse.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**   
        Par conséquent, pour la phase de pré-traitement des données, nous avons décidé de conserver uniquement les colonnes **nconst** et **primaryName**.
        """)