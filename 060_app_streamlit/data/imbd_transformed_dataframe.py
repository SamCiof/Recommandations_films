import pandas as pd

def get_imdb_transformed_dataframe():
    data = {
        "imdbId": ["tt0111161", "tt0468569", "tt1375666", "tt0137523", "tt0109830"],
        "titleType": ["movie", "movie", "movie", "movie", "movie"],
        "title": [
            "The Shawshank Redemption", 
            "The Dark Knight", 
            "Inception", 
            "Fight Club", 
            "Forrest Gump"
        ],
        "genres": [
            "Drama", 
            "Action,Crime,Drama", 
            "Action,Adventure,Sci-Fi", 
            "Drama", 
            "Drama,Romance"
        ],
        "averageRating": [9.3, 9.0, 8.8, 8.8, 8.8],
        "numVotes": [2896494.0, 2877871.0, 2557396.0, 2330795.0, 2263456.0],
        "actor": [
            "Tim Robbins", 
            "Christian Bale", 
            "Leonardo DiCaprio", 
            "Brad Pitt", 
            "Tom Hanks"
        ],
        "actress": [
            None, 
            "Maggie Gyllenhaal", 
            "Marion Cotillard", 
            "Eugenie Bondurant", 
            "Robin Wright"
        ],
        "composer": [
            "Thomas Newman", 
            "James Newton Howard", 
            "Hans Zimmer", 
            "John King", 
            "Alan Silvestri"
        ],
        "director": [
            "Frank Darabont", 
            "Christopher Nolan", 
            "Christopher Nolan", 
            "David Fincher", 
            "Robert Zemeckis"
        ],
        "producer": [
            "Niki Marvin", 
            "Christopher Nolan", 
            "Christopher Nolan", 
            "Ross Grayson Bell", 
            "Steve Tisch"
        ]
    }
    
    df = pd.DataFrame(data)
    return df
