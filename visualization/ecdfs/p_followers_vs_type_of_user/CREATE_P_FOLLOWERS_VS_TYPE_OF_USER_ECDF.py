"""

    Author: Daniel Markusson

"""

from visualization.ecdfs.p_followers_vs_type_of_user.generate_data.get_followers_data import \
    get_followers_lists
from visualization.ecdfs.create_ecdf import create_comparitive_ecdf


def create_followers_ecdf():
    """ Create a histogram of the followers.
    """
    followers, labels = get_followers_lists()

    create_comparitive_ecdf(
        followers, labels, ["Number of Followers", "Is Fake/Real"],
        "Is Fake/Real", "Number of Followers",
        "Number of Followers vs. Type of User",
        "p_followers_vs_type_of_user_ecdf.png")


def main():
    """ Create the followers histogram.
    """
    create_followers_ecdf()


if __name__ == "__main__":
    main()
