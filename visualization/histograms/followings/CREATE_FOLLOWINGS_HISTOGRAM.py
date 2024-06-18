"""

    Author: Daniel Markusson

"""

from visualization.histograms.followings.generate_data.get_followings_data import get_followings_lists
from visualization.histograms.create_histogram import create_comparitive_histogram


def create_followings_histogram():
    """ Create a histogram of the followers.
    """
    followings, labels = get_followings_lists()

    create_comparitive_histogram(
        followings, labels, ["Number of Followers", "Is Fake/Real"],
        "Is Fake/Real", "Number of Followers",
        "Followings Across Fake and Real Users",
        "followings_histogram.png")


def main():
    """ Create the followers histogram.
    """
    create_followings_histogram()


if __name__ == "__main__":
    main()
