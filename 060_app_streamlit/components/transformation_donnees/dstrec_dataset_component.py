import streamlit as st

from components.base_component import BaseComponent
from data.imbd_transformed_dataframe import get_imdb_transformed_dataframe
from data.movielens_transformed_dataframe import get_movielens_transformed_dataframe
from data.dstrec_dataframe import get_dstrec_dataframe

class DstrecDatasetsComponent(BaseComponent):
    def __init__(self):
        super().__init__("Prétraitement final des données")
        self.df_imdb = get_imdb_transformed_dataframe()
        self.df_movielens = get_movielens_transformed_dataframe()
        self.dstrec = get_dstrec_dataframe()

    def display(self):
        st.header(self.title)
        st.markdown(self.get_introduction())
        st.markdown(self.get_imdb_preparing(), unsafe_allow_html=True)
        st.dataframe(self.df_imdb)
        st.markdown(self.get_movielens_preparing(), unsafe_allow_html=True)
        st.dataframe(self.df_movielens)
        st.markdown(self.get_df_merging(), unsafe_allow_html=True)
        st.dataframe(self.dstrec)

    def get_introduction(self):
        return("""
        Au sein de ce prétraitement final notre objectif sera de nettoyer les deux datasets précédemment créés pour ensuite les fusionner et transformer nos données.

        Ces étapes nous permettront ainsi d’obtenir notre jeu de données final, jeu qui sera utilisé pour notre modélisation.

        """)
    
    def get_imdb_preparing(self):
        return ("""
        <h3>Préparation des données de IMDb</h3>     
        Dans un premier temps nous affichons les données manquantes du dataset <b>imdb</b> pour avoir une vision des éléments qui devront être revus pendant ce prétraitement :</b><br>     
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:55%;">Nom de la colonne</th>
                    <th style="width:45%;">Nombre de valeur(s) manquante(s)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>tconst</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>titleType</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>primaryTitle</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>genres</td>
                    <td>59 214</td>
                </tr>
                <tr>
                    <td>averageRating</td>
                    <td>297 910</td>
                </tr>
                <tr>
                    <td>numVotes</td>
                    <td>297 910</td>
                </tr>
                <tr>
                    <td>actor</td>
                    <td>159 729</td>
                </tr>
                <tr>
                    <td>actress</td>
                    <td>194 922</td>
                </tr>
                <tr>
                    <td>composer</td>
                    <td>301 291</td>
                </tr>
                <tr>
                    <td>director</td>
                    <td>46 632</td>
                </tr>
                <tr>
                    <td>producer</td>
                    <td>204 624</td>
                </tr>
            </tbody>
        </table>    
        Notre jeu de données actuelles comporte à ce stade 572 547 lignes et 11 colonnes.<br>     
        <br><b>Suppression des lignes dont la valeur averageRating est manquante :</b> 
        <br>Au regard de la taille de notre jeu de données, nous faisons le choix de supprimer les lignes dont la note moyenne est absente car cette note va être l’une des valeurs les plus importantes pour notre modèle de recommandation de films.
        <br>Suite à ce retrait, notre jeu de données présente désormais 274 637 lignes et 11 colonnes.<br>
        <br><b>Renommage des colonnes :</b> 
        <br>Afin de prédire la suite de notre transformation des données nous renommons dès maintenant les colonnes du dataset imdb afin que les noms des colonnes correspondent au dataset movielens et soient compréhensibles de tous. Ainsi <b>tconst</b> devient <b>imdbId</b> et <b>primaryTitle</b> devient <b>title</b>.<br>
        <br><b>Suppression des colonnes titleType et composer :</b> 
        <br>Pour notre objectif de création d’un modèle de recommandation nous estimons que les colonnes <b>titleType</b> et <b>composer</b> ne nous seront pas utiles, nous décidons donc de supprimer directement ces colonnes.<br>
        <br><b>Affichage des premières lignes du nouveau dataset :</b>
        """)
    
    def get_movielens_preparing(self):
        return ("""
        <h3>Préparation des données de MovieLens</h3>     
        Tout comme pour imdb nous commençons par afficher les données manquantes de ce dataset afin d’avoir une vision des éventuels problèmes à résoudre :</b><br>     
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:55%;">Nom de la colonne</th>
                    <th style="width:45%;">Nombre de valeur(s) manquante(s)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>movieId</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>title</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>genres</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>imdbId</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>average_rating</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>most_common_tag</td>
                    <td>0</td>
                </tr>
            </tbody>
        </table>    
        Notre jeu de données comporte à ce stade 18 352 lignes et 5 colonnes sans aucune valeur manquante.<br>     
        <br><b>Suppression des colonnes most_common_tag et movieId :</b> 
        <br>La colonne <b>movieId</b> ne nous servira plus car elle n’est pas commune avec les données <b>imdb</b> , celle-ci nous a permis uniquement de regrouper nos données movielens à l’étape précédente.
        <br>Quant à la colonne <b>most_common_tag</b> nous faisons le choix de ne pas la garder car nous estimons que celle-ci ne nous servira pas dans le cadre de la modélisation.<br>
        
        <br><b>Renommage des colonnes :</b> 
        <br>Comme pour les données <b>imdb</b> nous voulons que les colonnes soient claires et communes, nous procédons donc à la modification de la colonne <b>average_rating</b> en <b>averageRating</b>.<br>
        
        <br><b>Reformatage de la colonne averageRating :</b>
        <br>Dans le jeu de données <b>movielens</b> nos notes moyennes sont sur 5 alors que dans le jeu de données <b>imdb</b> ces dernières sont sur 10. Dans un souci de clarté et de cohérence nous multiplions par deux les notes moyennes de <b>movielens</b> afin qu’elles soient également sur 10.<br>
        <br><b>Affichage des premières lignes du nouveau dataset :</b>
        """)
    
    def get_df_merging(self):
        return ("""
        <h3>Fusion des deux jeux de données</h3>     
        Avant de procéder à la fusion finale de nos deux datasets nous avons effectué des tests afin de voir si des lignes (correspondant à un film) sont communes au deux jeux de données.
        Ceci nous a indiqué que seuls 2 343 lignes présentes dans <b>movielens</b> ne sont pas communes avec <b>imdb</b>. Nous traiterons plus bas le sort de ces lignes.</b><br>     
        <br><b>Fusion des deux jeux de données et gestion des colonnes communes :</b> 
        <br>Nous procédons à la fusion des jeux <b>imdb</b> et <b>movielens</b> via la colonne <b>imdbId</b>. Concernant les colonnes communes, sachant que la note <b>imdb</b> est reliée à un nombre de vote pour ne pas fausser les données nous garderons la note <b>imdb</b>.
        La données <b>IMDB</b> étant la plus fiable en termes de recherche de film, nous décidons de prioriser la donnée <b>imdb</b> pour les films se trouvant dans les deux datasets pour les colonnes communes. Nous supprimons les colonnes que nous avions créées lors de la fusion.<br>
        Nous décidons également de supprimer les 2 343 lignes qui ne se trouvaient que dans le dataset movielens car ces dernières ne comportent pas de valeurs pour les autres colonnes de notre dataset et risqueraient donc de complexifier notre travail.<br>          
        <br><b>Vérification des doublons :</b> 
        <br>Nous constatons que nous n’avons pas de doublons après la fusion et les traitements effectués sur celle-ci.<br>       
        <br><b>Gestion des valeurs manquantes :</b> 
        <br>Une fois la fusion effectuée nous nous intéressons aux valeurs manquantes de notre jeu de données :<br>   
        <table style="width:100%; border-collapse: collapse; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="width:55%;">Nom de la colonne</th>
                    <th style="width:45%;">Nombre de valeur(s) manquante(s)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>imdbId</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>numVotes</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>actor</td>
                    <td>37 037</td>
                </tr>
                <tr>
                    <td>actress</td>
                    <td>49 541</td>
                </tr>
                <tr>
                    <td>director</td>
                    <td>4 323</td>
                </tr>
                <tr>
                    <td>producer</td>
                    <td>66 793</td>
                </tr>
                <tr>
                    <td>title</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>genres</td>
                    <td>8 526</td>
                </tr>
                <tr>
                    <td>averageRating</td>
                    <td>0</td>
                </tr>
            </tbody>
        </table>    
        Au vu du grand nombre de lignes dans notre jeu de données, nous décidons tout simplement de supprimer les lignes contenant des valeurs manquantes afin d’avoir un dataset propre et sans valeur manquante afin que le modèle puisse fonctionner au mieux.
        Nous supprimons ainsi les lignes dont les valeurs sont manquantes dans les colonnes <b>genres, director, actor, actress et producer.</b><br>
        Notre jeu de données contient désormais 164 108 lignes et 9 colonnes.<br>     
        <br><b>Fusion des colonnes actor et actress :</b> 
        <br>Pour des raisons de simplicité et de lisibilité nous préférons regrouper les colonnes <b>actor</b> et <b>actress</b> sous la forme <b>actor/actress</b> afin d’avoir dans la même colonne l’acteur et l’actrice principale du film. On crée ainsi la colonne <b>actor_actress</b> et supprimons les colonnes de base.<br>        
        <br><b>Réorganisation du jeu de données :</b> 
        <br>Afin d’avoir un ordre de colonne cohérent et avant de procéder à la transformation de la colonne <b>genres</b>, nous ré-organisons l’ordre de nos colonnes dans le dataset comme suit : <b>'imdbId', 'title', 'genres', 'averageRating', 'numVotes', 'director', 'actor_actress', 'producer'.</b><br>
        <br><b>Transformation de la colonne genres en booléens :</b> 
        <br>Afin de faciliter le travail de notre futur modèle de recommandation, nous transformons la colonne genres en booléens. Pour ce faire nous cherchons toutes les valeurs prises par la colonne genre en prenant en compte le fait que plusieurs genres peuvent être attribués à un même film en utilisant notamment
        les fonctions split pour séparer les genres et get_dummies pour créer les colonnes booléennes. Pour finir cette étape nous supprimons les colonnes qui nous ont permis de faire cette transformation.<br>
        <br><b>Création du fichier final :</b> 
        <br>Nous enregistrons notre dataset final sous le nom dstrec.csv.<br>
        <br><b>Affichage des premières lignes du dataset final :</b>
        """)