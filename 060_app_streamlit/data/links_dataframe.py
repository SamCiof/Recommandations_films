import pandas as pd

def get_links_dataframe():
    data = {
        "movieId": [1, 2, 3, 4, 5],
        "imdbId": [114709, 113497, 113228, 114885, 113041],
        "tmdbId": [862.0, 8844.0, 15602.0, 31357.0, 11862.0]
    }
    df = pd.DataFrame(data)
    return df
