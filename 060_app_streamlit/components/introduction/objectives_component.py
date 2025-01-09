from components.base_component import BaseComponent

class ObjectivesComponent(BaseComponent):
    def __init__(self):
        super().__init__("Objectifs")

    def get_content(self):
        return (
            """
            **Création d'un système de recommandation**
            - Analyser et préparer les ensembles de données IMDb et MovieLens pour la modélisation.
            - Implémentation d’un système de recommandation pour générer des recommandations personnalisées basées sur les comportements et les préférences des utilisateurs.
            - Consolidation d'un jeu de données en utilisant des techniques de web scraping pour enrichir les données disponibles et améliorer la précision du modèle, si nécessaire.

            **Rapports d'exploration, de data visualisation et de pre-processing des données**
            - Réalisation d'un rapport détaillé d'exploration des données, mettant en évidence les tendances, les corrélations et les caractéristiques significatives du jeu de données.
            - Utilisation de techniques de data visualisation pour présenter de manière efficace les informations extraites des données.
            - Mise en œuvre de processus de pre-processing des données pour nettoyer, transformer et préparer les données en vue de leur utilisation dans la modélisation.

            **Rapport de modélisation**
            - Développement et entraînement d'un modèle de recommandation basé sur le machine learning.
            - Évaluation approfondie de la performance du modèle, en utilisant des métriques pertinentes et en comparant ses résultats avec des modèles de référence.

            **Rapport final et GitHub associé**
            - Compilation de tous les résultats, analyses et conclusions dans un rapport final détaillé.
            - Publication du code source, des scripts et des documents associés sur GitHub pour une transparence et une reproductibilité maximales des résultats obtenus.
            """
        )