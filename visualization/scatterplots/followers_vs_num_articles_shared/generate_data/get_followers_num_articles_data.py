"""

    Author: Daniel Markusson

"""

from visualization.utils import get_user_distribution
from visualization.get_json_dict import DATABASE


def get_followers_shared_list():
    """ Get the number of followers and the number of articles shared for all users.

    Returns:
        list[tuple[int, int]]:  A list of tuples where each element is a tuple containing the number
                                of followers in the first element and the number of articles shared 
                                in the second element.
    """
    dist = get_user_distribution(DATABASE)

    l = []

    for user in dist['all-users']:
        num_followers = DATABASE['users']['counts'][user]['followers']['count']
        num_articles_shared = DATABASE['users']['counts'][user]['articles']['num-shared']
        l.append((num_articles_shared, num_followers))

    return l
