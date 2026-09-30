import pandas as pd

DATA = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
    "main/data/2025/2025-06-03"
)


def load_gutenberg_data():
    authors = pd.read_csv(f"{DATA}/gutenberg_authors.csv")
    metadata = pd.read_csv(f"{DATA}/gutenberg_metadata.csv")
    return authors, metadata