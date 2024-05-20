"""

    Author: Daniel Markusson
    

"""
import os
from visualization.tables.create_table import create_table
from visualization.tables.user_basic_stats.generate_stats.get_user_sharing_basic_stats import \
    UserSharingStats
from visualization.get_json_dict import DATABASE
from definitions import DECIMALS_TO_ROUND


def create_shares_per_user_table():
    """ Generates a table with basic statistics about the number of shares per article.
    """
    shares_per_user_stats = UserSharingStats(DATABASE)
    means = shares_per_user_stats.mean()
    medians = shares_per_user_stats.median()
    modes = shares_per_user_stats.mode()
    stdevs = shares_per_user_stats.stdev()
    ranges = shares_per_user_stats.range()
    iqrs = shares_per_user_stats.iqr()
    skews = shares_per_user_stats.skew()
    kurtosis = shares_per_user_stats.kurtosis()

    independent_vars = ["", "Shares/User",
                        "Shares/Fake", "Shares/Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Stdev", "Range", "IQR",
                      "Skew", "Kurtosis"]

    values = [
        # Means
        [round(means["mean-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(means["mean-shares-per-real-user"], DECIMALS_TO_ROUND)],
        # Medians
        [int(medians["median-shares-per-user"])],
        [int(medians["median-shares-per-fake-user"])],
        [int(medians["median-shares-per-real-user"])],
        # Modes
        [int(modes["mode-shares-per-user"])],
        [int(modes["mode-shares-per-fake-user"])],
        [int(modes["mode-shares-per-real-user"])],
        # Stdevs
        [round(stdevs["stdev-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-shares-per-real-user"], DECIMALS_TO_ROUND)],
        # Ranges
        [int(ranges["range-shares-per-user"])],
        [int(ranges["range-shares-per-fake-user"])],
        [int(ranges["range-shares-per-real-user"])],
        # IQR
        [int(iqrs["iqr-shares-per-user"])],
        [int(iqrs["iqr-shares-per-fake-user"])],
        [int(iqrs["iqr-shares-per-real-user"])],
        # Skew
        [round(skews["skew-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(skews["skew-shares-per-real-user"], DECIMALS_TO_ROUND)],
        # Kurtosis
        [round(kurtosis["kurtosis-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-shares-per-real-user"], DECIMALS_TO_ROUND)]
    ]

    create_table(os.path.join("users", "shares_per_user_basic_statistics.png"),
                 "Shares Per User Basic Statistics", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


if __name__ == "__main__":
    create_shares_per_user_table()
