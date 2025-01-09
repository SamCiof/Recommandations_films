import pandas as pd

def get_genome_tags_dataframe():
    data = {
        "tagId": [1, 2, 3, 4, 5],
        "tag": ["007", "007 (series)", "18th century", "1920s", "1930s"]
    }
    df = pd.DataFrame(data)
    return df
