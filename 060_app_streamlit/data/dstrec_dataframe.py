import pandas as pd

def get_dstrec_dataframe():
    data = {
        "imdbId": [
            "tt0000009", 
            "tt0000147", 
            "tt0000502", 
            "tt0000574", 
            "tt0000675"
        ],
        "numVotes": [212.0, 515.0, 17.0, 900.0, 20.0],
        "actor": [
            "William Courtenay", 
            None, 
            "Antonio del Pozo", 
            "Godfrey Cass", 
            None
        ],
        "actress": [
            "Blanche Bayliss", 
            None, 
            None, 
            "Bella Cola", 
            None
        ],
        "director": [
            "Alexander Black", 
            "Enoch J. Rector", 
            "Ricardo de Baños", 
            "Charles Tait", 
            "Narciso Cuyàs"
        ],
        "producer": [
            "Alexander Black", 
            "William A. Brady", 
            None, 
            "W.A. Gibson", 
            None
        ],
        "title": [
            "Miss Jerry", 
            "The Corbett-Fitzsimmons Fight", 
            "Bohemios", 
            "The Story of the Kelly Gang", 
            "Don Quijote"
        ],
        "genres": [
            "Romance", 
            "Documentary,News,Sport", 
            None, 
            "Action,Adventure,Biography", 
            "Drama"
        ],
        "averageRating": [5.4, 5.2, 4.4, 6.0, 4.2]
    }
    
    df = pd.DataFrame(data)
    return df
