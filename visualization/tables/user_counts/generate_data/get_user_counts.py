"""

    Author: Daniel Markusson


"""
from visualization.get_json_dict import DATABASE
from visualization.utils import get_user_distribution


def get_user_counts():
    """ Get the total number of users in the database, the total number of users who exclusively 
        share fake articles, and the total number of users who exclusively share real articles, along with that, large sharer counts of the same things are included.

        * A large sharer is a user who has shared more than x̄ + 2Sₓ, where x̄ is the sample mean 
        number of shares per user and Sₓ is the sample standard deviation of the number of shares 
        per user.

    Returns:
        `dict`: A dictionary containing the counts outlined above.
    """
    dist = get_user_distribution(DATABASE)
    large_sharers = []
    for user in dist['all-users']:
        if DATABASE['users']['counts'][user]['articles']['num-shared'] > (1.5733 + (2 * 2.1422)):
            large_sharers.append(user)

    large_fake_sharers = []
    for fake_user in dist['fake-users']:
        if DATABASE['users']['counts'][fake_user]['articles']['num-shared'] > (1.373 + (2 * 1.2792)):
            large_fake_sharers.append(fake_user)

    large_real_sharers = []
    for real_user in dist['real-users']:
        if DATABASE['users']['counts'][real_user]['articles']['num-shared'] > (1.5899 + (2 * 2.7163)):
            large_real_sharers.append(real_user)

    return {'num-users': len(dist['all-users']),
            'num-fake-users': len(dist['fake-users']),
            'num-real-users': len(dist['real-users']),
            'num-large-sharers': len(large_sharers),
            'num-large-fake-sharers': len(large_fake_sharers),
            'num-large-real-sharers': len(large_real_sharers)}


def main():
    """ Main function for the script.
    """
    print(get_user_counts())


if __name__ == "__main__":
    main()
