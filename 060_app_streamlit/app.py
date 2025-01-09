import streamlit as st
from router.router import Router
from components.sidebar.sidebar_component import Sidebar


class MyApp:
    def __init__(self):
        self.router = Router()
        self.sidebar = Sidebar()

    def run(self):
        custom_css = """
        <style>
        .st-emotion-cache-13ln4jf {
            max-width: 52rem;
        }
        img {
            max-width: 46rem;
        }
        </style>
        """

        st.markdown(custom_css, unsafe_allow_html=True)
        self.sidebar.display(self.router.get_routes())
        page = st.session_state.get("selected_page", "home")
        self.router.render_page(page["key"])

if __name__ == "__main__":
    app = MyApp()
    app.run()
