"""


    Author: Daniel Markusson


"""

from visualization.utils import is_article_fake, get_all_article_ids
from visualization.get_json_dict import DATABASE

SMALL_LIMIT = 1
INTERVAL_SIZE = 1


def get_num_fake_real_per_num_authors(interval_size):
    """ Get the number of fake and real articles per share interval.

    Returns:
        `dict`: A dictionary containing the number of fake and real articles per share interval.
    """
    authors_dict = {}

    for uid in get_all_article_ids(DATABASE):
        if is_article_fake(uid):
            article_index = DATABASE["articles"]["fake-articles"]["ids"].index(
                uid)
            authors = len(DATABASE["articles"]
                          ["fake-articles"]["authors"][article_index])//interval_size
        else:
            article_index = DATABASE["articles"]["real-articles"]["ids"].index(
                uid)
            authors = len(DATABASE["articles"]
                          ["real-articles"]["authors"][article_index])//interval_size

        try:
            authors_dict[authors]
        except KeyError:
            authors_dict[authors] = {'fake': 0, 'real': 0}

        if is_article_fake(uid):
            authors_dict[authors]["fake"] += 1
        else:
            authors_dict[authors]["real"] += 1

    too_small = set()
    for authors, fake_real_dict in authors_dict.items():
        if fake_real_dict["fake"] + fake_real_dict["real"] <= SMALL_LIMIT:
            too_small.add(authors)

    too_small_fake_accum = 0
    too_small_real_accum = 0
    for authors in too_small:
        too_small_fake_accum += authors_dict[authors]["fake"]
        too_small_real_accum += authors_dict[authors]["real"]

        del authors_dict[authors]

    return authors_dict


def get_proportion_fake_per_num_authors(interval_size=INTERVAL_SIZE):
    """ Get the proportion of fake articles per share interval.

    Returns:
        `list[tuple(int, int)]`:    A list of tuples containing the share interval and the 
                                    proportion of fake articles.
    """
    num_authors_fake_real_dict = get_num_fake_real_per_num_authors(
        interval_size)

    num_authors_proportion_fake_real = {}

    for authors, fake_real_dict in num_authors_fake_real_dict.items():

        num_authors_proportion_fake_real[authors*interval_size] = fake_real_dict["fake"] / \
            (fake_real_dict["fake"] + fake_real_dict["real"])

    list_num_authors_proportion_fake_real = list(
        num_authors_proportion_fake_real.items())

    list_num_authors_proportion_fake_real.sort()

    return list_num_authors_proportion_fake_real


def main():
    """Main function for the script."""
    print(get_proportion_fake_per_num_authors())


if __name__ == "__main__":
    main()
