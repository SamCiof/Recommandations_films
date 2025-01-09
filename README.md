# DSTREC - Système de Recommandation de Films

Ce projet implémente un système de recommandation de films utilisant diverses techniques d'analyse de données et d'apprentissage automatique.

## Structure du Projet

```
├── 000_rapport
│   └── DSTREC_Système_de_Recommandation_de_film_V2.pdf
├── 010_data
│   ├── 000_source
│   ├── 001_transformed
│   └── 002_merged
├── 020_evaluation_des_donnees
│   ├── imdb_datasets
│   └── movielens
├── 030_datavisualisation_des_donnees
│   └── (plusieurs notebooks Jupyter de datavisualisation)
├── 040_transformation_des_donnees
│   ├── dstrec_dataset
│   ├── imdb_datasets
│   └── movielens
├── 050_modelisation_des_donnes
│   └── (plusieurs notebooks Jupyter de modélisation)
├── 060_app_streamlit
│   └── (fichiers de l'application Streamlit)
├── LICENSE
├── README.md
├── requirements.txt
└── venv
```

## Description des Dossiers

- `000_rapport`: Contient le rapport du projet.
- `010_data`: Stocke les données brutes, transformées et fusionnées.
- `020_evaluation_des_donnees`: Contient les évaluations des ensembles de données IMDb et MovieLens.
- `030_datavisualisation_des_donnees`: Notebooks Jupyter pour la visualisation des données.
- `040_transformation_des_donnees`: Scripts et données pour la transformation et le préprocessing des ensembles de données.
- `050_modelisation_des_donnes`: Notebooks Jupyter pour différentes approches de modélisation.
- `060_app_streamlit`: Application Streamlit pour la présentation et la démonstration du système de recommandation.

## Installation

1. Clonez ce dépôt : `git clone https://github.com/DataScientest-Studio/fev24_cds_recommandations`
2. Créez un environnement virtuel : `python -m venv venv`
3. Activez l'environnement virtuel :
   - Windows : `venv\Scripts\activate`
   - Unix ou MacOS : `source venv/bin/activate`
4. Installez les dépendances : `pip install -r requirements.txt`

## Utilisation

1. Préparez les données en exécutant les notebooks dans le dossier `040_transformation_des_donnees`.
2. Entraînez les modèles en utilisant les notebooks dans `050_modelisation_des_donnes`.
3. Lancez l'application Streamlit : `cd 060_app_streamlit` -> `python3 server.py` 

## Licence

Voir le fichier `LICENSE` pour plus d'informations.
