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

import statistics
import linecache
import simplejson as json
import pandas as pd

from rich_terminal import RichTerminal

# Articles


def get_fake_real(verbose=False):
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
    buzzfeed_dataframe_fake = pd.read_csv(
        "./raw/BuzzFeed_fake_news_content.csv").fillna("None")
    buzzfeed_dataframe_real = pd.read_csv(
        "./raw/BuzzFeed_real_news_content.csv").fillna("None")
    politifact_dataframe_fake = pd.read_csv(
        "./raw/PolitiFact_fake_news_content.csv").fillna("None")
    politifact_dataframe_real = pd.read_csv(
        "./raw/PolitiFact_real_news_content.csv").fillna("None")

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


def get_outlet_stats(path: str):
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


# Article-User Relationship


def get_article_counts(verbose=False):
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
    articles = get_fake_real(verbose)
    stats = dict()
    buzzfeed_stats = get_outlet_stats("./raw/BuzzFeedNewsUser.txt")
    politifact_stats = get_outlet_stats("./raw/PolitiFactNewsUser.txt")

    error_articles = set()

    # Populating the dictionaries
    for name in articles['fake'].id:
        stats[name] = {"shares": 0, "users-who-shared": set()}

    for name in articles['real'].id:
        stats[name] = {"shares": 0, "users-who-shared": set()}

    for stat in buzzfeed_stats:
        name = linecache.getline(
            "./raw/BuzzFeedNews.txt", int(stat[0])).replace('\n', '')
        try:
            stats[name]["shares"] += int(stat[2].replace('\n', ''))
            stats[name]["users-who-shared"].add(
                get_username(int(stat[1]), 'buzzfeed'))
        except KeyError:
            if verbose and name not in error_articles:
                rt = RichTerminal()
                rt.print_warn(
                    name + " found in News-User relationship but no matching article was found.")
                rt.print_minimal("Continuing...")
            error_articles.add(name)

    for stat in politifact_stats:
        name = linecache.getline(
            "./raw/PolitiFactNews.txt", int(stat[0])).replace('\n', '')
        try:
            stats[name]["shares"] += int(stat[2])
            stats[name]["users-who-shared"].add(
                get_username(int(stat[1]), 'politifact'))
        except KeyError:
            if verbose:
                rt = RichTerminal()
                rt.print_warn(
                    name + " found in News-User relationship but no matching article was found.")
                rt.print_minimal("Continuing...")

    for _, values in stats.items():
        values["users-who-shared"] = list(values["users-who-shared"])

    return stats


def get_user_counts(verbose=False):
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
    users = get_users()

    # Creates a dictionary to store the user counts.
    counts = dict()

    # Populating the users dictionary with empty information to be filled in later.
    for user in users:
        counts[user] = {"followers": {"count": 0, "users": set()},
                        "following": {"count": 0, "users": set()},
                        "articles": {
                            "num-shared": 0,
                            "articles-shared": set(),
                            "num-fake-shared": 0,
                            "num-real-shared": 0
        }}

    # Gets all of the "a follows b" user-user relationships.
    a_follows_b = get_follow_relationships()

    # Analyzes the `a_follows_b` set and increments/adds people to the required stored variables.
    for follower, receiving_follow in a_follows_b:
        counts[receiving_follow]["followers"]["count"] += 1
        counts[receiving_follow]["followers"]["users"].add(follower)

        counts[follower]["following"]["count"] += 1
        counts[follower]["following"]["users"].add(receiving_follow)

    # Gets the counts of the articles (number of shares and set of users who shared).
    article_counts = get_article_counts(verbose)

    # Gets set-like object of all the names of articles.
    articles = article_counts.keys()

    # Analyzes `articleCounts`, modifying variables within `counts` based on what articles were
    # shared by whom.
    for article in articles:
        users_who_shared = article_counts[article]["users-who-shared"]

        for user in users_who_shared:
            counts[user]["articles"]["num-shared"] += 1
            counts[user]["articles"]["articles-shared"].add(article)
            if is_article_fake(article):
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


