from .data import DATA, load_gutenberg_data


def get_data():
    authors, metadata = load_gutenberg_data()
    return authors.merge(metadata, on="gutenberg_author_id", how="inner")