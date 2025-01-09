from views.base_page import BasePage
from components.conclusion.difficultes_rencontrees import DifficultesRencontresComponent
from components.conclusion.resultats_obtenus import ResultatsObtenusComponent
from components.conclusion.analyse_retrospective import AnalyseRetrospectiveComponent
from components.conclusion.perspectives_amelioration import PerspectivesAmeliorationComponent
from components.conclusion.montee_en_competence import MonterEnCompetenceComponent

class ConclusionPage(BasePage): 
    def __init__(self):
        super().__init__()
        self.header_title = "Conclusion"
        self.difficultes_rencontrees = DifficultesRencontresComponent()
        self.resultats_obtenus = ResultatsObtenusComponent()
        self.analyse_retrospective = AnalyseRetrospectiveComponent()
        self.perspectives_amelioration = PerspectivesAmeliorationComponent()
        self.montee_en_competence = MonterEnCompetenceComponent()
        self.chapters = {
            "Résultats obtenus": self.resultats_obtenus,
            "Difficultés rencontrés": self.difficultes_rencontrees,
            "Analyse retrospective": self.analyse_retrospective,
            "Perspectives d'amélioration": self.perspectives_amelioration,
            "Monter en compétence": self.montee_en_competence
        }




