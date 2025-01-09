import pandas as pd

def get_rating_dataframe():
    data = {
        "userId": [1, 1, 1, 1, 1],
        "movieId": [2, 29, 32, 47, 50],
        "rating": [3.5, 3.5, 3.5, 3.5, 3.5],
        "timestamp": [1112486027, 1112484676, 1112484819, 1112484727, 1112484580]
    }
    df = pd.DataFrame(data)
    return df
