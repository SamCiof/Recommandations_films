import os
import subprocess

def run_server(port=3200):
    """Lance le serveur Streamlit sur le port spécifié."""
    command = f"streamlit run app.py --server.port {port}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    port = os.getenv("STREAMLIT_PORT", 3200)
    run_server(port)