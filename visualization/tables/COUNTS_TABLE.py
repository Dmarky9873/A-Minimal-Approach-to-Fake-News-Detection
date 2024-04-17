"""


    Author: Daniel Markusson


"""


from get_json_dict import DATABASE
from definitions import THEME
from create_table import create_table


def display_counts_table():
    """ Generates a table with counts of unique authors, fake articles, real articles, unique
        articles and unique users.
    """
    # TODO: Add a function that returns the number of unique users.
    # TODO: Add a function that returns the number of unique articles.
    # TODO: Add a function that returns the number of fake articles.
    # TODO: Add a function that returns the number of real articles.
    ...


def get_author_count():
    """ Returns the number of unique authors and the number of authors who publish both fake and
        real articles.

    Returns:
        tuple:  A tuple whos first element is the number of unique authors and the second element is
                the number of authors who publish both fake and real articles.
    """

    fake_authors = set()
    real_authors = set()

    for author in DATABASE["articles"]["fake-articles"]["authors"]:
        fake_authors.update(author)
    for author in DATABASE["articles"]["real-articles"]["authors"]:
        real_authors.update(author)

    authors_who_publish_both = fake_authors.intersection(real_authors)
    authors = fake_authors.union(real_authors)

    return len(authors), len(authors_who_publish_both)


def main():
    """ Function to be ran when the file is executed.
    """
    display_counts_table()


if __name__ == "__main__":
    main()
