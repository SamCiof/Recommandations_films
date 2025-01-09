import streamlit as st

from components.base_component import BaseComponent
from data.movielens_dataframe import get_movieslens_dataframe

class MovielensDatasetsComponent(BaseComponent):
    def __init__(self):
        super().__init__("Prétraitement des données MovieLens 20M")
        self.df_movielens = get_movieslens_dataframe()

    def display(self):
        st.header(self.title)
        st.markdown(self.get_dataset_choice())
        st.markdown(self.get_movies_preparing())
        st.markdown(self.get_links_preparing())
        st.markdown(self.get_ratings_preparing())
        st.markdown(self.get_tags_preparing())
        st.markdown(self.get_movielens_dataset_transformating())
        st.dataframe(self.df_movielens)


    def get_dataset_choice(self):
        return ("""
        ### Choix des datasets utilisés
        Comme nous l’avons indiqué précédemment nous faisons le choix de ne pas tenir compte des datasets genome-scores.csv et genome-tags.csv
        qui ne nous semblent pas pertinents pour la construction de notre dataset final et qui ne pourront être reliés aux données Imdb.
        Nous travaillerons donc sur les datasets **movies.csv, links.csv** et **ratings.csv**.
        """)
    
    def get_movies_preparing(self):
        return ("""
        ### Préparation du dataset movies
        Dans un premier temps nous nous occupons de la colonne **title**. Les valeurs de cette dernière sont composées comme suit : Titre du film (année), par exemple : Toy Story (1995).
        Par souci de simplicité et pour que les titres correspondent entre le jeu de données Movielens et Imdb nous décidons de supprimer l’année dans de nos titres. 
        
        Dans un second temps, nous conservons le reste des données sans apporter de modification : **movieId** et **genres**.
        """)
    
    def get_links_preparing(self):
        return ("""
        ### Préparation du dataset links
        Nous commençons dans ce dataset par supprimer la colonne **tmdbId** qui d’une part contient des valeurs manquantes et qui d'autre part ne nous servira pas car nous n’avons pas de données liées à tmdb.
        
        Concernant la colonne **imdbId** nous nous rendons compte qu’il y a un problème à résoudre. En effet les identifiants imdb sont normalement au format “tt0000000” (par exemple : tt0114709), or dans notre jeu de données les deux “t” et les “0” ont été supprimé pour ne garder que les chiffres composant la fin de l’identifiant (exemple : 114709).
        
        Afin que nos données comportent les véritables identifiants et que ceux-ci concordent avec le jeu de données Imdb nous transformons les valeurs de la colonne **imdbId** pour qu’elles respectent le format des identifiants imdb.
        """)
    
    def get_ratings_preparing(self):
        return ("""
        ### Préparation du dataset ratings
        Pour commencer nous décidons de supprimer la colonne **timestamp** qui ne nous sera pas utile dans notre jeu de données et pour notre modèle. 
        
        Comme indiqué précédemment nous souhaitons avoir une ligne par film, afin de réaliser cela nous ne pouvons donc pas garder toutes les notes pour chaque utilisateur. Nous décidons donc de créer une
        colonne **average_ratings** comportant la note moyenne pour chaque film. Une fois cette colonne créée nous la rajoutons à notre dataframe ratings et nous arrondissons la note moyenne à une décimale.
        
        Puis nous supprimons la colonne **rating** originale de notre dataframe.
        
        La note étant désormais la même pour toutes les lignes d’un même film, nous supprimons la colonne **userId** qui nous ne sera plus utile puisque nous avons supprimer la colonne contenant la note attribuée par le user.
        
        Afin d’être sûre de n’avoir qu’une ligne par film nous supprimons les doublons dans le dataframe ratings.
        """)
    
    def get_tags_preparing(self):
        return ("""
        ### Préparation du dataset tags
        Comme dans notre dataset ratings, nous supprimons la colonne **timestamp**.
        
        La colonne **tag** contient des valeurs manquantes, nous décidons simplement de supprimer les lignes contenant ces valeurs manquantes. 
       
        Dans la logique de nos précédents prétraitements nous souhaitons une ligne par film, afin d’aboutir à cela nous choisissons de rechercher le tag qui ressort le plus pour chaque film et de conserver ce dernier comme valeur
        dans une nouvelle colonne intitulée **most_common_tag**. Puis nous supprimons les colonnes **tag** et **userId** du dataframe original avant de supprimer les doublons pour conserver une ligne par film.
        """)
    
    def get_movielens_dataset_transformating(self):
        return ("""
        ### Création du dataset movielens
        Après avoir effectué les différentes phases de préparation ci-dessus, nous allons désormais passer à la préparation de notre dataset pour les données **movielens**.
        
        Nous procédons à la fusion de nos quatre dataframes nettoyés via la colonne *movieId** communes à ces différents datasets. Nous déterminons d’ailleurs **movieId** comme index de notre dataset movielens.
       
        Le jeu de données comporte 659 doublons dans la colonne title, nous décidons donc de supprimer ces doublons.
        
        Le dataset movielens final contient 5 colonnes et 18352 lignes, il ne comporte aucune donnée manquante. Nous sauvegardons le tout et l’enregistrons dans le fichier movielens.csv.

        **Affichage des premières lignes du nouveau dataset :**
        """)