"""


    Author: Daniel Markusson


"""

import os
import linecache
import pandas as pd
from rt.rich_terminal import RichTerminal


def get_raw_files_directory():
    """ Retrieves the directory of the raw files to be interpreted by the `get_articles_dataframe`
        function.

    Returns:
        `str`: The path that leads to the directory of the raw files.
    """
    rt = RichTerminal()

    # The set to house all of the directories in the current working directory
    directories = set()

    # Goes through all of the directories in the current working directory and checks if "raw-files"
    # is there.
    for _, dirs, _ in os.walk(os.getcwd(), topdown=True):
        for name in dirs:
            directories.add(name)

    # If raw files isn't at the current working directory, we move up one directory and check there.
    c = 0
    while "raw-files" not in directories:
        os.chdir('..')
        for _, dirs, _ in os.walk(".", topdown=True):
            for name in dirs:
                directories.add(name)
        c += 1

        if c == 4:
            rt.print_alert(
                "Searched up 5 directories and did not find the 'raw-files' directory. \nAre you \
                sure it is there? Please check the name of the directory."
            )

    # Once we have
    raw_files_path = os.path.join(os.getcwd(), "raw-files")

    return raw_files_path


def get_articles_dataframe(verbose=False):
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

    raw_files_path = get_raw_files_directory()

    # Reads the CSV files, filters the "NaN" characters, and stores them in temporary variables.
    buzzfeed_dataframe_fake = pd.read_csv(
        os.path.join(raw_files_path, "BuzzFeed_fake_news_content.csv")).fillna("None")
    buzzfeed_dataframe_real = pd.read_csv(
        os.path.join(raw_files_path, "BuzzFeed_real_news_content.csv")).fillna("None")
    politifact_dataframe_fake = pd.read_csv(
        "../raw-files/PolitiFact_fake_news_content.csv").fillna("None")
    politifact_dataframe_real = pd.read_csv(
        "../raw-files/PolitiFact_real_news_content.csv").fillna("None")

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

    if verbose:
        rt = RichTerminal()

        print(rt.get_string_minimal(
            "Successfully retrieved all fake and real dataframes.") + " \nDataframes:\n")
        print("BuzzFeed_real size:", rt.get_string_major(
            buzzfeed_dataframe_real.size))
        print("BuzzFeed_fake size:", rt.get_string_major(
            buzzfeed_dataframe_fake.size))
        print("PolitiFact_real size:", rt.get_string_major(
            politifact_dataframe_real.size))
        print("PolitiFact_fake size:", rt.get_string_major(
            politifact_dataframe_fake.size))
        print(rt.page_break)

        print(rt.get_string_minimal(
            """Successfully concatinated all dataframes.""") + "\nDataframes:\n")
        print("Dataframe_real size: " + rt.get_string_major(data['real'].size))
        print("Dataframe_fake size: " + rt.get_string_major(data['fake'].size))
        print("\n\n")

    return data


def get_article_name(id_num: int, outlet: str, is_fake: bool):
    """Gets the name of the article based on its `ID` and `outlet`.

    Args:
        ID (`int`): The ID of the article so that it can be found in the [outlet]News.txt file.
        outlet (`str`): The outlet of the article. ALL LOWERCASE (`buzzfeed` or `politifact`).

    Returns:
        `str`: Returns the name of the article.
    """
    # Because IDs correspond to the line number in the [outlet]News.txt files, we can use linecache
    # to quickly find the name within the file.
    if outlet == "buzzfeed":
        if is_fake:
            return linecache.getline("./raw/BuzzFeedNews.txt", id_num - 1 + 91).replace('\n', '')
        return linecache.getline("./raw/BuzzFeedNews.txt", id_num - 1).replace('\n', '')
    if is_fake:
        return linecache.getline("./raw/PolitiFactNews.txt", id_num - 1 + 120).replace('\n', '')
    return linecache.getline("./raw/PolitiFactNews.txt", id_num - 1).replace('\n', '')


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
