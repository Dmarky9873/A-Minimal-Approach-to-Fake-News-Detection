"""

    Author: Daniel Markusson
    

"""
import os
from visualization.tables.create_table import create_table
from visualization.tables.user_follow_stats.generate_stats.get_user_follow_stats import FollowStats
from visualization.get_json_dict import DATABASE
from definitions import DECIMALS_TO_ROUND


def create_followers_per_user_table():
    """ Generates a table with basic statistics about the number of shares per article.
    """
    followers_per_user_stats = FollowStats(DATABASE)
    means = followers_per_user_stats.mean()
    medians = followers_per_user_stats.median()
    modes = followers_per_user_stats.mode()
    stdevs = followers_per_user_stats.stdev()
    ranges = followers_per_user_stats.range()
    iqrs = followers_per_user_stats.iqr()
    skews = followers_per_user_stats.skew()
    kurtosis = followers_per_user_stats.kurtosis()

    independent_vars = ["", "All", "Fake", "Real", "Large", "L. Fake",
                        "L. Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Stdev", "Range", "IQR",
                      "Skew", "Kurtosis"]

    values = [
        # Means
        # Followers all
        [round(means["mean-followers-per-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followers-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followers-per-real-user"], DECIMALS_TO_ROUND)],
        # Followers large
        [round(means["mean-followers-per-large-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followers-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followers-per-large-real-user"], DECIMALS_TO_ROUND)],

        # Medians
        # Followers all
        [int(medians["median-followers-per-user"])],
        [int(medians["median-followers-per-fake-user"])],
        [int(medians["median-followers-per-real-user"])],
        # Followers large
        [int(medians["median-followers-per-large-user"])],
        [int(medians["median-followers-per-large-fake-user"])],
        [int(medians["median-followers-per-large-real-user"])],

        # Modes
        # Followers all
        [int(modes["mode-followers-per-user"])],
        [int(modes["mode-followers-per-fake-user"])],
        [int(modes["mode-followers-per-real-user"])],
        # Followers large
        [int(modes["mode-followers-per-large-user"])],
        [int(modes["mode-followers-per-large-fake-user"])],
        [int(modes["mode-followers-per-large-real-user"])],

        # Stdevs
        # Followers all
        [round(stdevs["stdev-followers-per-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followers-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followers-per-real-user"], DECIMALS_TO_ROUND)],
        # Followers large
        [round(stdevs["stdev-followers-per-large-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followers-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followers-per-large-real-user"], DECIMALS_TO_ROUND)],

        # Ranges
        # Followers all
        [int(ranges["range-followers-per-user"])],
        [int(ranges["range-followers-per-fake-user"])],
        [int(ranges["range-followers-per-real-user"])],
        # Followers large
        [int(ranges["range-followers-per-large-user"])],
        [int(ranges["range-followers-per-large-fake-user"])],
        [int(ranges["range-followers-per-large-real-user"])],

        # IQR
        # Followers all
        [int(iqrs["iqr-followers-per-user"])],
        [int(iqrs["iqr-followers-per-fake-user"])],
        [int(iqrs["iqr-followers-per-real-user"])],
        # Followers large
        [int(iqrs["iqr-followers-per-large-user"])],
        [int(iqrs["iqr-followers-per-large-fake-user"])],
        [int(iqrs["iqr-followers-per-large-real-user"])],

        # Skew
        # Followers all
        [round(skews["skew-followers-per-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followers-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followers-per-real-user"], DECIMALS_TO_ROUND)],
        # Followers large
        [round(skews["skew-followers-per-large-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followers-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followers-per-large-real-user"], DECIMALS_TO_ROUND)],

        # Kurtosis
        # Followers all
        [round(kurtosis["kurtosis-followers-per-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followers-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followers-per-real-user"], DECIMALS_TO_ROUND)],
        # Followers large
        [round(kurtosis["kurtosis-followers-per-large-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followers-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followers-per-large-real-user"], DECIMALS_TO_ROUND)],
    ]

    create_table(os.path.join("users", "followers_basic_stats.png"),
                 "Followers Basic Stats", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


def create_followings_per_user_table():
    """ Generates a table with basic statistics about the number of shares per article.
    """
    followers_per_user_stats = FollowStats(DATABASE)
    means = followers_per_user_stats.mean()
    medians = followers_per_user_stats.median()
    modes = followers_per_user_stats.mode()
    stdevs = followers_per_user_stats.stdev()
    ranges = followers_per_user_stats.range()
    iqrs = followers_per_user_stats.iqr()
    skews = followers_per_user_stats.skew()
    kurtosis = followers_per_user_stats.kurtosis()

    independent_vars = ["", "All", "Fake", "Real", "Large",
                        "L. Fake", "L. Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Stdev", "Range", "IQR",
                      "Skew", "Kurtosis"]

    values = [
        # Means
        # Followings all
        [round(means["mean-followings-per-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followings-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followings-per-real-user"], DECIMALS_TO_ROUND)],
        # Followings large
        [round(means["mean-followings-per-large-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followings-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-followings-per-large-real-user"], DECIMALS_TO_ROUND)],

        # Medians
        # Followings all
        [int(medians["median-followings-per-user"])],
        [int(medians["median-followings-per-fake-user"])],
        [int(medians["median-followings-per-real-user"])],
        # Followings large
        [int(medians["median-followings-per-large-user"])],
        [int(medians["median-followings-per-large-fake-user"])],
        [int(medians["median-followings-per-large-real-user"])],

        # Modes
        # Followings all
        [int(modes["mode-followings-per-user"])],
        [int(modes["mode-followings-per-fake-user"])],
        [int(modes["mode-followings-per-real-user"])],
        # Followings large
        [int(modes["mode-followings-per-large-user"])],
        [int(modes["mode-followings-per-large-fake-user"])],
        [int(modes["mode-followings-per-large-real-user"])],

        # Stdevs
        # Followings all
        [round(stdevs["stdev-followings-per-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followings-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followings-per-real-user"], DECIMALS_TO_ROUND)],
        # Followings large
        [round(stdevs["stdev-followings-per-large-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followings-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-followings-per-large-real-user"], DECIMALS_TO_ROUND)],

        # Ranges
        # Followings all
        [int(ranges["range-followings-per-user"])],
        [int(ranges["range-followings-per-fake-user"])],
        [int(ranges["range-followings-per-real-user"])],
        # Followings large
        [int(ranges["range-followings-per-large-user"])],
        [int(ranges["range-followings-per-large-fake-user"])],
        [int(ranges["range-followings-per-large-real-user"])],

        # IQR
        # Followings all
        [int(iqrs["iqr-followings-per-user"])],
        [int(iqrs["iqr-followings-per-fake-user"])],
        [int(iqrs["iqr-followings-per-real-user"])],
        # Followings large
        [int(iqrs["iqr-followings-per-large-user"])],
        [int(iqrs["iqr-followings-per-large-fake-user"])],
        [int(iqrs["iqr-followings-per-large-real-user"])],

        # Skew
        # Followings all
        [round(skews["skew-followings-per-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followings-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followings-per-real-user"], DECIMALS_TO_ROUND)],
        # Followings large
        [round(skews["skew-followings-per-large-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followings-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-followings-per-large-real-user"], DECIMALS_TO_ROUND)],

        # Kurtosis
        # Followings all
        [round(kurtosis["kurtosis-followings-per-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followings-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followings-per-real-user"], DECIMALS_TO_ROUND)],
        # Followings large
        [round(kurtosis["kurtosis-followings-per-large-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followings-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-followings-per-large-real-user"], DECIMALS_TO_ROUND)]
    ]

    create_table(os.path.join("users", "followings_basic_stats.png"),
                 "Followings Basic Stats", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


if __name__ == "__main__":
    create_followers_per_user_table()
    create_followings_per_user_table()
