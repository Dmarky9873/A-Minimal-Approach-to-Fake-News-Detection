"""

    Author: Daniel Markusson
    

"""
import os
from visualization.tables.create_table import create_table
from visualization.tables.article_tables.generate_stats.article_counts import get_article_counts
from visualization.tables.article_tables.generate_stats.shares_per_article_stats import \
    SharesPerArticleStats
from visualization.get_json_dict import DATABASE
from definitions import DECIMALS_TO_ROUND


def create_articles_counts_table():
    """ Generates a table with counts of unique articles, fake articles, real articles, unique
        articles and unique users.
    """
    article_counts = get_article_counts()
    independent_vars = ["", "# Unique", "# Fake", "# Real"]
    dependent_vars = ["Counts"]
    values = [[article_counts["num-articles"]],
              [article_counts["num-fake-articles"]],
              [article_counts["num-real-articles"]]]
    create_table(os.path.join("articles", "articles_counts_table.png"), "Article Counts",
                 independent_vars, dependent_vars, values)


def create_shares_per_article_table():
    """ Generates a table with basic statistics about the number of shares per article.
    """
    shares_per_article_stats = SharesPerArticleStats(DATABASE)
    means = shares_per_article_stats.mean()
    medians = shares_per_article_stats.median()
    modes = shares_per_article_stats.mode()
    stdevs = shares_per_article_stats.stdev()
    ranges = shares_per_article_stats.range()
    iqrs = shares_per_article_stats.iqr()
    skews = shares_per_article_stats.skew()
    kurtosis = shares_per_article_stats.kurtosis()

    independent_vars = ["", "Shares/Article",
                        "Shares/Fake", "Shares/Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Stdev", "Range", "IQR",
                      "Skew", "Kurtosis"]

    values = [
        # Means
        [round(means["mean-shares-per-article"], DECIMALS_TO_ROUND)],
        [round(means["mean-shares-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(means["mean-shares-per-real-article"], DECIMALS_TO_ROUND)],
        # Medians
        [int(medians["median-shares-per-article"])],
        [int(medians["median-shares-per-fake-article"])],
        [int(medians["median-shares-per-real-article"])],
        # Modes
        [int(modes["mode-shares-per-article"])],
        [int(modes["mode-shares-per-fake-article"])],
        [int(modes["mode-shares-per-real-article"])],
        # Stdevs
        [round(stdevs["stdev-shares-per-article"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-shares-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(stdevs["stdev-shares-per-real-article"], DECIMALS_TO_ROUND)],
        # Ranges
        [int(ranges["range-shares-per-article"])],
        [int(ranges["range-shares-per-fake-article"])],
        [int(ranges["range-shares-per-real-article"])],
        # IQR
        [int(iqrs["iqr-shares-per-article"])],
        [int(iqrs["iqr-shares-per-fake-article"])],
        [int(iqrs["iqr-shares-per-real-article"])],
        # Skew
        [round(skews["skew-shares-per-article"], DECIMALS_TO_ROUND)],
        [round(skews["skew-shares-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(skews["skew-shares-per-real-article"], DECIMALS_TO_ROUND)],
        # Kurtosis
        [round(kurtosis["kurtosis-shares-per-article"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-shares-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-shares-per-real-article"], DECIMALS_TO_ROUND)]
    ]

    create_table(os.path.join("articles", "shares_per_article_basic_statistics.png"),
                 "Shares Per Article Basic Statistics", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


if __name__ == "__main__":
    create_articles_counts_table()
    create_shares_per_article_table()
