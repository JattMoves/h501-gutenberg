from .data import load_gutenberg_data


def get_data():
    """Load the source data and join authors to book metadata.

    Renames author aliases consistently and retains every metadata row.
    """
    df_authors, df_metadata = load_gutenberg_data()

    df_authors = (
        df_authors.drop(columns=["author"], errors="ignore")
        # Distinguish the source alias from the canonical author name.
        .rename(columns={"alias": "author_alias"})
    )

    return df_metadata.merge(
        df_authors,
        on="gutenberg_author_id",
        # Keep metadata rows even when an author record is missing.
        how="left",
    )