import pandas as pd

def get_title_crew_dataframe():
    data = {
        "tconst": ["tt0000001", "tt0000002", "tt0000003", "tt0000004", "tt0000005"],
        "directors": ["nm0005690", "nm0721526", "nm0721526", "nm0721526", "nm0005690"],
        "writers": [None, None, None, None, None]
    }
    df = pd.DataFrame(data)
    return df
