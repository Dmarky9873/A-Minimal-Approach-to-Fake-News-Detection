"""

    Author: Daniel Markusson


"""
import statistics
from counts import get_user_counts
from article_user_relationship import get_shares_list


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
