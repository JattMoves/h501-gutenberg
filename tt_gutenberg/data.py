import pandas as pd


def load_gutenberg_data():
    base_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03"
    )
    authors = pd.read_csv(f"{base_url}/gutenberg_authors.csv")
    metadata = pd.read_csv(f"{base_url}/gutenberg_metadata.csv")
    languages = pd.read_csv(f"{base_url}/gutenberg_languages.csv")
    return authors, metadata, languages