"""


    Author: Daniel Markusson


"""

from visualization.utils import is_article_fake, get_all_article_ids
from visualization.get_json_dict import DATABASE

SMALL_LIMIT = 3
INTERVAL_SIZE = 1000


def get_num_fake_real_per_lengths(interval_size):
    """ Get the number of fake and real articles per share interval.

    Returns:
        `dict`: A dictionary containing the number of fake and real articles per share interval.
    """
    lengths_dict = {}

    for uid in get_all_article_ids(DATABASE):
        if is_article_fake(uid):
            article_index = DATABASE["articles"]["fake-articles"]["ids"].index(
                uid)
            length = len(DATABASE["articles"]
                         ["fake-articles"]["bodies"][article_index])//interval_size
        else:
            article_index = DATABASE["articles"]["real-articles"]["ids"].index(
                uid)
            length = len(DATABASE["articles"]
                         ["real-articles"]["bodies"][article_index])//interval_size

        try:
            lengths_dict[length]
        except KeyError:
            lengths_dict[length] = {'fake': 0, 'real': 0}

        if is_article_fake(uid):
            lengths_dict[length]["fake"] += 1
        else:
            lengths_dict[length]["real"] += 1

    too_small = set()
    for length, fake_real_dict in lengths_dict.items():
        if fake_real_dict["fake"] + fake_real_dict["real"] <= SMALL_LIMIT:
            too_small.add(length)

    too_small_fake_accum = 0
    too_small_real_accum = 0
    for length in too_small:
        too_small_fake_accum += lengths_dict[length]["fake"]
        too_small_real_accum += lengths_dict[length]["real"]

        del lengths_dict[length]

    return lengths_dict


def get_proportion_fake_per_lengths(interval_size=INTERVAL_SIZE):
    """ Get the proportion of fake articles per share interval.

    Returns:
        `list[tuple(int, int)]`:    A list of tuples containing the share interval and the 
                                    proportion of fake articles.
    """
    lengths_per_fake_real_article = get_num_fake_real_per_lengths(
        interval_size)

    lengths_per_proportion_fake_real = {}

    for authors, fake_real_dict in lengths_per_fake_real_article.items():

        lengths_per_proportion_fake_real[authors*interval_size] = fake_real_dict["fake"] / \
            (fake_real_dict["fake"] + fake_real_dict["real"])

    list_lengths_per_proportion_fake_real = list(
        lengths_per_proportion_fake_real.items())

    list_lengths_per_proportion_fake_real.sort()

    return list_lengths_per_proportion_fake_real


def main():
    """Main function for the script."""
    print(get_proportion_fake_per_lengths())


if __name__ == "__main__":
    main()
