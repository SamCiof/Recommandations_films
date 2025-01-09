import pandas as pd

def get_title_basics_dataframe():
    data = {
        "tconst": ["tt0000001", "tt0000002", "tt0000003", "tt0000004", "tt0000005"],
        "titleType": ["short", "short", "short", "short", "short"],
        "primaryTitle": ["Carmencita", "Le clown et ses chiens", "Pauvre Pierrot", "Un bon bock", "Blacksmith Scene"],
        "originalTitle": ["Carmencita", "Le clown et ses chiens", "Pauvre Pierrot", "Un bon bock", "Blacksmith Scene"],
        "isAdult": [0.0, 0.0, 0.0, 0.0, 0.0],
        "startYear": [1894.0, 1892.0, 1892.0, 1892.0, 1893.0],
        "endYear": [None, None, None, None, None],
        "runtimeMinutes": [1, 5, 5, 12, 1],
        "genres": ["Documentary,Short", "Animation,Short", "Animation,Comedy,Romance", "Animation,Short", "Comedy,Short"]
    }
    df = pd.DataFrame(data)
    return df
