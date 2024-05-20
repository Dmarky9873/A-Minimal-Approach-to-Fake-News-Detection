"""


    Author: Daniel Markusson


"""

from visualization.utils import is_article_fake, get_all_article_ids
from visualization.get_json_dict import database

SMALL_LIMIT = 3
INTERVAL_SIZE = 50


def get_num_fake_real_per_share(interval_size):
    """ Get the number of fake and real articles per share interval.

    Returns:
        `dict`: A dictionary containing the number of fake and real articles per share interval.
    """
    shares_dict = {}

    for uid in get_all_article_ids(database):
        shares = database["articles"]["counts"][uid]["shares"]//interval_size

        try:
            shares_dict[shares]
        except KeyError:
            shares_dict[shares] = {'fake': 0, 'real': 0}

        if is_article_fake(uid):
            shares_dict[shares]["fake"] += 1
        else:
            shares_dict[shares]["real"] += 1

    too_small = set()
    for shares, fake_real_dict in shares_dict.items():
        if fake_real_dict["fake"] + fake_real_dict["real"] <= SMALL_LIMIT:
            too_small.add(shares)

    too_small_fake_accum = 0
    too_small_real_accum = 0
    for shares in too_small:
        too_small_fake_accum += shares_dict[shares]["fake"]
        too_small_real_accum += shares_dict[shares]["real"]

        del shares_dict[shares]

    return shares_dict


def get_proportion_fake_per_share(interval_size=INTERVAL_SIZE):
    """ Get the proportion of fake articles per share interval.

    Returns:
        `list[tuple(int, int)]`:    A list of tuples containing the share interval and the 
                                    proportion of fake articles.
    """
    shares_fake_real_dict = get_num_fake_real_per_share(interval_size)

    shares_proportion_fake_real = {}

    for shares, fake_real_dict in shares_fake_real_dict.items():

        shares_proportion_fake_real[shares*interval_size] = fake_real_dict["fake"] / \
            (fake_real_dict["fake"] + fake_real_dict["real"])

    list_shares_proportion_fake_real = list(
        shares_proportion_fake_real.items())

    list_shares_proportion_fake_real.sort()

    return list_shares_proportion_fake_real


def main():
    """Main function for the script."""
    print(get_proportion_fake_per_share())


if __name__ == "__main__":
    main()
