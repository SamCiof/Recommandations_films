from views.base_page import BasePage
from components.transformation_donnees.introduction_component import IntroductionComponent
from components.transformation_donnees.imbd_datasets_component import ImdbDatasetsComponent
from components.transformation_donnees.movielens_datasets_component import MovielensDatasetsComponent
from components.transformation_donnees.dstrec_dataset_component import DstrecDatasetsComponent

class TransformationDonnePage(BasePage): 
    def __init__(self):
        super().__init__()
        self.header_title = "Prétraitement des données"
        self.introduction = IntroductionComponent()
        self.imdb = ImdbDatasetsComponent()
        self.movielens = MovielensDatasetsComponent()
        self.dstrec = DstrecDatasetsComponent()
        self.chapters = {
            "Introduction": self.introduction,
            "Prétraitement des données IMDb": self.imdb,
            "Prétraitement des données MovieLens": self.movielens,
            "Prétraitement final des données": self.dstrec
        }
    
