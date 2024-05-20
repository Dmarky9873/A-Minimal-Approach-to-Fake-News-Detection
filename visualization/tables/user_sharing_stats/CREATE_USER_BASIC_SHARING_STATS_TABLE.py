"""

    Author: Daniel Markusson
    

"""
import os
from visualization.tables.create_table import create_table
from visualization.tables.user_sharing_stats.generate_stats.get_user_sharing_basic_stats import \
    UserSharingStats, LargeUserSharingStats
from visualization.get_json_dict import DATABASE
from definitions import DECIMALS_TO_ROUND


def create_shares_per_user_table():
    """ Generates a table with basic statistics about the number of shares per article.
    """
    shares_per_normal_user_stats = UserSharingStats(DATABASE)
    means_normal = shares_per_normal_user_stats.mean()
    medians_normal = shares_per_normal_user_stats.median()
    modes_normal = shares_per_normal_user_stats.mode()
    stdevs_normal = shares_per_normal_user_stats.stdev()
    ranges_normal = shares_per_normal_user_stats.range()
    iqrs_normal = shares_per_normal_user_stats.iqr()
    skews_normal = shares_per_normal_user_stats.skew()
    kurtosis_normal = shares_per_normal_user_stats.kurtosis()

    shares_per_large_user_stats = LargeUserSharingStats(DATABASE)
    means_large = shares_per_large_user_stats.mean()
    medians_large = shares_per_large_user_stats.median()
    modes_large = shares_per_large_user_stats.mode()
    stdevs_large = shares_per_large_user_stats.stdev()
    ranges_large = shares_per_large_user_stats.range()
    iqrs_large = shares_per_large_user_stats.iqr()
    skews_large = shares_per_large_user_stats.skew()
    kurtosis_large = shares_per_large_user_stats.kurtosis()

    independent_vars = ["", "All", "Fake", "Real", "Large",
                        "L. Fake", "L. Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Stdev", "Range", "IQR",
                      "Skew", "Kurtosis"]

    values = [
        # Means
        [round(means_normal["mean-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(means_normal["mean-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(means_normal["mean-shares-per-real-user"], DECIMALS_TO_ROUND)],
        [round(means_large["mean-shares-per-large-user"], DECIMALS_TO_ROUND)],
        [round(means_large["mean-shares-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(means_large["mean-shares-per-large-real-user"], DECIMALS_TO_ROUND)],
        # Medians
        [int(medians_normal["median-shares-per-user"])],
        [int(medians_normal["median-shares-per-fake-user"])],
        [int(medians_normal["median-shares-per-real-user"])],
        [int(medians_large["median-shares-per-large-user"])],
        [int(medians_large["median-shares-per-large-fake-user"])],
        [int(medians_large["median-shares-per-large-real-user"])],
        # Modes
        [int(modes_normal["mode-shares-per-user"])],
        [int(modes_normal["mode-shares-per-fake-user"])],
        [int(modes_normal["mode-shares-per-real-user"])],
        [int(modes_large["mode-shares-per-large-user"])],
        [int(modes_large["mode-shares-per-large-fake-user"])],
        [int(modes_large["mode-shares-per-large-real-user"])],
        # Stdevs
        [round(stdevs_normal["stdev-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(stdevs_normal["stdev-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(stdevs_normal["stdev-shares-per-real-user"], DECIMALS_TO_ROUND)],
        [round(stdevs_large["stdev-shares-per-large-user"], DECIMALS_TO_ROUND)],
        [round(stdevs_large["stdev-shares-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(stdevs_large["stdev-shares-per-large-real-user"], DECIMALS_TO_ROUND)],
        # Ranges
        [int(ranges_normal["range-shares-per-user"])],
        [int(ranges_normal["range-shares-per-fake-user"])],
        [int(ranges_normal["range-shares-per-real-user"])],
        [int(ranges_large["range-shares-per-large-user"])],
        [int(ranges_large["range-shares-per-large-fake-user"])],
        [int(ranges_large["range-shares-per-large-real-user"])],
        # IQR
        [int(iqrs_normal["iqr-shares-per-user"])],
        [int(iqrs_normal["iqr-shares-per-fake-user"])],
        [int(iqrs_normal["iqr-shares-per-real-user"])],
        [int(iqrs_large["iqr-shares-per-large-user"])],
        [int(iqrs_large["iqr-shares-per-large-fake-user"])],
        [int(iqrs_large["iqr-shares-per-large-real-user"])],
        # Skew
        [round(skews_normal["skew-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(skews_normal["skew-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(skews_normal["skew-shares-per-real-user"], DECIMALS_TO_ROUND)],
        [round(skews_large["skew-shares-per-large-user"], DECIMALS_TO_ROUND)],
        [round(skews_large["skew-shares-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(skews_large["skew-shares-per-large-real-user"], DECIMALS_TO_ROUND)],
        # Kurtosis
        [round(kurtosis_normal["kurtosis-shares-per-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis_normal["kurtosis-shares-per-fake-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis_normal["kurtosis-shares-per-real-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis_large["kurtosis-shares-per-large-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis_large["kurtosis-shares-per-large-fake-user"], DECIMALS_TO_ROUND)],
        [round(kurtosis_large["kurtosis-shares-per-large-real-user"], DECIMALS_TO_ROUND)]
    ]

    create_table(os.path.join("users", "shares_per_user_basic_statistics.png"),
                 "Shares Per User Basic Statistics", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


if __name__ == "__main__":
    create_shares_per_user_table()
