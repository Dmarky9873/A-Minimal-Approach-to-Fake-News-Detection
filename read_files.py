"""
    Author: Daniel Markusson

    Methods:
    *    __getFakeReal --> Dict()
            Summary:
                Returns a dictionary where `__getFakeReal()['fake']` has the content of the fake 
                news articles and `__getFakeReal()['real']` has the content of the real news 
                articles.
                
    *   __getArticleName --> str()
            Summary:
                Gets the name of the article based on its `ID` and `outlet`.
                    
    *   __getOutletStats --> list()
            Summary:
                Helper function that interprets each line from the [outlet]NewsUser.txt file as a 
                list with values: [News Article ID, User ID, Times Shared].
                
"""

import json
import pandas as pd
# from prettytable import PrettyTable
import linecache
import statistics

from rich_terminal import Rich_Terminal

# Articles


def __getFakeReal(verbose=False):
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

    for i in range(2):
        for j, k in realDFs[i].iterrows():
            old_id = k.id
            num = int(old_id[old_id.index('_') + 1:old_id.index('-')]) + 1
            outlet = "buzzfeed" if i == 0 else "politifact"
            new_id = __getArticleName(num, outlet, False)
            k.id = new_id

        for j, k in fakeDFs[i].iterrows():
            old_id = k.id
            num = int(old_id[old_id.index('_') + 1:old_id.index('-')]) + 1
            outlet = "buzzfeed" if i == 0 else "politifact"
            new_id = __getArticleName(num, outlet, True)
            k.id = new_id

    data['real'] = pd.concat(realDFs)
    data['fake'] = pd.concat(fakeDFs)

    if verbose:
        rt = Rich_Terminal()

        print(rt.getString_MINIMAL(
            "Successfully retrieved all fake and real dataframes.") + " \nDataframes:\n")
        print("BuzzFeed_real size:", rt.getString_MAJOR(buzzfeedDF_real.size))
        print("BuzzFeed_fake size:", rt.getString_MAJOR(buzzfeedDF_fake.size))
        print("PolitiFact_real size:", rt.getString_MAJOR(politifactDF_real.size))
        print("PolitiFact_fake size:", rt.getString_MAJOR(politifactDF_fake.size))
        print(rt.PAGE_BREAK)

        print(rt.getString_MINIMAL(
            """Successfully concatinated all dataframes.""") + "\nDataframes:\n")
        print("Dataframe_real size: " + rt.getString_MAJOR(data['real'].size))
        print("Dataframe_fake size: " + rt.getString_MAJOR(data['fake'].size))
        print("\n\n")

    return data


def __getArticleName(ID: int, outlet: str, isFake: bool):
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
        if isFake:
            return linecache.getline("./raw/BuzzFeedNews.txt", ID - 1 + 91).replace('\n', '')
        return linecache.getline("./raw/BuzzFeedNews.txt", ID - 1).replace('\n', '')
    if isFake:
        return linecache.getline("./raw/PolitiFactNews.txt", ID - 1 + 120).replace('\n', '')
    return linecache.getline("./raw/PolitiFactNews.txt", ID - 1).replace('\n', '')


def __getOutletStats(path: str):
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
    with open(path) as f:
        for l in f:
            stats.append(l.split('\t'))

    return stats


# Article-User Relationship


def __getArticleCounts(verbose=False):
    """Gets the counts of the articles (num shares and users who shared).

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to 
        False.

    Returns:
        `dict`: A dictionary with keys set as the unique article IDs. The keys correspond to another 
        sub-dictionary whos keys are `shares` and `users-who-shared`. `shares` is an unsigned 
        integer which is the number of times article `name` was shared. `users-who-shared` is a set 
        with the usernames of the users who shared article `name`.
    """
    articles = __getFakeReal(verbose)
    stats = dict()
    buzzfeedStats = __getOutletStats("./raw/BuzzFeedNewsUser.txt")
    politifactStats = __getOutletStats("./raw/PolitiFactNewsUser.txt")

    errorArticles = set()

    # Populating the dictionaries
    for name in articles['fake'].id:
        stats[name] = {"shares": 0, "users-who-shared": set()}

    for name in articles['real'].id:
        stats[name] = {"shares": 0, "users-who-shared": set()}

    for stat in buzzfeedStats:
        name = linecache.getline(
            "./raw/BuzzFeedNews.txt", int(stat[0])).replace('\n', '')
        try:
            stats[name]["shares"] += int(stat[2].replace('\n', ''))
            stats[name]["users-who-shared"].add(
                __getUsername(int(stat[1]), 'buzzfeed'))
        except KeyError:
            if verbose and name not in errorArticles:
                rt = Rich_Terminal()
                rt.print_WARN(
                    name + " found in News-User relationship but no matching article was found.")
                rt.print_MINIMAL("Continuing...")
            errorArticles.add(name)

    for stat in politifactStats:
        name = linecache.getline(
            "./raw/PolitiFactNews.txt", int(stat[0])).replace('\n', '')
        try:
            stats[name]["shares"] += int(stat[2])
            stats[name]["users-who-shared"].add(
                __getUsername(int(stat[1]), 'politifact'))
        except KeyError:
            if verbose:
                rt = Rich_Terminal()
                rt.print_WARN(
                    name + " found in News-User relationship but no matching article was found.")
                rt.print_MINIMAL("Continuing...")

    return stats


