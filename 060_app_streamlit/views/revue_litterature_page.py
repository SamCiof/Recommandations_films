from views.base_page import BasePage
from components.revue_litterature.recommendation_system_component import RecommendationSystemComponent
from components.revue_litterature.purpose_component import PurposeComponent
from components.revue_litterature.audience_component import AudienceComponent
from components.revue_litterature.how_it_works_component import HowItWorksComponent
from components.revue_litterature.advantages_limitations_component import AdvantagesLimitationsComponent
from components.revue_litterature.history_evolution_component import HistoryEvolutionComponent
from components.revue_litterature.netflix_algorithm_component import NetflixAlgorithmComponent

class RevueLitteraturePage(BasePage): 
    def __init__(self):
        super().__init__()
        self.header_title = "Revue de littérature"
        self.recommendation_system = RecommendationSystemComponent()
        self.purpose = PurposeComponent()
        self.audience = AudienceComponent()
        self.how_it_works = HowItWorksComponent()
        self.advantages_limitations = AdvantagesLimitationsComponent()
        self.history_evolution = HistoryEvolutionComponent()
        self.netflix_algorithm = NetflixAlgorithmComponent()

        self.chapters = {
            "Qu’est ce qu’un système de recommandation ?": self.recommendation_system,
            "A quoi sert un système de recommandation ?": self.purpose,
            "Pour qui ?": self.audience,
            "Comment fonctionnent les systèmes de recommandation basés sur le ML ?": self.how_it_works,
            "Quels sont les avantages et les limitations des systèmes de recommandation basés sur le ML ?": self.advantages_limitations,
            "Quelle est l’histoire et l’évolution du système de recommandation ?": self.history_evolution,
            "Comment fonctionne l’algorithme de Netflix ?": self.netflix_algorithm,
        }
