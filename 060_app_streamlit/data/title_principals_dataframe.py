import pandas as pd

def get_title_principals_dataframe():
    data = {
        "tconst": ["tt0000001", "tt0000001", "tt0000001", "tt0000001", "tt0000002"],
        "ordering": [1, 2, 3, 4, 1],
        "nconst": ["nm1588970", "nm0005690", "nm0005690", "nm0374658", "nm0721526"],
        "category": ["self", "director", "producer", "cinematographer", "director"],
        "job": [None, None, "producer", "director of photography", None],
        "characters": [["Self"], None, None, None, None]
    }
    df = pd.DataFrame(data)
    return df
