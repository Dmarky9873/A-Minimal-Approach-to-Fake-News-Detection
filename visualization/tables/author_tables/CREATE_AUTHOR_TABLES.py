"""


    Author: Daniel Markusson


"""

import os
from authors_per_article_stats import AuthorsPerArticleStats
from author_counts import get_author_counts
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


def create_average_authors_per_articles_table():
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
        [int(iqrs["iqr-authors-per-real-article"])]
        # TODO: Impliment skew and kurtosis
    ]

    create_table(os.path.join("authors", "authors_per_article_basic_statistics.png"),
                 "Authors Per Article Basic Statistics", independent_vars, dependent_vars, values,
                 height=500, title_y=0.85)


def create_avg_articles_per_author_table():
    """ Generates a table with the average number of articles per author, the average number of
        articles per exlusively fake author, and the average number of articles per exclusively real
        author.
    """
    averages = get_avg_articles_per_author()
    independent_vars = ["", "Average Articles/Author",
                        "Aricles/Fake", "Articles/Real"]
    dependent_vars = ["Average"]
    values = [[round(averages["average-num-articles-per-author"], DECIMALS_TO_ROUND)],
              [round(averages["average-num-articles-per-excl-fake-author"],
                     DECIMALS_TO_ROUND)],
              [round(averages["average-num-articles-per-excl-real-author"], DECIMALS_TO_ROUND)]]

    create_table(os.path.join("authors", "average_articles_per_author_table.png"),
                 "Average Articles per Author", independent_vars, dependent_vars, values)


def get_authors():
    """ Returns all authors in the database, authors who publish both fake and real articles,
        authors who exclusively publish fake articles, and authors who exclusively publish real
        articles.

    Returns:
        `dict`: A dictionary containing values outlined above.
    """
    fake_authors = set()
    real_authors = set()

    for author in DATABASE["articles"]["fake-articles"]["authors"]:
        fake_authors.update(author)
    for author in DATABASE["articles"]["real-articles"]["authors"]:
        real_authors.update(author)

    authors_who_publish_both = fake_authors.intersection(real_authors)
    authors = fake_authors.union(real_authors)
    exclusively_fake_authors = fake_authors.difference(real_authors)
    exclusively_real_authors = real_authors.difference(fake_authors)

    return {"every-author": authors,
            "authors-who-publish-both": authors_who_publish_both,
            "exclusively-fake-authors": exclusively_fake_authors,
            "exclusively-real-authors": exclusively_real_authors}


def get_avg_articles_per_author():
    """ Returns the average number of articles per author, the average number of articles per
        exclusively fake author, and the average number of articles per exclusively real author.

    Returns:
        `dict`: A dictionary containing values outlined above.
    """
    author_types = get_authors()
    exclusively_fake_authors = author_types["exclusively-fake-authors"]
    exclusively_real_authors = author_types["exclusively-real-authors"]
    all_authors = author_types["every-author"]
    avg_articles_per_author = 0
    avg_articles_per_exclusively_fake_author = 0
    avg_articles_per_exclusively_real_author = 0

    article_counts = dict()

    for author in all_authors:
        article_counts[author] = 0

    for fake_authors, real_authors in zip(DATABASE["articles"]["fake-articles"]["authors"],
                                          DATABASE["articles"]["real-articles"]["authors"]):
        for fake_author in fake_authors:
            article_counts[fake_author] += 1
        for real_author in real_authors:
            article_counts[real_author] += 1

    for author in all_authors:
        avg_articles_per_author += article_counts[author]
        if author in exclusively_fake_authors:
            avg_articles_per_exclusively_fake_author += article_counts[author]
        if author in exclusively_real_authors:
            avg_articles_per_exclusively_real_author += article_counts[author]

    avg_articles_per_author /= len(all_authors)
    avg_articles_per_exclusively_fake_author /= len(exclusively_fake_authors)
    avg_articles_per_exclusively_real_author /= len(exclusively_real_authors)

    return {"average-num-articles-per-author": avg_articles_per_author,
            "average-num-articles-per-excl-fake-author": avg_articles_per_exclusively_fake_author,
            "average-num-articles-per-excl-real-author": avg_articles_per_exclusively_real_author}


def main():
    """ Function to be ran when the file is executed.
    """
    create_average_authors_per_articles_table()


if __name__ == "__main__":
    main()
