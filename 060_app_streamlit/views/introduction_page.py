from views.base_page import BasePage
from components.introduction.context_and_motivation_component import ContextAndMotivationComponent
from components.introduction.objectives_component import ObjectivesComponent

class IntroductionPage(BasePage): 
    def __init__(self):
        super().__init__()
        self.header_title = "Introduction"
        self.context_and_motivation = ContextAndMotivationComponent()
        self.objectives = ObjectivesComponent()
        self.chapters = {
            "Contexte et motivation": self.context_and_motivation,
            "Objectifs": self.objectives
        }
