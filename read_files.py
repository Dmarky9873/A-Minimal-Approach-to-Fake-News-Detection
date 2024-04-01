"""
    Author: Daniel Markusson

    Methods:
    *    getFakeReal --> Dict()
            Summary:
                Returns a dictionary where `getFakeReal()['fake']` has the content of the fake 
                news articles and `getFakeReal()['real']` has the content of the real news 
                articles.
                
    *   getArticleName --> str()
            Summary:
                Gets the name of the article based on its `ID` and `outlet`.
                    
    *   getOutletStats --> list()
            Summary:
                Helper function that interprets each line from the [outlet]NewsUser.txt file as a 
                list with values: [News Article ID, User ID, Times Shared].
                
"""

import simplejson as json
import pandas as pd
import linecache
import statistics

from rich_terminal import Rich_Terminal

# Articles


def getFakeReal(verbose=False):
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
    buzzfeedDF_fake = pd.read_csv(
        "./raw/BuzzFeed_fake_news_content.csv").fillna("None")
    buzzfeedDF_real = pd.read_csv(
        "./raw/BuzzFeed_real_news_content.csv").fillna("None")
    politifactDF_fake = pd.read_csv(
        "./raw/PolitiFact_fake_news_content.csv").fillna("None")
    politifactDF_real = pd.read_csv(
        "./raw/PolitiFact_real_news_content.csv").fillna("None")

    realDFs = [buzzfeedDF_real, politifactDF_real]
    fakeDFs = [buzzfeedDF_fake, politifactDF_fake]

    for i in range(2):
        for j, k in realDFs[i].iterrows():
            old_id = k.id
            num = int(old_id[old_id.index('_') + 1:old_id.index('-')]) + 1
            outlet = "buzzfeed" if i == 0 else "politifact"
            new_id = getArticleName(num, outlet, False)
            k.id = new_id

        for j, k in fakeDFs[i].iterrows():
            old_id = k.id
            num = int(old_id[old_id.index('_') + 1:old_id.index('-')]) + 1
            outlet = "buzzfeed" if i == 0 else "politifact"
            new_id = getArticleName(num, outlet, True)
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


def getArticleName(ID: int, outlet: str, isFake: bool):
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


def getOutletStats(path: str):
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


def isArticleFake(name: str):
    """Returns `True` if article `name` is fake, and `False` if it is true.

    Args:
        name (`str`): The unique name of an article.

    Returns:
        `bool`: Returns `True` if article `name` is fake, and `False` if it is true.
    """
    if "Fake" in name:
        return True
    return False


# Article-User Relationship


def getArticleCounts(verbose=False):
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
    articles = getFakeReal(verbose)
    stats = dict()
    buzzfeedStats = getOutletStats("./raw/BuzzFeedNewsUser.txt")
    politifactStats = getOutletStats("./raw/PolitiFactNewsUser.txt")

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
                getUsername(int(stat[1]), 'buzzfeed'))
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
                getUsername(int(stat[1]), 'politifact'))
        except KeyError:
            if verbose:
                rt = Rich_Terminal()
                rt.print_WARN(
                    name + " found in News-User relationship but no matching article was found.")
                rt.print_MINIMAL("Continuing...")

    for article in stats.keys():
        stats[article]["users-who-shared"] = list(
            stats[article]["users-who-shared"])

    return stats


