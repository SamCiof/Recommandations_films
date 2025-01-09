from components.base_component import BaseComponent

class ResultatsObtenusComponent(BaseComponent):
    def __init__(self):
        super().__init__("Résultats obtenus")

    def get_content(self):
        return """
        Notre système de recommandation de films, développé en utilisant les ensembles de données IMDb et MovieLens, a démontré une capacité prometteuse à personnaliser les suggestions de films basées sur les préférences des utilisateurs et les similarités avec des films qui ont été aimés par les utilisateurs eux-mêmes. Grâce à des méthodes avancées de traitement de données et de machine learning ainsi que des tests de différents modèles, le système a réussi à offrir des recommandations pertinentes, ce qui constitue une avancée significative vers une expérience utilisateur enrichie et personnalisée.

        Nous avons mis à profit les connaissances acquises durant les cours et même au-delà, car nous nous sommes également documentés sur d’autres méthodes existantes.

        Et le résultat obtenu a été un succès. Le modèle choisi, Annoy, a particulièrement mis en évidence son efficacité et sa robustesse lors des tests, tout en se distinguant par sa rapidité d'exécution et ses faibles exigences en termes de ressources matérielles par rapport aux autres modèles testés.

        En outre, grâce à l'efficacité de l'équipe, nous avons non seulement pu finaliser les livrables du projet bien avant la date prévue pour la soutenance, mais également mener à bien des tâches supplémentaires, telle que l’analyse de l’interprétabilité du modèle.

        """
