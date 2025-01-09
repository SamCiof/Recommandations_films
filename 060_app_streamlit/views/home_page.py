import streamlit as st
from views.base_page import BasePage

class HomePage(BasePage): 
    def __init__(self):
        super().__init__()
        self.header_title = "Développement d'un système de recommandation de film"

    def display(self):
        st.markdown(self.get_header(self.header_title), unsafe_allow_html=True)
        st.image(self.get_image_path(), use_column_width=True)

    def get_image_path(self):
        return "images/Content-based-filtering-vs-Collaborative-filtering-Source.png"
