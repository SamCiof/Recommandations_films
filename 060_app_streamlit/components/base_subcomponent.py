import streamlit as st

class BaseSubcomponent:
    def __init__(self):
        self.image = None

    def display(self):
        st.subheader(self.subtitle)
        st.dataframe(self.dataframe)
        if self.image:
            st.markdown(self.get_visualisation())
            st.image(image=f"images/{self.image}")
        st.markdown(self.get_information())
        st.markdown(self.get_observation())
        st.markdown(self.get_decision())
        
    def get_visualisation(self):
        return(f"""
        **{self.visualisation} :**
        """)

    def get_information(self):
        return(f"""
        **Information :**     
        Le jeu de données contenait {self.column_number} colonnes et {self.row_number} lignes.
        """)
    
    def get_observation(self):
        return ""    

    def get_decision(self):
        return ""  

