"""


    Author: Daniel Markusson


"""

import linecache
from articles import get_articles_dataframe, is_article_fake
from article_user_relationship import user_article_shares
from users import get_username, get_users, get_follow_relationships
from file_retrieval import get_file_location
from rt.rich_terminal import RichTerminal


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
    articles = get_articles_dataframe(verbose)
    stats = dict()
    buzzfeed_stats = user_article_shares(
        get_file_location("BuzzFeedNewsUser.txt"))
    politifact_stats = user_article_shares(
        get_file_location("PolitiFactNewsUser.txt"))

    error_articles = set()

    # Populating the dictionaries
    for name in articles['fake'].id:
        stats[name] = {"shares": 0, "users-who-shared": set()}

    for name in articles['real'].id:
        stats[name] = {"shares": 0, "users-who-shared": set()}

    for stat in buzzfeed_stats:
        name = linecache.getline(get_file_location(
            "BuzzFeedNews.txt"), int(stat[0])).replace('\n', '')
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
            get_file_location("PolitiFactNews.txt"), int(stat[0])).replace('\n', '')
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


get_article_counts()