def getUserCounts(verbose=False):
    """Gets the counts of the users (number of followers, number of people following, followers, 
    people following, number of shared articles, and articles shared). VERY LARGE.

    Args:
        verbose (`bool`, optional): Set `True` for more information during method call. Defaults to 
        `False`.

    Returns:
        `dict`: A dictionary of dictionaries. The keys of `dict` are the unique usernames of each 
        user within the dataset, which correspond to subdictionaries `followers`, `following`, and 
        `articles`. `followers`, `following` and `articles` each are subdictionaries (keys of 
        `dict`[some unique username]) corresponding to counts and sets of values, as elaborated 
        here:
         - `followers`:
             * `count`: An unsigned integer corresponding to the number of people following user 
             when user is a unique username dictionary key.
             * `users`: Set of all people following user when user is a unique username dictionary 
             key.
         - `following`:
             * `count`: An unsigned integer corresponding to the number of people user is following 
             when user is a unique username dictionary key.
             * `users`: Set of all users user is following when user is a unique username dictionary 
             key.
         - `articles`:
             * `num-shared`: Number of unique articles user shared when user is a unique username 
             dictionary key.
             * `articles-shared`: Set of articles user shared when user is a unique username 
             dictionary key.
             * `num-fake-shared`: An unsigned integer of the number of fake articles shared by user 
             when user is a unique username dictionary key.
             * `num-real-shared`: An unsigned integer of the number of real articles shared by user 
             when user is a unique username dictionary key.
    """

    # Gets the set of all users within the dataset.
    users = getUsers()

    # Creates a dictionary to store the user counts.
    counts = dict()

    # Populating the users dictionary with empty information to be filled in later.
    for user in users:
        counts[user] = {"followers": {"count": 0, "users": set()}, "following": {
            "count": 0, "users": set()}, "articles": {"num-shared": 0, "articles-shared": set(), "num-fake-shared": 0, "num-real-shared": 0}}

    # Gets all of the "a follows b" user-user relationships.
    a_follows_b = getFollowRelationships()

    # Analyzes the `a_follows_b` set and increments/adds people to the required stored variables.
    for follower, receiving_follow in a_follows_b:
        counts[receiving_follow]["followers"]["count"] += 1
        counts[receiving_follow]["followers"]["users"].add(follower)

        counts[follower]["following"]["count"] += 1
        counts[follower]["following"]["users"].add(receiving_follow)

    # Gets the counts of the articles (number of shares and set of users who shared).
    articleCounts = getArticleCounts(verbose)

    # Gets set-like object of all the names of articles.
    articles = articleCounts.keys()

    # Analyzes `articleCounts`, modifying variables within `counts` based on what articles were
    # shared by whom.
    for article in articles:
        usersWhoShared = articleCounts[article]["users-who-shared"]

        for user in usersWhoShared:
            counts[user]["articles"]["num-shared"] += 1
            counts[user]["articles"]["articles-shared"].add(article)
            if isArticleFake(article):
                counts[user]["articles"]["num-fake-shared"] += 1
            else:
                counts[user]["articles"]["num-real-shared"] += 1

    for user in users:
        counts[user]["followers"]["users"] = list(
            counts[user]["followers"]["users"])

        counts[user]["following"]["users"] = list(
            counts[user]["following"]["users"])

        counts[user]["articles"]["articles-shared"] = list(
            counts[user]["articles"]["articles-shared"])

    return counts


def getSharesList(verbose=False):
    """Helper function to retrieve a list of the number of shares for each article.

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to 
        `False`.

    Returns:
        `list`: A list of the number of shares for each article within the dataset.
    """
    counts = getArticleCounts(verbose)
    articles = counts.keys()
    sharesList = []
    for article in articles:
        sharesList.append(counts[article]['shares'])
    return sharesList


