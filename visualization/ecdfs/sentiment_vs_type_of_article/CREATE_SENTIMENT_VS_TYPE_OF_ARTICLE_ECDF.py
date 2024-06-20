"""

    Authors: Daniel Markusson


"""

from visualization.ecdfs.sentiment_vs_type_of_article.generate_stats.get_sentiment_stats import \
    get_sentiment_analysis
from visualization.ecdfs.create_ecdf import create_comparitive_ecdf


def create_sentiment_ecdf():
    """
        Creates the ECDF of the probability to receive a certain number of shares based on the type
        of article.
    """
    labels, scores = get_sentiment_analysis()

    create_comparitive_ecdf(scores, labels, ["Sentiment", "Type of Article"], "Type of Article",
                            "Sentiment",
                            "Textual Sentiment vs. Type of Article",
                            "sentiment_ecdf.png", xlabel="Sentiment Score (-1 to 1)",
                            log_scale=False)


if __name__ == "__main__":
    create_sentiment_ecdf()
