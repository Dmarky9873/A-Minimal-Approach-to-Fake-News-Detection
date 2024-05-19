"""

    Author: Daniel Markusson


"""

from visualization.utils import is_article_fake, get_all_article_ids
from visualization.get_json_dict import DATABASE


def get_shares_lists():
    """ Gets the number of shares for each article in the database and returns them in three 
        lists: one with all types of articles, one with only fake articles and one with only 
        real articles.

    Returns:
        `tuple[list[int], list[int], list[int]]`:   A tuple where the first element is the number of 
                                                    shares for all articles, the second element is 
                                                    the number of shares for fake articles, and the 
                                                    third element is the number of shares for real 
                                                    articles.
    """
    shares_list = []
    fake_shares_list = []
    real_shares_list = []

    for uid in get_all_article_ids(DATABASE):
        shares = DATABASE["articles"]["counts"][uid]["shares"]
        shares_list.append(shares)

        if is_article_fake(uid):
            fake_shares_list.append(shares)
        else:
            real_shares_list.append(shares)

    return shares_list, fake_shares_list, real_shares_list
