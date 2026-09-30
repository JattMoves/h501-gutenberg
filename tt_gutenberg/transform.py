from .data import load_gutenberg_data

def get_data():
    authors, metadata, languages = load_gutenberg_data()

    authors_and_metadata = authors.merge(
        metadata,
        on="gutenberg_author_id",
        how="inner",
    )

    return authors_and_metadata.merge(
        languages,
        on="gutenberg_id",
        how="inner",
    )
    
    