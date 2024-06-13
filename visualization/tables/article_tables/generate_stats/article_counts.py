"""

    Author: Daniel Markusson


"""
from visualization.get_json_dict import DATABASE


def get_article_counts():
    """ Get the number of articles in the DATABASE, the number of fake articles, and the number of 
        real articles.

    Returns:
        `dict`: A dictionary with the number of articles, fake articles, and real articles.
    """
    num_fake_articles = len(DATABASE["articles"]["fake-articles"]["ids"])
    num_real_articles = len(DATABASE["articles"]["real-articles"]["ids"])
    num_articles = num_fake_articles + num_real_articles
    return {"num-articles": num_articles,
            "num-fake-articles": num_fake_articles,
            "num-real-articles": num_real_articles}
