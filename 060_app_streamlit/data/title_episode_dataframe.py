import pandas as pd

def get_title_episode_dataframe():
    data = {
        "tconst": ["tt0041951", "tt0042816", "tt0042889", "tt0043426", "tt0043631"],
        "parentTconst": ["tt0041038", "tt0989125", "tt0989125", "tt0040051", "tt0989125"],
        "seasonNumber": [1.0, 1.0, None, 3.0, 2.0],
        "episodeNumber": [9.0, 17.0, None, 42.0, 16.0]
    }
    df = pd.DataFrame(data)
    return df
