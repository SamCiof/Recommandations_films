import pandas as pd

def get_tags_dataframe():
    data = {
        "userId": [18, 65, 65, 65, 65],
        "movieId": [4141, 208, 353, 521, 592],
        "tag": ["Mark Waters", "dark hero", "dark hero", "noir thriller", "dark hero"],
        "timestamp": [1240597180, 1368150078, 1368150079, 1368149983, 1368150078]
    }
    df = pd.DataFrame(data)
    return df
