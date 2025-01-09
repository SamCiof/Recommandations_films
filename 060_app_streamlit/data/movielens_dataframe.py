import pandas as pd

def get_movieslens_dataframe():
    data = {
        "movieId": [1, 2, 3, 4, 5],
        "title": ["Toy Story", "Jumanji", "Grumpier Old Men", "Waiting to Exhale", "Father of the Bride Part II"],
        "genres": [
            "Adventure|Animation|Children|Comedy|Fantasy",
            "Adventure|Children|Fantasy",
            "Comedy|Romance",
            "Comedy|Drama|Romance",
            "Comedy"
        ],
        "imdbId": ["tt0114709", "tt0113497", "tt0113228", "tt0114885", "tt0113041"],
        "average_rating": [3.9, 3.2, 3.2, 2.9, 3.1],
        "most_common_tag": ["Pixar", "Robin Williams", "moldy", "chick flick", "steve martin"]
    }
    
    df = pd.DataFrame(data)
    df.set_index("movieId", inplace=True)
    return df
