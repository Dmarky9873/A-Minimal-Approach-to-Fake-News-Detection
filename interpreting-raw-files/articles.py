"""


    Author: Daniel Markusson


"""

import linecache
import pandas as pd
from file_retrieval import get_raw_file_location

BUZZFEED_NAMES_DIR = get_raw_file_location("BuzzFeedNews.txt")
POLITIFACT_NAMES_DIR = get_raw_file_location("PolitiFactNews.txt")


def get_articles_dataframe():
    """ Returns a dictionary where `get_fake_real()['fake']` has the content of the fake news
        articles and `get_fake_real()['real']` has the content of the real news articles.

    Args:
        `showinfo` (bool, optional): If true, get_fake_real() will print information regarding the
        files it reads. If false, it doesn't. Defaults to True.

    Returns:
        `dict()`: A dictionary who's key `['fake']` is a pandas dataframe of the various fake news
        articles within the dataset, and who's key `['real']` is a pandas dataframe of the various
        real news articles within the dataset.
    """

    # Creates a dictionary to store the data.
    data = dict()

    # Reads the CSV files, filters the "NaN" characters, and stores them in temporary variables.
    buzzfeed_dataframe_fake = pd.read_csv(get_raw_file_location(
        "BuzzFeed_fake_news_content.csv")).fillna("None")
    buzzfeed_dataframe_real = pd.read_csv(get_raw_file_location(
        "BuzzFeed_real_news_content.csv")).fillna("None")
    politifact_dataframe_fake = pd.read_csv(get_raw_file_location(
        "PolitiFact_fake_news_content.csv")).fillna("None")
    politifact_dataframe_real = pd.read_csv(get_raw_file_location(
        "PolitiFact_real_news_content.csv")).fillna("None")

    #
    real_dataframes = [buzzfeed_dataframe_real, politifact_dataframe_real]
    fake_dataframes = [buzzfeed_dataframe_fake, politifact_dataframe_fake]

    for i in range(2):
        for _, k in real_dataframes[i].iterrows():
            old_id = k.id
            num = int(old_id[old_id.index('_') + 1:old_id.index('-')]) + 1
            outlet = "buzzfeed" if i == 0 else "politifact"
            new_id = get_article_name(num, outlet, False)
            k.id = new_id

        for _, k in fake_dataframes[i].iterrows():
            old_id = k.id
            num = int(old_id[old_id.index('_') + 1:old_id.index('-')]) + 1
            outlet = "buzzfeed" if i == 0 else "politifact"
            new_id = get_article_name(num, outlet, True)
            k.id = new_id

    data['real'] = pd.concat(real_dataframes)
    data['fake'] = pd.concat(fake_dataframes)

    return data


def get_article_name(id_num: int, outlet: str, is_fake: bool):
    """Gets the name of the article based on its `ID` and `outlet`.

    Args:
        ID (`int`): The ID of the article so that it can be found in the [outlet]News.txt file.
        outlet (`str`): The outlet of the article. ALL LOWERCASE (`buzzfeed` or `politifact`).
        is_fake: Is the article fake?

    Returns:
        `str`: Returns the name of the article.
    """
    # Because IDs correspond to the line number in the [outlet]News.txt files, we can use linecache
    # to quickly find the name within the file.
    if outlet == "buzzfeed":
        if is_fake:
            return linecache.getline(BUZZFEED_NAMES_DIR, id_num - 1 + 91)\
                .replace('\n', '')
        return linecache.getline(BUZZFEED_NAMES_DIR, id_num - 1)\
            .replace('\n', '')
    if is_fake:
        return linecache.getline(POLITIFACT_NAMES_DIR, id_num - 1 + 120)\
            .replace('\n', '')
    return linecache.getline(POLITIFACT_NAMES_DIR, id_num - 1)\
        .replace('\n', '')


def is_article_fake(name: str):
    """Returns `True` if article `name` is fake, and `False` if it is true.

    Args:
        name (`str`): The unique name of an article.

    Returns:
        `bool`: Returns `True` if article `name` is fake, and `False` if it is true.
    """
    if "Fake" in name:
        return True
    return False


ARTICLES_DATAFRAME = get_articles_dataframe()
