"""
    Author: Daniel Markusson

    Methods:
    *    get_fake_real --> Dict()
            Summary:
                Returns a dictionary where `get_fake_real()['fake']` has the content of the fake 
                news articles and `get_fake_real()['real']` has the content of the real news 
                articles.
                
    *   get_article_name --> str()
            Summary:
                Gets the name of the article based on its `ID` and `outlet`.
                    
    *   get_outlet_stats --> list()
            Summary:
                Helper function that interprets each line from the [outlet]NewsUser.txt file as a 
                list with values: [News Article ID, User ID, Times Shared].
                
"""

import simplejson as json
from counts import get_article_counts, get_user_counts
from summary_statistics import get_articles_summary_statistics, get_user_summary_statistics
from articles import get_articles_dataframe

# from rich_terminal import RichTerminal


# Article-User Relationship


# Users


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

    with open("./cleaned_data.json", 'w', encoding="UTF-8") as f:
        json.dump(data, f)


def main():
    """Main method to be run if this file is ran.
    """
    update_json(False)


if __name__ == '__main__':
    main()
