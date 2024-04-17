"""


    Author: Daniel Markusson


"""

import os
from get_json_dict import DATABASE
from create_table import create_table
from definitions import DECIMALS_TO_ROUND


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
    averages = get_avg_authors_per_article()
    independent_vars = ["", "Authors/Article",
                        "Authors/Fake", "Authors/Real"]
    dependent_vars = ["Average"]
    values = [[round(averages[0], DECIMALS_TO_ROUND)], [round(averages[1], DECIMALS_TO_ROUND)], [
        round(averages[2], DECIMALS_TO_ROUND)]]

    create_table(os.path.join("authors", "average_authors_per_article_table.png"),
                 "Average Authors per Article", independent_vars, dependent_vars, values)


def get_author_counts():
    """ Returns the number of authors in the database, the number of authors who publish both fake 
        and real articles, the number of authors who exclusively publish fake articles, and the 
        number of authors who exclusively publish real articles.

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

    return {"total-authors": len(authors),
            "authors-who-publish-both": len(authors_who_publish_both),
            "exclusively-fake-authors": len(exclusively_fake_authors),
            "exclusively-real-authors": len(exclusively_real_authors)}


def get_avg_authors_per_article():
    """ Returns the average number of authors per article, the average number of authors per fake 
        article, and the average number of authors per real article.

    Returns:
        `tuple`:    A tuple containing the average number of authors per article, the average number 
                    of authoers per fake article, and the average number of authors per real 
                    article.
    """
    avg_authors_per_article = 0
    avg_authors_per_fake_article = 0
    avg_authors_per_real_article = 0

    for authors in DATABASE["articles"]["fake-articles"]["authors"]:
        avg_authors_per_article += len(authors)
        avg_authors_per_fake_article += len(authors)

    for authors in DATABASE["articles"]["real-articles"]["authors"]:
        avg_authors_per_article += len(authors)
        avg_authors_per_real_article += len(authors)

    avg_authors_per_article /= len(DATABASE["articles"]["fake-articles"]["ids"]) + len(
        DATABASE["articles"]["real-articles"]["ids"])

    avg_authors_per_real_article /= len(
        DATABASE["articles"]["real-articles"]["ids"])

    avg_authors_per_fake_article /= len(
        DATABASE["articles"]["fake-articles"]["ids"])

    return avg_authors_per_article, avg_authors_per_fake_article, avg_authors_per_real_article


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
    all_authors = author_types["total-authors"]
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
