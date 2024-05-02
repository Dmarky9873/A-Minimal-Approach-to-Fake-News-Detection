"""


    Author: Daniel Markusson


"""

from get_proportion_fake_per_share import get_proportion_fake_per_share
from visualization.two_dimensional_charts.scatterplots.create_scatterplot import create_scatterplot


def create_scatterplot_p_fake_vs_shares():
    """ Create a scatterplot of the proportion of fake articles per share interval. """
    p_fake_per_share = get_proportion_fake_per_share()
    create_scatterplot(p_fake_per_share,
                       'Number of Shares', 'Proportion Fake',
                       "Proportion of Fake Articles at Different Numbers of Shares",
                       "p_fake_vs_shares.png")


def main():
    """Main function for creating the scatterplot."""
    create_scatterplot_p_fake_vs_shares()


if __name__ == '__main__':
    main()
