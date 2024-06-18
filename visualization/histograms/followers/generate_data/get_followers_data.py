"""

    Author: Daniel Markusson

"""

from visualization.utils import get_user_distribution
from visualization.get_json_dict import DATABASE


def get_followers_lists():
    """ Gets the number of followers for all users and labels them as fake, real or both/neither.

    Returns:
        tuple[list[int], list[str]]:    The tuple of lists containing the number of followers and
                                        the label of each user.
    """
    user_dist = get_user_distribution(DATABASE)
    followers = []
    labels = []
    for user in user_dist['all-users']:
        num_followers = DATABASE['users']['counts'][user]['followers']['count']
        if user in user_dist['fake-users']:
            labels.append('Fake')
            followers.append(num_followers)
        elif user in user_dist['real-users']:
            labels.append('Real')
            followers.append(num_followers)
    return followers, labels


if __name__ == "__main__":
    print(get_followers_lists())
