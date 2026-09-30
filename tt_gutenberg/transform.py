from .data import DATA, load_gutenberg_data


def get_data():
    if isinstance(DATA, dict):
        df_authors = DATA["df_authors"]
        df_metadata = DATA["df_metadata"]
    else:
        df_authors, df_metadata = load_gutenberg_data()

    df_authors = (
        df_authors.drop(columns=["author"], errors="ignore")
        .rename(columns={"alias": "author_alias"})
    )

    return df_metadata.merge(
        df_authors,
        on="gutenberg_author_id",
        how="left",
    )