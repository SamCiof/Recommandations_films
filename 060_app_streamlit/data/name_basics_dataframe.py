import pandas as pd

def get_name_basics_dataframe():
    data = {
        "nconst": ["nm0000001", "nm0000002", "nm0000003", "nm0000004", "nm0000005"],
        "primaryName": ["Fred Astaire", "Lauren Bacall", "Brigitte Bardot", "John Belushi", "Ingmar Bergman"],
        "birthYear": [1899.0, 1924.0, 1934.0, 1949.0, 1918.0],
        "deathYear": [1987.0, 2014.0, None, 1982.0, 2007.0],
        "primaryProfession": ["actor,miscellaneous,producer", "actress,soundtrack,archive_footage", "actress,music_department,producer", "actor,writer,music_department", "writer,director,actor"],
        "knownForTitles": ["tt0072308,tt0050419,tt0053137,tt0027125", "tt0037382,tt0075213,tt0117057,tt0038355", "tt0057345,tt0049189,tt0056404,tt0054452", "tt0072562,tt0077975,tt0080455,tt0078723", "tt0050986,tt0083922,tt0050976,tt0069467"]
    }
    df = pd.DataFrame(data)
    return df
