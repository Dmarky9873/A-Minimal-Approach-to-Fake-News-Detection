"""


    Author: Daniel Markusson


"""

from visualization.scatterplots.p_fake_vs_length.generate_stats.get_proportion_fake_per_length \
    import get_proportion_fake_per_lengths
from visualization.scatterplots.create_scatterplot import create_scatterplot


def create_scatterplot_p_fake_vs_length():
    """ Create a scatterplot of the proportion of fake articles per share interval. """
    p_fake_per_length = get_proportion_fake_per_lengths()
    create_scatterplot(p_fake_per_length,
                       'Length (in Characters)', 'Proportion Fake',
                       "Proportion of Fake Articles at Different Article Lengths",
                       "p_fake_vs_lengths.png")


def main():
    """Main function for creating the scatterplot."""
    create_scatterplot_p_fake_vs_length()


if __name__ == '__main__':
    main()
