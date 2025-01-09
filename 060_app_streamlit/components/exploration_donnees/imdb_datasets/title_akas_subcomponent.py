from components.base_subcomponent import BaseSubcomponent

from data.title_akas_dataframe import get_title_akas_dataframe

class TitleAkasSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Title akas"
        self.dataframe = get_title_akas_dataframe()
        self.visualisation ="Visualisation des colonnes ayant un fort taux de valeurs manquantes"
        self.image = "title_akas_proportion_of_zero_and_entered_values.png"
        self.column_number = "8"
        self.row_number = "48 459 150"

    def get_observation(self):
        return ("""
        **Observation :**      
        Nous avons observé que ce jeu de données n’apporte pas de plus-value pour le modèle de ML.
        Les colonnes censées fournir des informations supplémentaires sur les films contiennent énormément de valeurs manquantes. Par exemple,  sur l’échantillon analysé :
        * La colonne **types** a plus de 67% de valeurs manquantes.
        * La colonne **attributes** a plus de 99% de valeurs manquantes.
        * La colonne **language** a plus de 36% de valeurs manquantes.
        
        Cette quantité importante de valeurs manquantes limite l'utilité de ces colonnes dans notre analyse.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**       
        De surcroît, les titres alternatifs des films, bien qu'intéressants, ne sont pas essentiels pour l'objectif principal de notre modèle de recommandation.
        Ainsi, nous avons décidé de ne pas inclure ce dataset dans la phase de prétraitement des données.
        """)