def getUserSummaryStatistics(verbose=False):
    """Gets the summary statistics of the user counts.

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to 
        `False`.

    Returns:
        `dict`: Dictionary of summary statistics for counts.
    """
    userCounts = getUserCounts(verbose)
    users = userCounts.keys()
    summaryStatistics = dict()

    followersList = []
    followingList = []
    numArticlesSharedList = []
    numFakeArticlesSharedList = []
    numRealArticlesSharedList = []

    for user in users:
        followersList.append(userCounts[user]["followers"]["count"])
        followingList.append(userCounts[user]["following"]["count"])

        numArticlesSharedList.append(
            userCounts[user]["articles"]["num-shared"])
        numFakeArticlesSharedList.append(
            userCounts[user]["articles"]["num-fake-shared"])
        numRealArticlesSharedList.append(
            userCounts[user]["articles"]["num-real-shared"])

    summaryStatistics["followers"] = {"data": followersList, "mean": statistics.mean(
        followersList), "stdev": statistics.pstdev(followersList), "median": statistics.median(followersList),
        "q1": statistics.quantiles(followersList)[0], "q3": statistics.quantiles(followersList)[2],
        "mode": statistics.mode(followersList)}

    summaryStatistics["following"] = {"data": followingList, "mean": statistics.mean(
        followingList), "stdev": statistics.pstdev(followingList), "median": statistics.median(followingList),
        "q1": statistics.quantiles(followingList)[0], "q3": statistics.quantiles(followingList)[2],
        "mode": statistics.mode(followingList)}

    summaryStatistics["articles-shared"] = {"data": numArticlesSharedList, "mean": statistics.mean(
        numArticlesSharedList), "stdev": statistics.pstdev(numArticlesSharedList), "median": statistics.median(numArticlesSharedList),
        "q1": statistics.quantiles(numArticlesSharedList)[0], "q3": statistics.quantiles(numArticlesSharedList)[2],
        "mode": statistics.mode(numArticlesSharedList)}

    summaryStatistics["fake-articles-shared"] = {"data": numFakeArticlesSharedList, "mean": statistics.mean(
        numFakeArticlesSharedList), "stdev": statistics.pstdev(numFakeArticlesSharedList), "median": statistics.median(numFakeArticlesSharedList),
        "q1": statistics.quantiles(numFakeArticlesSharedList)[0], "q3": statistics.quantiles(numFakeArticlesSharedList)[2],
        "mode": statistics.mode(numFakeArticlesSharedList)}

    summaryStatistics["real-articles-shared"] = {"data": numRealArticlesSharedList, "mean": statistics.mean(
        numRealArticlesSharedList), "stdev": statistics.pstdev(numRealArticlesSharedList), "median": statistics.median(numRealArticlesSharedList),
        "q1": statistics.quantiles(numRealArticlesSharedList)[0], "q3": statistics.quantiles(numRealArticlesSharedList)[2],
        "mode": statistics.mode(numRealArticlesSharedList)}

    return summaryStatistics


def getArticleSummaryStatistics(verbose=False):
    """Gets the summary statistics of the articles (number of shares).

    Args:
        verbose (`bool`, optional): Set `True` for more information during method call. Defaults to 
        False.

    Returns:
        `dict`: A dictionary that has the summary statistics of `data` (number of shares for each 
        article). Keys: `data`, `mean`, `median`, `mode`, `q1`, `q3`, and `stdev`.
    """

    sharesList = getSharesList(verbose)

    summaryStats = dict()

    summaryStats["shares"] = {"data": sharesList, "mean": statistics.mean(sharesList),
                              "median": statistics.median(sharesList),
                              "stdev": statistics.pstdev(sharesList),
                              "q1": statistics.quantiles(sharesList)[0],
                              "q3": statistics.quantiles(sharesList)[2],
                              "mode": statistics.mode(sharesList)}

    return summaryStats


# Users


def getUsername(ID: int, outlet: str):
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


def getUsers():
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


def getFollowRelationships():
    """Gets the follow relationships of each user. VERY LARGE.

    Returns:
        `set`: Set of "a-follows-b" tuples.
    """
    a_follows_b = set()

    with open("./raw/BuzzFeedUserUser.txt") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a, b = int(l_[0]), int(l_[1])
            a, b = int(a), int(b)

            username_A = getUsername(a, 'buzzfeed')
            username_B = getUsername(b, 'buzzfeed')

            a_follows_b.add((username_A, username_B))

    with open("./raw/PolitiFactUserUser.txt") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a = int(l_[0])
            b = int(l_[1])

            a, b = int(a), int(b)

            username_A = getUsername(a, 'politifact')
            username_B = getUsername(b, 'politifact')

            a_follows_b.add((username_A, username_B))

    return a_follows_b


def updateJson(verbose=False):

    data = dict()

    data["articles"] = {"fake-articles": dict(), "real-articles": dict(),
                        "counts": getArticleCounts(verbose), "statistics": getArticleSummaryStatistics(verbose)}

    fakeRealArticles = getFakeReal(verbose)
    data["articles"]["fake-articles"] = fakeRealArticles["fake"].to_dict()
    data["articles"]["real-articles"] = fakeRealArticles["real"].to_dict()

    data["users"] = {"counts": getUserCounts(
        verbose), "statistics": getUserSummaryStatistics(verbose)}

    with open("./cleaned_data.json", 'w') as f:
        json.dump(data, f)


def main():
    updateJson(False)


if __name__ == '__main__':
    main()
