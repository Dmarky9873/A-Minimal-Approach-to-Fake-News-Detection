"""

    Author: Daniel Markusson

"""

from visualization.utils import get_user_distribution
from visualization.get_json_dict import DATABASE

IQR_ALL = 32
Q1_ALL = 3
Q3_ALL = 35
LOWER_OUTLIER_LESS_THAN_ALL = Q1_ALL - 1.5 * IQR_ALL
UPPER_OUTLIER_GREATER_THAN_ALL = 500

IQR_FAKE = 27
Q1_FAKE = 3
Q3_FAKE = 30
LOWER_OUTLIER_LESS_THAN_FAKE = Q1_FAKE - 1.5 * IQR_FAKE
UPPER_OUTLIER_GREATER_THAN_FAKE = 500

IQR_REAL = 39
Q1_REAL = 4
Q3_REAL = 43
LOWER_OUTLIER_LESS_THAN_REAL = Q1_REAL - 1.5 * IQR_REAL
UPPER_OUTLIER_GREATER_THAN_REAL = 500


def get_followings_lists():
    """ Gets the number of followers for all users and labels them as fake, real or both/neither.

    Returns:
        tuple[list[int], list[str]]:    The tuple of lists containing the number of followers and
                                        the label of each user.
    """
    user_dist = get_user_distribution(DATABASE)
    fake_followings = []
    real_followings = []
    labels = []
    for user in user_dist['all-users']:
        num_following = DATABASE['users']['counts'][user]['following']['count']
        if user in user_dist['fake-users']:
            if not (num_following < LOWER_OUTLIER_LESS_THAN_FAKE or num_following >
                    UPPER_OUTLIER_GREATER_THAN_FAKE):
                labels.append('Fake')
                fake_followings.append(num_following)
        elif user in user_dist['real-users']:
            if not (num_following < LOWER_OUTLIER_LESS_THAN_REAL or num_following >
                    UPPER_OUTLIER_GREATER_THAN_REAL):
                labels.append('Real')
                real_followings.append(num_following)
    return fake_followings + real_followings, labels


if __name__ == "__main__":
    print(get_followings_lists())
