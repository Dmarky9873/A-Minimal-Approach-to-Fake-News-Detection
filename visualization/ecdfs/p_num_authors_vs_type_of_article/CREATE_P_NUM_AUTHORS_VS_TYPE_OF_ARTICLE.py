"""

    Authors: Daniel Markusson


"""

from visualization.ecdfs.p_num_authors_vs_type_of_article.generate_stats.get_num_authors_lists import \
    get_num_authors_lists
from visualization.ecdfs.create_ecdf import create_comparitive_ecdf


def create_p_fake_vs_num_authors_ecdf():
    """
        Creates the ECDF of the probability to have a certain number of authors based on the type
        of article.
    """
    fake_articles, real_articles = get_num_authors_lists()

    combined_list = []
    labels = []
    for num_authors in fake_articles:
        combined_list.append(num_authors)
        labels.append("Fake")
    for num_authors in real_articles:
        combined_list.append(num_authors)
        labels.append("Real")

    create_comparitive_ecdf(combined_list, labels, ["Number of Authors", "Type of Article"],
                            "Type of Article",
                            "Number of Authors",
                            "Number of Authors vs. Type of Article",
                            "p_num_authors_vs_type_of_article.png")


def main():
    """ Main function for the script.
    """
    create_p_fake_vs_num_authors_ecdf()


if __name__ == "__main__":
    main()
