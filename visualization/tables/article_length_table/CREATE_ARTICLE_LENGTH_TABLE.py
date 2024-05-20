"""

    Author: Daniel Markusson

"""

import os
from visualization.tables.create_table import create_table
from visualization.tables.article_length_table.generate_stats.get_article_length_summary_stats \
    import LengthOfArticleStats
from visualization.get_json_dict import database
from definitions import DECIMALS_TO_ROUND


def create_length_of_articles_table():
    """ Generates a table with basic statistics about the number of shares per article.
    """
    length_of_article_stats = LengthOfArticleStats(database)
    means = length_of_article_stats.mean()
    medians = length_of_article_stats.median()
    modes = length_of_article_stats.mode()
    stdevs = length_of_article_stats.stdev()
    ranges = length_of_article_stats.range()
    iqrs = length_of_article_stats.iqr()
    skews = length_of_article_stats.skew()
    kurtosis = length_of_article_stats.kurtosis()

    independent_vars = ["", "Both",
                        "Fake", "Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Stdev", "Range", "IQR",
                      "Skew", "Kurtosis"]

    values = [
        # Means
        [round(means["mean-article-length"], DECIMALS_TO_ROUND)],
        [round(means["mean-fake-article-length"], DECIMALS_TO_ROUND)],
        [round(means["mean-real-article-length"], DECIMALS_TO_ROUND)],
        # Medians
        [int(medians["median-article-length"])],
        [int(medians["median-fake-article-length"])],
        [int(medians["median-real-article-length"])],
        # Modes
        [int(modes["mode-article-length"])],
        [int(modes["mode-fake-article-length"])],
        [int(modes["mode-real-article-length"])],
        # Stdevs
        [round(stdevs["stdev-article-length"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-fake-article-length"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-real-article-length"], DECIMALS_TO_ROUND)],
        # Ranges
        [int(ranges["range-article-length"])],
        [int(ranges["range-fake-article-length"])],
        [int(ranges["range-real-article-length"])],
        # IQR
        [int(iqrs["iqr-article-length"])],
        [int(iqrs["iqr-fake-article-length"])],
        [int(iqrs["iqr-real-article-length"])],
        # Skew
        [round(skews["skew-article-length"], DECIMALS_TO_ROUND)],
        [round(skews["skew-fake-article-length"], DECIMALS_TO_ROUND)],
        [round(skews["skew-real-article-length"], DECIMALS_TO_ROUND)],
        # Kurtosis
        [round(kurtosis["kurtosis-article-length"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-fake-article-length"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-real-article-length"], DECIMALS_TO_ROUND)]
    ]

    create_table(os.path.join("length", "length_of_articles_basic_stats.png"),
                 "Length of Articles Basic Statistics", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


def main():
    """ Main function for creating the table.
    """
    create_length_of_articles_table()


if __name__ == "__main__":
    main()
