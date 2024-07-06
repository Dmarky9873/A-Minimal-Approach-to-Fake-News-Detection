"""

    Authors: Daniel Markusson


"""

from visualization.ecdfs.readability.generate_stats.get_readability_indexes import get_readability_analysis
from visualization.ecdfs.create_ecdf import create_comparitive_ecdf


def create_readability_ecdf():
    """
        Creates the ECDF of the probability to receive a certain number of shares based on the type
        of article.
    """
    labels, scores = get_readability_analysis()

    create_comparitive_ecdf(scores, labels, ["Readability", "Type of Article"], "Type of Article",
                            "Readability",
                            "Dale-Chall Readability vs. Type of Article",
                            "readability_ecdf.png", xlabel="Dale-Chall Readability Index",
                            log_scale=False)


if __name__ == "__main__":
    create_readability_ecdf()
