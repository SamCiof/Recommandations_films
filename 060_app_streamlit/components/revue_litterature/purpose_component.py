from components.base_component import BaseComponent

class PurposeComponent(BaseComponent):
    def __init__(self):
        super().__init__("A quoi sert un système de recommandation ?")

    def get_content(self):
        return (
            """
            **Amélioration de l'expérience utilisateur** : En proposant du contenu pertinent et personnalisé, les utilisateurs sont plus susceptibles de trouver ce qu'ils recherchent et de découvrir de nouveaux contenus qu'ils apprécieront.
            
            **Augmentation de l'engagement et des revenus** : En gardant les utilisateurs engagés et en augmentant la probabilité qu'ils consomment plus de contenu ou achètent plus de produits, les systèmes de recommandation peuvent avoir un impact direct sur les revenus des entreprises.
            
            **Gestion et filtrage de l'information** : Dans un monde où l'information est abondante, les systèmes de recommandation aident à filtrer le bruit et à mettre en avant les éléments les plus pertinents.
            """
        )