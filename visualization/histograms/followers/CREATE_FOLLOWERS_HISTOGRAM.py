"""

    Author: Daniel Markusson

"""

from visualization.histograms.followers.generate_data.get_followers_data import get_followers_lists
from visualization.histograms.create_histogram import create_comparitive_histogram


def create_followers_histogram():
    """ Create a histogram of the followers.
    """
    followers, labels = get_followers_lists()

    create_comparitive_histogram(
        followers, labels, ["Number of Followers", "Is Fake/Real"],
        "Is Fake/Real", "Number of Followers",
        "Histogram of Number of Followers Compared Across the Types of Users",
        "followers_histogram.png")


def main():
    """ Create the followers histogram.
    """
    create_followers_histogram()


if __name__ == "__main__":
    main()
