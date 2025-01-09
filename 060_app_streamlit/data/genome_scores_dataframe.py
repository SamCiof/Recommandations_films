import pandas as pd

def get_genome_scores_dataframe():
    data = {
        "movieId": [1, 1, 1, 1, 1],
        "tagId": [1, 2, 3, 4, 5],
        "relevance": [0.02500, 0.02500, 0.05775, 0.09675, 0.14675]
    }
    df = pd.DataFrame(data)
    return df
