"""

    Authors: Daniel Markusson


"""

from visualization.ecdfs.p_shares_vs_type_of_article.generate_stats.get_shares_lists import \
    get_shares_lists
from visualization.ecdfs.create_ecdf import create_comparitive_ecdf


def create_p_fake_vs_shares_ecdf():
    """
        Creates the ECDF of the probability to receive a certain number of shares based on the type
        of article.
    """
    shares_list, fake_shares_list, real_shares_list = get_shares_lists()

    combined_list = []
    labels = []
    for shares in shares_list:
        combined_list.append(shares)
        labels.append("Combined")
    for shares in fake_shares_list:
        combined_list.append(shares)
        labels.append("Fake")
    for shares in real_shares_list:
        combined_list.append(shares)
        labels.append("Real")

    create_comparitive_ecdf(combined_list, labels, ["Shares", "Type of Article"], "Type of Article",
                            "Shares",
                            "Proportion of an Amount of Shares Depending on the Type of Article",
                            "p_shares_vs_type_of_article.png")


def main():
    """ Main function for the script.
    """
    create_p_fake_vs_shares_ecdf()


if __name__ == "__main__":
    main()