def get_user_summary_statistics(verbose=False):
    """Gets the summary statistics of the user counts.

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to 
        `False`.

    Returns:
        `dict`: Dictionary of summary statistics for counts.
    """
    user_counts = get_user_counts(verbose)
    users = user_counts.keys()
    summary_statistics = dict()

    followers_list = []
    following_list = []
    num_articles_shared_list = []
    num_fake_articles_shared_list = []
    num_real_articles_shared_list = []

    for user in users:
        followers_list.append(user_counts[user]["followers"]["count"])
        following_list.append(user_counts[user]["following"]["count"])

        num_articles_shared_list.append(
            user_counts[user]["articles"]["num-shared"])
        num_fake_articles_shared_list.append(
            user_counts[user]["articles"]["num-fake-shared"])
        num_real_articles_shared_list.append(
            user_counts[user]["articles"]["num-real-shared"])

    summary_statistics["followers"] = {
        "data": followers_list, "mean": statistics.mean(
            followers_list), "stdev": statistics.pstdev(followers_list),
        "median": statistics.median(followers_list),
        "q1": statistics.quantiles(followers_list)[0],
        "q3": statistics.quantiles(followers_list)[2],
        "mode": statistics.mode(followers_list)
    }

    summary_statistics["following"] = {
        "data": following_list, "mean": statistics.mean(
            following_list), "stdev": statistics.pstdev(following_list),
        "median": statistics.median(following_list),
        "q1": statistics.quantiles(following_list)[0],
        "q3": statistics.quantiles(following_list)[2],
        "mode": statistics.mode(following_list)
    }

    summary_statistics["articles-shared"] = {
        "data": num_articles_shared_list,
        "mean": statistics.mean(
            num_articles_shared_list), "stdev": statistics.pstdev(num_articles_shared_list),
        "median": statistics.median(num_articles_shared_list),
        "q1": statistics.quantiles(num_articles_shared_list)[0],
        "q3": statistics.quantiles(num_articles_shared_list)[2],
        "mode": statistics.mode(num_articles_shared_list)
    }

    summary_statistics["fake-articles-shared"] = {
        "data": num_fake_articles_shared_list,
        "mean": statistics.mean(
            num_fake_articles_shared_list),
        "stdev": statistics.pstdev(num_fake_articles_shared_list),
        "median": statistics.median(num_fake_articles_shared_list),
        "q1": statistics.quantiles(num_fake_articles_shared_list)[0],
        "q3": statistics.quantiles(num_fake_articles_shared_list)[2],
        "mode": statistics.mode(num_fake_articles_shared_list)
    }

    summary_statistics["real-articles-shared"] = {
        "data": num_real_articles_shared_list,
        "mean": statistics.mean(
            num_real_articles_shared_list),
        "stdev": statistics.pstdev(num_real_articles_shared_list),
        "median": statistics.median(num_real_articles_shared_list),
        "q1": statistics.quantiles(num_real_articles_shared_list)[0],
        "q3": statistics.quantiles(num_real_articles_shared_list)[2],
        "mode": statistics.mode(num_real_articles_shared_list)}

    return summary_statistics


def get_articles_summary_statistics(verbose=False):
    """Gets the summary statistics of the articles (number of shares).

    Args:
        verbose (`bool`, optional): Set `True` for more information during method call. Defaults to 
        False.

    Returns:
        `dict`: A dictionary that has the summary statistics of `data` (number of shares for each 
        article). Keys: `data`, `mean`, `median`, `mode`, `q1`, `q3`, and `stdev`.
    """

    shares_list = get_shares_list(verbose)

    summary_statistics = dict()

    summary_statistics["shares"] = {
        "data": shares_list, "mean": statistics.mean(shares_list),
        "median": statistics.median(shares_list),
        "stdev": statistics.pstdev(shares_list),
        "q1": statistics.quantiles(shares_list)[0],
        "q3": statistics.quantiles(shares_list)[2],
        "mode": statistics.mode(shares_list)
    }

    return summary_statistics


# Users


def get_username(id_num: int, outlet: str):
    """Gets the unique username of user `ID` based on their outlet, `outlet`.

    Args:
        ID (`int`): The ID of the user, retrieved from the news-user relationship file.
        outlet (`str`): The outlet of user `ID`.

    Returns:
        `str`: The unique username of user `ID`.
    """
    if outlet == 'buzzfeed':
        return linecache.getline("./raw/BuzzFeedUser.txt", id_num).replace('\n', '')
    return linecache.getline("./raw/PolitiFactUser.txt", id_num).replace('\n', '')


def get_users():
    """Gets set of all users in dataset.

    Returns:
        `set`: Set of all users in a dataset.
    """

    users = set()
    with open("./raw/PolitiFactUser.txt", encoding="UTF-8") as f:
        for l in f:
            users.add(l.replace('\n', ''))

    with open("./raw/BuzzFeedUser.txt", encoding="UTF-8") as f:
        for l in f:
            users.add(l.replace('\n', ''))

    return users


def get_follow_relationships():
    """Gets the follow relationships of each user. VERY LARGE.

    Returns:
        `set`: Set of "a-follows-b" tuples.
    """
    a_follows_b = set()

    with open("./raw/BuzzFeedUserUser.txt", encoding="UTF-8") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a, b = int(l_[0]), int(l_[1])
            a, b = int(a), int(b)

            username_a = get_username(a, 'buzzfeed')
            username_b = get_username(b, 'buzzfeed')

            a_follows_b.add((username_a, username_b))

    with open("./raw/PolitiFactUserUser.txt", encoding="UTF-8") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a = int(l_[0])
            b = int(l_[1])

            a, b = int(a), int(b)

            username_a = get_username(a, 'politifact')
            username_b = get_username(b, 'politifact')

            a_follows_b.add((username_a, username_b))

    return a_follows_b


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

    fake_and_real_articles = get_fake_real(verbose)
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
