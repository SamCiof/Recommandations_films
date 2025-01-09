import streamlit as st

class Sidebar:
    def __init__(self):
        self.sidebar_title = "Sommaire"

    def display(self, routes):
        st.sidebar.markdown(self.get_sidebar_title(), unsafe_allow_html=True)
        st.sidebar.radio("Sommaire", routes, format_func=lambda x: x["title"], key="selected_page", label_visibility="hidden")
        st.sidebar.markdown(self.get_project_info(), unsafe_allow_html=True)

    def get_sidebar_title(self):
        return f"<h2 style='margin-bottom: 0px; padding-bottom: 0px;'>{self.sidebar_title}</h2>"
    
    def get_project_info(self):
        return """
        <div style='margin-top: 20px; padding: 10px; border: 1px solid #A9CEF4; border-radius: 10px; background-color: #A9CEF492;'>
            <h3>DataScientest - Projet recommandations : Promotion DS continu février 2024</h3>
            <h4>Participants :</h4>
            <ul style='list-style-type: none; padding: 0;'>
                <li>Andrew</li>
                <li>Rachelle</li>
                <li>Samantha</li>
            </ul>
            <h4>Github :</h4> https://github.com/DataScientest-Studio/fev24_cds_recommandations 
        </div>
        """
