import streamlit as st
from views.home_page import HomePage
from cache.annoy_cache import load_data_and_model
from views.introduction_page import IntroductionPage
from views.revue_litterature_page import RevueLitteraturePage
from views.exploration_donnees_page import ExplorationDonneesPagePage
from views.transformation_donnees_page import TransformationDonnePage
from views.exploitation_donnees_page import ExploitationDonneesPagePage
from views.conclusion_page import ConclusionPage
from views.demonstration_page import DemonstrationPage

class Router:
    def __init__(self):
        self.df, self.t = load_data_and_model()
        self.routes = {
            "home": {"title": "Présentation", "view": HomePage()},
            "introduction": {"title": "Introduction", "view": IntroductionPage()},
            "revue_litterature":{"title": "Revue littérature", "view": RevueLitteraturePage()},
            "exploration_donnees":{"title": "Exploration des données", "view": ExplorationDonneesPagePage()},
            "transformation_donnees":{"title": "Prétraitement des données", "view": TransformationDonnePage()},
            "exploitation_donnees":{"title": "Exploitation des données", "view": ExploitationDonneesPagePage()},
            "demonstration":{"title": "Démonstration", "view": DemonstrationPage(self.df, self.t)},
            "conclusion":{"title": "Conclusion", "view": ConclusionPage()},
        }

    def get_routes(self):
        return [{"key": key, "title": route["title"]} for key, route in self.routes.items()]

    def render_page(self, page_key):
        if page_key in self.routes:
            self.routes[page_key]["view"].display()
        else:
            st.error("Page non trouvée.")
