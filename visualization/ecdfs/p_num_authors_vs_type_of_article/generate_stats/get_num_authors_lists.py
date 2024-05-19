"""

    Author: Daniel Markusson


"""

from visualization.utils import is_article_fake, get_all_article_ids
from visualization.get_json_dict import DATABASE


def get_num_authors_lists():
    """ Get the number of authors for all articles, fake articles and real articles.

    Returns:
        `tuple`:    A tuple containing three lists, the first list contains the number of authors 
                    for all articles, the second list contains the number of authors for fake 
                    articles and the third list contains the number of authors for real articles.
    """
    all_articles = []
    fake_articles = []
    real_articles = []

    for uid in get_all_article_ids(DATABASE):
        if is_article_fake(uid):
            article_index = DATABASE["articles"]["fake-articles"]["ids"].index(
                uid)
            authors = len(DATABASE["articles"]
                          ["fake-articles"]["authors"][article_index])
            fake_articles.append(authors)
        else:
            article_index = DATABASE["articles"]["real-articles"]["ids"].index(
                uid)
            authors = len(DATABASE["articles"]
                          ["real-articles"]["authors"][article_index])
            real_articles.append(authors)
        all_articles.append(authors)

    return all_articles, fake_articles, real_articles
