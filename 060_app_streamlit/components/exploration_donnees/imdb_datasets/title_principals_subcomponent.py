from components.base_subcomponent import BaseSubcomponent

from data.title_principals_dataframe import get_title_principals_dataframe

class TitlePrincipalsSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Title principals"
        self.dataframe = get_title_principals_dataframe()
        self.column_number = "6"
        self.row_number = "85 883 465"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Nous avons observé que le jeu de données ne contenait pas de valeurs dupliquées, les colonnes **job** et **characters** possèdent plus de 50% de valeurs manquantes,
        tandis que la colonne **ordering** n’apporte pas de plus-value pour la suite. Néanmoins, la colonne **category** pourrait être remodelée, pour inclure les noms des
        participants aux films dans les prédictions du modèle de machine learning, en particulier les acteurs et les producteurs.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Lors de la phase de prétraitement des données, nous extrairons les colonnes **job, characters** et **ordering**, puis effectuerons un remodelage (pivot) de la colonne **category**
        pour mieux structurer les données. Ensuite, nous extrairons les nouvelles colonnes inutiles ou qui contiennent beaucoup de valeurs manquantes telles que :
        **archive_footage, archive_sound, casting_director, cinematographer, composer, production_designer, self**.
        """)