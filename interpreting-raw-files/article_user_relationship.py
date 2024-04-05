"""


    Author: Daniel Markusson


"""
from counts import get_article_counts


def user_article_shares(path: str):
    """Helper function that interprets each line from the [outlet]NewsUser.txt file as a list with 
    values: [News Article ID, User ID, Times Shared].

    Args:
        path (`str`): The path to the [outlet]NewsUser.txt file.

    Returns:
        `list`: A two-dimensional array of each line in `path`. The subarrays have values [News 
        Article ID, User ID, Times Shared].
    """
    # Array to hold the subarrays
    stats = []
    # Reads the file and appends a subarray to the `stats` array. The subarray has values stated
    # in the method outline.
    with open(path, encoding="UTF-8") as f:
        for l in f:
            stats.append(l.split('\t'))

    return stats


def get_shares_list(verbose=False):
    """Helper function to retrieve a list of the number of shares for each article.

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to 
        `False`.

    Returns:
        `list`: A list of the number of shares for each article within the dataset.
    """
    counts = get_article_counts(verbose)
    articles = counts.keys()
    shares_list = []
    for article in articles:
        shares_list.append(counts[article]['shares'])
    return shares_list
