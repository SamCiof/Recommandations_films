from components.base_component import BaseComponent

class HistoryEvolutionComponent(BaseComponent):
    def __init__(self):
        super().__init__("Quelle est l’histoire et l’évolution du système de recommandation ?")

    def get_content(self):
        return (
            """
            Le premier système de recommandation connu est Grundy, développé en 1979 par Elaine Alice Rich, une informaticienne américaine. Il utilisait des stéréotypes pour recommander des livres à des utilisateurs en se basant sur un modèle simple de filtrage collaboratif, où les recommandations étaient générées en analysant les achats et les évaluations des utilisateurs. Le système identifiait les utilisateurs aux goûts similaires et recommandait aux utilisateurs des produits que les utilisateurs similaires avaient appréciés. Bien que Grundy ait été conçu pour les produits en général, son succès a démontré le potentiel des systèmes de recommandation pour fournir des suggestions personnalisées et pertinentes aux utilisateurs. Le système a inspiré le développement de nombreux autres systèmes de recommandation, et ses principes de base sont encore utilisés aujourd'hui dans les systèmes modernes.
            
            Puis dans les années 1990, des modèles de recommandations plus complexes ont vu le jour, notamment le système de Tapestry développé par une équipe dirigée par David Goldberg. Le système se basait sur un filtrage collaboratif. Celui-ci effectuait une recherche en fonction du contenu et des réactions enregistrées des autres utilisateurs. Ou bien même le système de GroupLens créé par John Riedl et Paul Resnick, est l’un des premiers systèmes à utiliser le filtrage collaboratif automatisé pour recommander des articles de Usenet. Il utilisait les évaluations des utilisateurs pour prédire les évaluations d'autres utilisateurs pour les mêmes articles.
            
            Ensuite dans les années 2000, les modèles basés sur les matrices ont monté en puissance, principalement grâce un à géant de la technologie, Amazon, qui a introduit un système de recommandation basé sur les items, où les produits similaires sont recommandés en fonction de ce que d’autres clients ont acheté, contribuant de manière significative à la popularité du commerce électronique. Dans les années 2006, un autre géant de la technologie, Netflix, a introduit les modèles de factorisation de matrice, qui ont marqué une avancée majeure en permettant de capturer les interactions complexes entre utilisateurs et items en décomposant la matrice utilisateur-item en produits de matrices de rang inférieur.
            
            En 2010, les filtres collaboratifs neuronaux ont commencé à émerger, combinant les réseaux de neurones avec des techniques de filtrage collaboratif pour améliorer la précision des recommandations en capturant des relations non linéaires entre utilisateurs et items, et l'intégration de données provenant des réseaux sociaux a permis de raffiner les recommandations en tenant compte des relations sociales et des influences interpersonnelles.
            """
        )