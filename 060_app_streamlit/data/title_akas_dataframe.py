import pandas as pd

def get_title_akas_dataframe():
    data = {
        "titleId": ["tt0000001", "tt0000001", "tt0000001", "tt0000001", "tt0000001"],
        "ordering": [1, 2, 3, 4, 5],
        "title": ["Carmencita", "Carmencita", "Carmencita", "Carmencita - spanyol tánc", "Καρμενσίτα"],
        "region": [None, "DE", "US", "HU", "GR"],
        "language": [None, None, None, None, None],
        "types": ["original", None, "imdbDisplay", "imdbDisplay", "imdbDisplay"],
        "attributes": [None, "literal title", None, None, None],
        "isOriginalTitle": [1, 0, 0, 0, 0]
    }
    df = pd.DataFrame(data)
    return df
