from .data import load_gutenberg_data


def list_authors(by_languages=False, alias=False):
    authors, metadata, languages = load_gutenberg_data()
    name_column = "alias" if alias else "author"

    book_languages = metadata[
        ["gutenberg_id", "gutenberg_author_id"]
    ].merge(
        languages[["gutenberg_id", "language"]],
        on="gutenberg_id",
    )
    combined = book_languages.merge(
        authors[["gutenberg_author_id", name_column]],
        on="gutenberg_author_id",
    )
    combined = combined.dropna(subset=[name_column])
    combined[name_column] = combined[name_column].str.strip()
    combined = combined[combined[name_column] != ""]

    if by_languages:
        counts = combined.groupby(name_column)["language"].nunique()
    else:
        counts = combined.groupby(name_column)["gutenberg_id"].nunique()

    return counts.sort_values(ascending=False).index.tolist()