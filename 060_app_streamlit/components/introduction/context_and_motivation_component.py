from components.base_component import BaseComponent

class ContextAndMotivationComponent(BaseComponent):
    def __init__(self):
        super().__init__("Contexte et motivation")

    def get_content(self):
        return """
        Les systèmes de recommandation sont devenus une composante essentielle des plateformes numériques modernes, jouant un rôle important dans la personnalisation de l'expérience utilisateur.
        Utilisés par des géants de la technologie comme Netflix, Amazon, et YouTube, ces systèmes aident à naviguer dans l'immense quantité de contenu disponible en proposant des recommandations
        personnalisées basées sur les préférences et les comportements passés des utilisateurs.

        Le présent rapport se propose d'explorer la conception et l'implémentation d'un modèle de recommandation en utilisant les ensembles de données fournis par IMDb et MovieLens.
        Pour ce faire, il s'appuiera sur les meilleures pratiques et les ressources offertes par la plateforme Datascientest, ainsi que sur les informations recueillies sur internet
        concernant les retours d’expérience menés par les géants de la technologie dans le domaine des systèmes de recommandation.
        """
