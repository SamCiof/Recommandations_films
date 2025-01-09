import streamlit as st

class BasePage:
    def __init__(self):
        pass

    def get_header(self, header_title):
        return f"<h1 style='text-align: center;'>{header_title}</h1>"
    
    def get_list_subheader(self, list_subheader="Chapitres"):
        return f"<p style='font-size: 1.6em; margin-bottom: 0px; padding-bottom: 0px;'>{list_subheader}</p>"
    
    def display_content(self, chapter):
        if chapter in self.chapters:
            self.chapters[chapter].display()
        else:
            st.error("Chapitre non trouvé.")
    
    def display(self):
        st.markdown(self.get_header(self.header_title), unsafe_allow_html=True)
        st.markdown(self.get_list_subheader(), unsafe_allow_html=True)

        chapter = st.radio("Select Chapter",
                           list(self.chapters.keys()), 
                           label_visibility="hidden")
 
        self.display_content(chapter)