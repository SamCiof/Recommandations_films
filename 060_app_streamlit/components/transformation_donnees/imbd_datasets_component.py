import streamlit as st

from components.base_component import BaseComponent
from data.imdb_dataframe import get_imdb_dataframe

class ImdbDatasetsComponent(BaseComponent):
    def __init__(self):
        super().__init__("Prétraitement des données IMDb")
        self.df_imdb = get_imdb_dataframe()

    def display(self):
        st.header(self.title)
        st.markdown(self.get_loading_data())
        st.markdown(self.get_title_basics_preparing())
        st.markdown(self.get_name_basics_preparing(), unsafe_allow_html=True)
        st.markdown(self.get_title_principals_preparing())
        st.markdown(self.get_title_principals_transformating(), unsafe_allow_html=True)
        st.markdown(self.get_imdb_dataset_transformating_first_part(), unsafe_allow_html=True)
        st.dataframe(self.df_imdb)
        st.markdown(self.get_imdb_dataset_transformating_second_part(), unsafe_allow_html=True)

    def get_loading_data(self):
        return ("""
        ### Chargement des données
        Lors du prétraitement des données IMDb, nous avons rencontré la même problématique à celle de la phase d'exploration en raison de la quantité massive de données à traiter.
        Cependant, contrairement à la phase précédente, nous ne pouvions pas utiliser le paramètre nrows car nous devions traiter l'ensemble des données disponibles.


        **Considération technique :**   
        Nous avons envisagé d'utiliser une base de données pour gérer les opérations, mais nous avons rapidement constaté que dès le premier fichier cela prenait énormément de temps.
        Nous avons également envisagé d'utiliser la librairie Dask, qui est capable de gérer des datasets plus grands que la mémoire disponible et d'exécuter des tâches en parallèle.
        Cependant, les opérations de réduction de données prévues allaient diminuer considérablement le volume des données. De plus, nous avions constamment besoin de visualiser les
        résultats, ce qui est plus simple et pratique avec Pandas. Pandas est également mieux optimisée pour des jeux de données qui peuvent être entièrement chargés en RAM.
        
        **Solution adoptée :**  
        Nous avons finalement opté pour l'utilisation de Pandas avec des boucles utilisant le paramètre chunksize. Cette approche permet de charger progressivement de grandes quantités
        de données sans dépasser la mémoire disponible. Néanmoins, entre chaque notebook, il nous a été essentiel de réactualiser le kernel pour libérer la mémoire et pouvoir continuer
        les opérations dans les notebooks suivants, afin d’éviter les problèmes de mémoire saturée et pour garantir un flux de travail fluide.
        """)
    
    def get_title_basics_preparing(self):
        return ("""
        ### Préparation du dataset Title basics
        
        **Chargement des données :**    
        Pendant le chargement des données du jeu de données title.basics, nous avons utilisé la fonction clean_and_filter_data. Celle-ci a supprimé les colonnes à extraire identifiées
        lors de la phase d'exploration des données, elle a transformé le typage de la colonne isAdult, afin qu’elle puisse par la suite l'insérer en un type de genre dans la colonne
        genres. Puis la fonctionne a supprimé la colonne isAdult. Ensuite, elle a filtré les lignes pour ne conserver que celles où la colonne titleType avait la valeur movie. Et enfin
        elle a fusionné le dataset title.basics avec celui de title.ratings afin d'inclure les informations de notation des films.

        **Suppression des valeurs manquantes et dupliquées :**     
        Nous avons ensuite procédé à la suppression des valeurs manquantes pour garantir la qualité des données et avons géré les doublons en utilisant le nombre de votes (numVotes) comme
        critère de filtrage, conservant uniquement la ligne avec le plus grand nombre de votes en cas de doublon.

        
        **Vérification et sauvegarde des données :**    
        Après ces étapes de nettoyage, nous avons effectué des analyses supplémentaires pour nous assurer que toutes les transformations et suppressions avaient été correctement appliquées et
        que le dataset était prêt pour la transformation des données. Puis, nous les avons sauvegardées dans un fichier CSV.
        
        En outre, nous avons créé un fichier CSV supplémentaire contenant uniquement la colonne tconst avec les mêmes lignes que le dataset principal. Cette approche permet d'optimiser les 
        performances et de réduire l'utilisation de la RAM pour les prochaines étapes de préparation des données des autres datasets.

        """)
    
    def get_name_basics_preparing(self):
        return ("""
        <h3>Préparation du dataset Name basics</h3>     
        <b>Chargement des données :</b><br>
        Lors du chargement des données du jeu de données <b>name.basics</b>, nous avons décidé d’exclure les colonnes identifiées comme à extraire lors de la phase d'exploration des données : <b>birthYear, deathYear, primaryProfession, knownForTitles.</b>
        <br><br><b>Affichage des premières lignes du nouveau dataset :</b><br>     
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:55%;">nconst</th>
                    <th style="width:45%;">primaryName</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>nm0000001</td>
                    <td>Fred Astaire</td>
                </tr>
                <tr>
                    <td>nm0000002</td>
                    <td>Lauren Bacall</td>
                </tr>
            </tbody>
        </table>        
        <b>Sauvegarde des données :</b> 
        <br>Après la suppression des colonnes non désirées pour le reste des opérations, nous avons sauvegardé le nouveau jeu de données dans un fichier CSV.<br>
        Ces étapes nous ont permis de simplifier le dataset <b>name.basics</b> en ne conservant que les informations essentielles (<b>nconst</b> et <b>primaryName</b>), facilitant ainsi les opérations futures et optimisant l'efficacité du traitement des données.<br><br>
        """)
    
    def get_title_principals_preparing(self):
        return ("""
        ### Préparation du dataset Title principals
        
        **Chargement des données :**    
        Lors du chargement des données du jeu de données **title.principals**, nous avons chargé uniquement les lignes correspondantes aux lignes du dataset **title_basics_tconst** contenant la colonne **tconst**. 
        
        **Sauvegarde des données :**    
        Après avoir filtré les données, nous avons sauvegardé ce nouveau jeu de données dans un fichier CSV. Cette sauvegarde permet d'assurer une utilisation cohérente et efficace de ces données filtrées pour les étapes ultérieures du processus.
        """)
    
    def get_title_principals_transformating(self):
        return ("""
        <h3>Transformation du dataset Title principals</h3>     
        <b>Chargement des données :</b><br>
        Après le chargement des données du jeu de données <b>title.principals</b>, nous l’avons mergé avec le dataset <b>name.basics</b> via la colonne <b>nconst</b>. Au cours de cette fusion, nous avons supprimé les colonnes <b>ordering, job</b> et <b>characters</b>, jugées inutiles pour la suite de l’analyse. Ensuite, nous avons également supprimé la colonne <b>nconst</b> qui n'était plus nécessaire après la fusion.
        <br><br><b>Affichage des premières lignes du nouveau dataset :</b><br>     
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:33%;">tconst</th>
                    <th style="width:33%;">category</th>
                    <th style="width:33%;">primaryName</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>tt0000009</td>
                    <td>actress</td>
                    <td>Blanche Bayliss</td>
                </tr>
                <tr>
                    <td>tt0000009</td>
                    <td>direc</td>
                    <td>Alexander Black</td>
                </tr>
            </tbody>
        </table>        
        <b>Remodelage (pivot) de la colonne category :</b> 
        <br>Nous avons remodelé la colonne <b>category</b> en utilisant les valeurs de la colonne <b>primaryName</b>. Cette opération a permis de transformer les catégories en nouvelles colonnes,
        avec les noms des participants correspondants. Après cette transformation, nous avons analysé et vérifié les nouvelles colonnes créées à partir des valeurs de la colonne <b>category</b>.
        Nous avons extrait les colonnes qui contenaient soit une grande quantité de valeurs manquantes, soit celles qui n'apportaient pas de plus-value.<br><br>
        <b>Sauvegarde des données :</b> 
        <br>Puis, nous avons sauvegardé le nouveau jeu de données transformé dans un fichier CSV.<br><br>
        """)
    
    def get_imdb_dataset_transformating_first_part(self):
        return ("""
        <h3>Transformation du dataset IMDb</h3>     
        <b>Chargement des données :</b><br>
        Dans cette dernière étape des transformations du jeu de données d’IMDb, nous avons chargé et fusionné le dataset <b>title.principals</b> avec <b>title.basics</b>, rassemblant ainsi toutes les données souhaitées pour l’union avec le jeu de données <b>MovieLens</b>.
        <br><br><b>Affichage des premières lignes du nouveau dataset :</b><br>     
        """)
    
    def get_imdb_dataset_transformating_second_part(self):
        return ("""        
        <b>Sauvegarde des données :</b> 
        <br>Puis, nous avons sauvegardé le nouveau jeu de données transformé dans un fichier CSV.<br><br>
        """)
    