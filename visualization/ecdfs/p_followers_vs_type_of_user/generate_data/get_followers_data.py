"""

    Author: Daniel Markusson

"""

from visualization.utils import get_user_distribution
from visualization.get_json_dict import DATABASE


def get_followers_lists():
    user_dist = get_user_distribution(DATABASE)
    followers = []
    labels = []
    for user in user_dist['all-users']:
        num_followers = DATABASE['users']['counts'][user]['followers']['count']
        followers.append(num_followers)
        if user in user_dist['fake-users']:
            labels.append('Fake')
        elif user in user_dist['real-users']:
            labels.append('Real')
        else:
            labels.append('Both/Neither')
    return followers, labels


if __name__ == "__main__":
    print(get_followers_lists())
