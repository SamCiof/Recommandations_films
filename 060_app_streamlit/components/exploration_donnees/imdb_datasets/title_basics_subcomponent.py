from components.base_subcomponent import BaseSubcomponent

from data.title_basics_dataframe import get_title_basics_dataframe

class TitleBasicsSubcompoment(BaseSubcomponent):
    def __init__(self) :
        super().__init__()
        self.subtitle = "Analyse du dataset Title basics"
        self.dataframe = get_title_basics_dataframe()
        self.visualisation ="Visualisation de la colonne genres"
        self.image = "title_basics_top_twenty_most_popular_genres.png"
        self.column_number = "9"
        self.row_number = "10 790 736"
 
    def get_observation(self):
        return ("""
        **Observation :**   
        Nous avons constaté que le jeu de données ne contenait pas de valeurs dupliquées, la colonne **endYear** indique l'année de fin pour les séries télévisées,
        la colonne **runtimeMinutes** possède 70% de valeurs manquantes, tandis que la colonne **originalTitle** a 99% de ses valeurs identiques à la colonne **primaryTitle**.
        """)


    def get_decision(self):
        return (""" 
        **Décision pour le prétraitement des données :**    
        Nous allons extraire les colonnes **originalTitle, endYear, runtimeMinutes** et **startYear** du jeu de données, filtrer uniquement les lignes où la colonne **titleType** contient
        le mot "movie", convertir la colonne **isAdult** en un type de genre dans la colonne genres, après un changement de typage préalable, extraire les doublons de la colonne **primaryTitle**.
        """)