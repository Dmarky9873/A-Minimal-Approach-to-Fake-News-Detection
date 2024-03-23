"""
    Author: Daniel Markusson

    Methods:
    *    getDataFrames --> Dict()
            Summary:
                Returns a dictionary where `getFakeReal()['fake']` has the content of the fake news 
                articles and `getFakeReal()['real']` has the content of the real news articles.
"""

import pandas as pd
from rich_terminal import Rich_Terminal


def getFakeReal(showinfo=True):
    """ Returns a dictionary where `getFakeReal()['fake']` has the content of the fake news articles 
        and `getFakeReal()['real']` has the content of the real news articles.

    Args:
        `showinfo` (bool, optional): If true, getFakeReal() will print information regarding the 
        files it reads. If false, it doesn't. Defaults to True.

    Returns:
        `dict()`: A dictionary who's key `['fake']` is a pandas dataframe of the various fake news 
        articles within the dataset, and who's key `['real']` is a pandas dataframe of the various 
        real news articles within the dataset.
    """

    data = dict()
    buzzfeedDF_fake = pd.read_csv("./raw/BuzzFeed_fake_news_content.csv")
    buzzfeedDF_real = pd.read_csv("./raw/BuzzFeed_real_news_content.csv")
    politifactDF_fake = pd.read_csv("./raw/PolitiFact_fake_news_content.csv")
    politifactDF_real = pd.read_csv("./raw/PolitiFact_real_news_content.csv")

    realDFs = [buzzfeedDF_real, politifactDF_real]
    fakeDFs = [buzzfeedDF_fake, politifactDF_fake]

    data['real'] = pd.concat(realDFs)
    data['fake'] = pd.concat(fakeDFs)

    if showinfo:
        rt = Rich_Terminal()

        print(rt.getString_MINIMAL(
            "Successfully retrieved all fake and real dataframes.") + " \nDataframes:\n")
        print("BuzzFeed_real size:", rt.getString_MAJOR(buzzfeedDF_real.size))
        print("BuzzFeed_fake size:", rt.getString_MAJOR(buzzfeedDF_fake.size))
        print("PolitiFact_real size:", rt.getString_MAJOR(politifactDF_real.size))
        print("PolitiFact_fake size:", rt.getString_MAJOR(politifactDF_fake.size))
        print(rt.PAGE_BREAK)

        print(rt.getString_MINIMAL(
            "Successfully concatinated all fake dataframes together and successfully concatinated all real dataframes together.") + "\nDataframes:\n")
        print("Dataframe_real size: " + rt.getString_MAJOR(data['real'].size))
        print("Dataframe_fake size: " + rt.getString_MAJOR(data['fake'].size))

    return data


if __name__ == '__main__':
    data = getFakeReal(showinfo=True)

    # print(data['real'].head())
    # print(data['fake'].head())
