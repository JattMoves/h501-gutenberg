import pandas as pd

DATA = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
    "main/data/2025/2025-06-03"
)


def get_data():
    authors = pd.read_csv(f"{DATA}/gutenberg_authors.csv")
    metadata = pd.read_csv(f"{DATA}/gutenberg_metadata.csv")

    authors = authors.drop(columns=["author"]).rename(
        columns={"alias": "author_alias"}
    )
    return authors.merge(metadata, on="gutenberg_author_id", how="inner")