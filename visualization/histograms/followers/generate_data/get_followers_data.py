"""

    Author: Daniel Markusson

"""

from visualization.utils import get_user_distribution
from visualization.get_json_dict import DATABASE

IQR_ALL = 32
Q1_ALL = 3
Q3_ALL = 35
LOWER_OUTLIER_LESS_THAN_ALL = Q1_ALL - 1.5 * IQR_ALL
UPPER_OUTLIER_GREATER_THAN_ALL = Q3_ALL + 1.5 * IQR_ALL

IQR_FAKE = 27
Q1_FAKE = 3
Q3_FAKE = 30
LOWER_OUTLIER_LESS_THAN_FAKE = Q1_FAKE - 1.5 * IQR_FAKE
UPPER_OUTLIER_GREATER_THAN_FAKE = Q3_FAKE + 1.5 * IQR_FAKE

IQR_REAL = 39
Q1_REAL = 4
Q3_REAL = 43
LOWER_OUTLIER_LESS_THAN_REAL = Q1_REAL - 1.5 * IQR_REAL
UPPER_OUTLIER_GREATER_THAN_REAL = Q3_REAL + 1.5 * IQR_REAL


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
            if not (num_followers < LOWER_OUTLIER_LESS_THAN_FAKE or num_followers >
                    UPPER_OUTLIER_GREATER_THAN_FAKE):
                labels.append('Fake')
                followers.append(num_followers)
        elif user in user_dist['real-users']:
            if not (num_followers < LOWER_OUTLIER_LESS_THAN_REAL or num_followers >
                    UPPER_OUTLIER_GREATER_THAN_REAL):
                labels.append('Real')
                followers.append(num_followers)
        else:
            if not (num_followers < LOWER_OUTLIER_LESS_THAN_ALL or num_followers >
                    UPPER_OUTLIER_GREATER_THAN_ALL):
                labels.append('Both/Neither')
                followers.append(num_followers)
    return followers, labels


if __name__ == "__main__":
    print(get_followers_lists())
