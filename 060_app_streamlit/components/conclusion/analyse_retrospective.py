from components.base_component import BaseComponent

class AnalyseRetrospectiveComponent(BaseComponent):
    def __init__(self):
        super().__init__("Analyse retrospective")

    def get_content(self):
        return """
        L’un des enseignements que nous pourrions faire est l’importance de bien connaître les données que l’on exploite. La phase d’exploration des données est essentielle et détermine la réussite du projet. La phase de prétraitement des données est également primordiale car de ce jeu de données final dépendra la qualité des résultats obtenus suite aux modélisations.

        En outre, le choix minutieux des caractéristiques du modèle de machine learning s'est avéré essentiel pour obtenir des résultats pertinents et en adéquation avec nos objectifs.

        """
