from views.base_page import BasePage
from components.exploration_donnees.introduction_component import IntroductionComponent
from components.exploration_donnees.imdb_datasets_component import ImdbDatasetsComponent
from components.exploration_donnees.movielens_datasets_component import MovielensDatasetsComponent

class ExplorationDonneesPagePage(BasePage): 
    def __init__(self):
        super().__init__()
        self.header_title = "Exploration des données"
        self.introduction = IntroductionComponent()
        self.imdb = ImdbDatasetsComponent()
        self.movielens = MovielensDatasetsComponent()
        self.chapters = {
            "Introduction": self.introduction,
            "Exploration des données IMDb" : self.imdb,
            "Exploration des données Movie Lens": self.movielens
        }
