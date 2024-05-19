"""


    Author: Daniel Markusson


"""

from visualization.scatterplots.p_fake_vs_authors.generate_stats.\
    get_proportion_fake_per_num_authors import get_proportion_fake_per_num_authors
from visualization.scatterplots.create_scatterplot import create_scatterplot


def create_scatterplot_p_fake_vs_num_authors():
    """ Create a scatterplot of the proportion of fake articles per share interval. """
    p_fake_per_num_authors = get_proportion_fake_per_num_authors()
    create_scatterplot(p_fake_per_num_authors,
                       'Number of Authors', 'Proportion Fake',
                       "Proportion of Fake Articles at Different Numbers of Authors",
                       "p_fake_vs_num_authors.png")


def main():
    """Main function for creating the scatterplot."""
    create_scatterplot_p_fake_vs_num_authors()


if __name__ == '__main__':
    main()
