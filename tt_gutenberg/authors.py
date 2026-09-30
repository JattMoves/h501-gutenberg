from .transform import get_data


def list_authors(by_languages=False, alias=False):
    data = get_data()
    name_column = "author_alias" if alias else "author"
    data = data.dropna(subset=[name_column]).copy()
    data[name_column] = data[name_column].str.strip()
    data = data[data[name_column] != ""]

    if by_languages:
        counts = data.groupby(name_column).size()
    else:
        counts = data.groupby(name_column)["gutenberg_id"].nunique()

    return counts.sort_values(ascending=False, kind="stable").index.tolist()