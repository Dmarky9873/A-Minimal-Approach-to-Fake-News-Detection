"""
    Author: Daniel Markusson

    Summary:
                
"""

import simplejson as json
from counts import get_article_counts, get_user_counts
from summary_statistics import get_articles_summary_statistics, get_user_summary_statistics
from articles import get_articles_dataframe


def update_json(verbose=False):
    """Updates the JSON "database" with the information from the raw files.

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to 
        False.
    """

    data = dict()

    data["articles"] = {
        "fake-articles": dict(), "real-articles": dict(),
        "counts": get_article_counts(verbose),
        "statistics": get_articles_summary_statistics(verbose)
    }

    fake_and_real_articles = get_articles_dataframe(verbose)
    data["articles"]["fake-articles"] = fake_and_real_articles["fake"].to_dict()
    data["articles"]["real-articles"] = fake_and_real_articles["real"].to_dict()

    data["users"] = {"counts": get_user_counts(
        verbose), "statistics": get_user_summary_statistics(verbose)}

    with open("./z.json", 'w', encoding="UTF-8") as f:
        json.dump(data, f)


def main():
    """Main method to be run if this file is ran.
    """
    update_json(False)


if __name__ == '__main__':
    main()
