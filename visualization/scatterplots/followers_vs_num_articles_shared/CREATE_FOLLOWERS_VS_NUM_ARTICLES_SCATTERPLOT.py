"""

    Authors: Daniel Markusson

"""

from visualization.scatterplots.followers_vs_num_articles_shared.generate_data.get_followers_num_articles_data import get_followers_shared_list
from visualization.scatterplots.create_scatterplot import create_scatterplot


def create_followers_vs_num_articles_scatterplot():
    """ Create a scatterplot of the number of followers vs the number of articles shared.
    """
    create_scatterplot(get_followers_shared_list(), "Articles Shared", "Followers",
                       "Followers vs Articles Shared", "followers_vs_num_articles_shared.png")


if __name__ == "__main__":
    create_followers_vs_num_articles_scatterplot()