# TODO: Finish the articles part of the users dictionary
def __getUserCounts(verbose=False):
    users = __getUsers()

    counts = dict()

    # Populating the users dictionary with empty information to be filled in later.
    for user in users:
        counts[user] = {"followers": {"count": 0, "users": set()}, "following": {
            "count": 0, "users": set()}, "articles": {"num-shared": 0, "articles-shared": set()}}

    a_follows_b = __getFollowRelationships()

    for follower, receiving_follow in a_follows_b:
        counts[receiving_follow]["followers"]["count"] += 1
        counts[receiving_follow]["followers"]["users"].add(follower)

        counts[follower]["following"]["count"] += 1
        counts[follower]["following"]["users"].add(receiving_follow)

    return counts


def __getSharesList(verbose=False):
    """Helper function to retrieve a list of the number of shares for each article.

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to 
        `False`.

    Returns:
        `list`: A list of the number of shares for each article within the dataset.
    """
    counts = __getArticleCounts(verbose)
    articles = counts.keys()
    sharesList = []
    for article in articles:
        sharesList.append(counts[article]['shares'])
    return sharesList


def __getArticleSummaryStatistics(verbose=False):
    """Gets the summary statistics of the articles (number of shares).

    Args:
        verbose (`bool`, optional): Set `True` for more information during method call. Defaults to 
        False.

    Returns:
        `dict`: A dictionary that has the summary statistics of `data` (number of shares for each 
        article). Keys: `data`, `mean`, `median`, `mode`, `q1`, `q3`, and `stdev`.
    """

    sharesList = __getSharesList(verbose)

    summaryStats = dict()

    summaryStats["shares"] = {"data": sharesList, "mean": statistics.mean(sharesList),
                              "median": statistics.median(sharesList),
                              "stdev": statistics.pstdev(sharesList),
                              "q1": statistics.quantiles(sharesList)[0],
                              "q3": statistics.quantiles(sharesList)[2],
                              "mode": statistics.mode(sharesList)}

    print(summaryStats)

    return summaryStats


def __getUserSummaryStatistics(verbose=False):
    pass

# Users


def __getUsername(ID: int, outlet: str):
    """Gets the unique username of user `ID` based on their outlet, `outlet`.

    Args:
        ID (`int`): The ID of the user, retrieved from the news-user relationship file.
        outlet (`str`): The outlet of user `ID`.

    Returns:
        `str`: The unique username of user `ID`.
    """
    if outlet == 'buzzfeed':
        return linecache.getline("./raw/BuzzFeedUser.txt", ID).replace('\n', '')
    return linecache.getline("./raw/PolitiFactUser.txt", ID).replace('\n', '')


def __getUsers():
    """Gets set of all users in dataset.

    Returns:
        `set`: Set of all users in a dataset.
    """

    users = set()
    with open("./raw/PolitiFactUser.txt") as f:
        for l in f:
            users.add(l.replace('\n', ''))

    with open("./raw/BuzzFeedUser.txt") as f:
        for l in f:
            users.add(l.replace('\n', ''))

    return users


def __getFollowRelationships():
    """Gets the follow relationships of each user. VERY LARGE.

    Returns:
        `set`: Set of "a-follows-b" tuples.
    """
    a_follows_b = set()

    with open("./raw/BuzzFeedUserUser.txt") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a = int(l_[0])
            b = int(l_[1])

            a, b = int(a), int(b)

            username_A = __getUsername(a, 'buzzfeed')
            username_B = __getUsername(b, 'buzzfeed')

            a_follows_b.add((username_A, username_B))

    with open("./raw/PolitiFactUserUser.txt") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a = int(l_[0])
            b = int(l_[1])

            a, b = int(a), int(b)

            username_A = __getUsername(a, 'politifact')
            username_B = __getUsername(b, 'politifact')

            a_follows_b.add((username_A, username_B))

    return a_follows_b


def main():
    __getUserCounts()


if __name__ == '__main__':
    main()
