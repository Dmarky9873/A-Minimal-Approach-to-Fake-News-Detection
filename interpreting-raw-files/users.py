"""


    Author: Daniel Markusson


"""

import linecache


def get_username(id_num: int, outlet: str):
    """Gets the unique username of user `ID` based on their outlet, `outlet`.

    Args:
        ID (`int`): The ID of the user, retrieved from the news-user relationship file.
        outlet (`str`): The outlet of user `ID`.

    Returns:
        `str`: The unique username of user `ID`.
    """
    if outlet == 'buzzfeed':
        return linecache.getline("./raw/BuzzFeedUser.txt", id_num).replace('\n', '')
    return linecache.getline("./raw/PolitiFactUser.txt", id_num).replace('\n', '')


def get_users():
    """Gets set of all users in dataset.

    Returns:
        `set`: Set of all users in a dataset.
    """

    users = set()
    with open("./raw/PolitiFactUser.txt", encoding="UTF-8") as f:
        for l in f:
            users.add(l.replace('\n', ''))

    with open("./raw/BuzzFeedUser.txt", encoding="UTF-8") as f:
        for l in f:
            users.add(l.replace('\n', ''))

    return users


def get_follow_relationships():
    """Gets the follow relationships of each user. VERY LARGE.

    Returns:
        `set`: Set of "a-follows-b" tuples.
    """
    a_follows_b = set()

    with open("./raw/BuzzFeedUserUser.txt", encoding="UTF-8") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a, b = int(l_[0]), int(l_[1])
            a, b = int(a), int(b)

            username_a = get_username(a, 'buzzfeed')
            username_b = get_username(b, 'buzzfeed')

            a_follows_b.add((username_a, username_b))

    with open("./raw/PolitiFactUserUser.txt", encoding="UTF-8") as f:
        for l in f:
            l_ = l.replace('\n', '').split('\t')
            a = int(l_[0])
            b = int(l_[1])

            a, b = int(a), int(b)

            username_a = get_username(a, 'politifact')
            username_b = get_username(b, 'politifact')

            a_follows_b.add((username_a, username_b))

    return a_follows_b