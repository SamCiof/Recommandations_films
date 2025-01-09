import pandas as pd

def get_movielens_transformed_dataframe():
    data = {
        "title": [
            "Toy Story", 
            "Jumanji", 
            "Grumpier Old Men", 
            "Waiting to Exhale", 
            "Father of the Bride Part II"
        ],
        "genres": [
            "Adventure|Animation|Children|Comedy|Fantasy", 
            "Adventure|Children|Fantasy", 
            "Comedy|Romance", 
            "Comedy|Drama|Romance", 
            "Comedy"
        ],
        "imdbId": [
            "tt0114709", 
            "tt0113497", 
            "tt0113228", 
            "tt0114885", 
            "tt0113041"
        ],
        "averageRating": [7.8, 6.4, 6.4, 5.8, 6.2]
    }
    
    df = pd.DataFrame(data)
    return df
