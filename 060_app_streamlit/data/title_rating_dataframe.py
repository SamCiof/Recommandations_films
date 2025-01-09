import pandas as pd

def get_title_rating_dataframe():
    data = {
        "tconst": ["tt0000001", "tt0000002", "tt0000003", "tt0000004", "tt0000005"],
        "averageRating": [5.7, 5.7, 6.5, 5.4, 6.2],
        "numVotes": [2058, 276, 2015, 179, 2784]
    }
    df = pd.DataFrame(data)
    return df
