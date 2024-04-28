"""


    Author: Daniel Markusson


"""

import os
from visualization.tables.author_tables.generate_stats.authors_per_article_stats import \
    AuthorsPerArticleStats
from visualization.tables.author_tables.generate_stats.articles_per_author_stats import \
    ArticlesPerAuthorStats
from visualization.tables.author_tables.generate_stats.author_counts import get_author_counts
from visualization.get_json_dict import DATABASE
from visualization.tables.create_table import create_table
from definitions import DECIMALS_TO_ROUND

# Creating Tables


def create_authors_counts_table():
    """ Generates a table with counts of unique authors, fake articles, real articles, unique
        articles and unique users.
    """
    author_counts = get_author_counts()
    independent_vars = ["", "# Unique", "# Both",
                        "# ⨁ Fake", "# ⨁ Real"]
    dependent_vars = ["Counts"]
    values = [[author_counts["total-authors"]],
              [author_counts["authors-who-publish-both"]],
              [author_counts["exclusively-fake-authors"]],
              [author_counts["exclusively-real-authors"]]]
    create_table(os.path.join("authors", "authors_counts_table.png"), "Author Counts",
                 independent_vars, dependent_vars, values)


def create_authors_per_articles_table():
    """ Generates a table with the average number of authors per article, the average number of
        authors per fake article, and average number of authors per real article.
    """

    authors_per_article_stats = AuthorsPerArticleStats(DATABASE)
    means = authors_per_article_stats.mean()
    medians = authors_per_article_stats.median()
    modes = authors_per_article_stats.mode()
    variances = authors_per_article_stats.variance()
    ranges = authors_per_article_stats.range()
    iqrs = authors_per_article_stats.iqr()
    skews = authors_per_article_stats.skew()
    kurtosis = authors_per_article_stats.kurtosis()

    independent_vars = ["", "Authors/Article",
                        "Authors/Fake", "Authors/Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Var", "Range", "IQR",
                      "Skew", "Kurtosis"]
    values = [
        # Means
        [round(means["mean-authors-per-article"], DECIMALS_TO_ROUND)],
        [round(means["mean-authors-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(means["mean-authors-per-real-article"], DECIMALS_TO_ROUND)],
        # Medians
        [int(medians["median-authors-per-article"])],
        [int(medians["median-authors-per-fake-article"])],
        [int(medians["median-authors-per-real-article"])],
        # Modes
        [int(modes["mode-authors-per-article"])],
        [int(modes["mode-authors-per-fake-article"])],
        [int(modes["mode-authors-per-real-article"])],
        # Variances
        [round(variances["variance-authors-per-article"], DECIMALS_TO_ROUND)],
        [round(variances["variance-authors-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(variances["variance-authors-per-real-article"], DECIMALS_TO_ROUND)],
        # Ranges
        [int(ranges["range-authors-per-article"])],
        [int(ranges["range-authors-per-fake-article"])],
        [int(ranges["range-authors-per-real-article"])],
        # IQR
        [int(iqrs["iqr-authors-per-article"])],
        [int(iqrs["iqr-authors-per-fake-article"])],
        [int(iqrs["iqr-authors-per-real-article"])],
        # Skew
        [round(skews["skew-authors-per-article"], DECIMALS_TO_ROUND)],
        [round(skews["skew-authors-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(skews["skew-authors-per-real-article"], DECIMALS_TO_ROUND)],
        # Kurtosis
        [round(kurtosis["kurtosis-authors-per-article"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-authors-per-fake-article"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-authors-per-real-article"], DECIMALS_TO_ROUND)]
    ]

    create_table(os.path.join("authors", "authors_per_article_basic_statistics.png"),
                 "Authors Per Article Basic Statistics", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


def create_articles_per_author_table():
    """ Generates a table with the average number of authors per article, the average number of
        authors per fake article, and average number of authors per real article.
    """

    articles_per_author_stats = ArticlesPerAuthorStats(DATABASE)
    means = articles_per_author_stats.mean()
    medians = articles_per_author_stats.median()
    modes = articles_per_author_stats.mode()
    variances = articles_per_author_stats.variance()
    ranges = articles_per_author_stats.range()
    iqrs = articles_per_author_stats.iqr()
    skews = articles_per_author_stats.skew()
    kurtosis = articles_per_author_stats.kurtosis()

    independent_vars = ["", "Articles/Author",
                        "Articles/Fake", "Articles/Real"]
    dependent_vars = ["Mean", "Median", "Mode",
                      "Var", "Range", "IQR",
                      "Skew", "Kurtosis"]
    values = [
        # Means
        [round(means["mean-articles-per-author"], DECIMALS_TO_ROUND)],
        [round(means["mean-articles-per-fake-author"], DECIMALS_TO_ROUND)],
        [round(means["mean-articles-per-real-author"], DECIMALS_TO_ROUND)],
        # Medians
        [int(medians["median-articles-per-author"])],
        [int(medians["median-articles-per-fake-author"])],
        [int(medians["median-articles-per-real-author"])],
        # Modes
        [int(modes["mode-articles-per-author"])],
        [int(modes["mode-articles-per-fake-author"])],
        [int(modes["mode-articles-per-real-author"])],
        # Variances
        [round(variances["variance-articles-per-author"], DECIMALS_TO_ROUND)],
        [round(variances["variance-articles-per-fake-author"], DECIMALS_TO_ROUND)],
        [round(variances["variance-articles-per-real-author"], DECIMALS_TO_ROUND)],
        # Ranges
        [int(ranges["range-articles-per-author"])],
        [int(ranges["range-articles-per-fake-author"])],
        [int(ranges["range-articles-per-real-author"])],
        # IQR
        [int(iqrs["iqr-articles-per-author"])],
        [int(iqrs["iqr-articles-per-fake-author"])],
        [int(iqrs["iqr-articles-per-real-author"])],
        # Skew
        [round(skews["skew-articles-per-author"], DECIMALS_TO_ROUND)],
        [round(skews["skew-articles-per-fake-author"], DECIMALS_TO_ROUND)],
        [round(skews["skew-articles-per-real-author"], DECIMALS_TO_ROUND)],
        # Kurtosis
        [round(kurtosis["kurtosis-articles-per-author"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-articles-per-fake-author"], DECIMALS_TO_ROUND)],
        [round(kurtosis["kurtosis-articles-per-real-author"], DECIMALS_TO_ROUND)]
    ]

    create_table(os.path.join("authors", "articles_per_author_basic_statistics.png"),
                 "Articles Per Author Basic Statistics", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


def main():
    """ Function to be ran when the file is executed.
    """
    create_articles_per_author_table()
    create_authors_per_articles_table()
    create_authors_counts_table()


if __name__ == "__main__":
    main()
