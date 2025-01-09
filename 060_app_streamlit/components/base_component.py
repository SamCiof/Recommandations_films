import streamlit as st

class BaseComponent:
    def __init__(self, title):
        self.title = title

    def display(self):
        st.header(self.title)
        st.markdown(self.get_content(), unsafe_allow_html=True)

    def get_content(self):
        raise NotImplementedError("La méthode get_content doit être implémentée par les sous-classes.")
