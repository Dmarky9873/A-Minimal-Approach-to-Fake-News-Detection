"""

    Authors: Daniel Markusson


"""

from visualization.ecdfs.semantics_vs_type_of_article.generate_stats.get_semantics_stats import \
    get_semantic_analysis
from visualization.ecdfs.create_ecdf import create_comparitive_ecdf


def create_semantics_ecdf():
    """
        Creates the ECDF of the probability to receive a certain number of shares based on the type
        of article.
    """
    labels, scores = get_semantic_analysis()

    print(scores)

    create_comparitive_ecdf(scores, labels, ["Semantics", "Type of Article"], "Type of Article",
                            "Semantics",
                            "Textual Semantics vs. Type of Article",
                            "semantics_ecdf.png", xlabel="Semantic Score (-1 to 1)",
                            log_scale=False)


if __name__ == "__main__":
    create_semantics_ecdf()
