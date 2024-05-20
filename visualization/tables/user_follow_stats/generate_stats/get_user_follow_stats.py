"""

    Author: Daniel Markusson


"""

import statistics
from scipy import stats
from visualization.utils import get_user_distribution


class FollowStats:
    """ Contains functions to get statistics about how users follow each other articles. 

        "Mean", "Median", "Mode",
        "Stdevstdev", "Range", "IQR",
        "Skew", "Kurtosis"
    """

    def __init__(self, database):

        self.all_users_followers = []
        self.fake_users_followers = []
        self.real_users_followers = []

        self.all_users_followings = []
        self.fake_users_followings = []
        self.real_users_followings = []

        self.large_users_followers = []
        self.large_fake_users_followers = []
        self.large_real_users_followers = []

        self.large_users_followings = []
        self.large_fake_users_followings = []
        self.large_real_users_followings = []

        user_dist = get_user_distribution(database)

        for user in user_dist['all-users']:
            num_followers = database['users']['counts'][user]['followers']['count']
            num_shared = database['users']['counts'][user]['articles']['num-shared']
            num_followings = database['users']['counts'][user]['following']['count']

            self.all_users_followers.append(num_followers)
            self.all_users_followings.append(num_followings)

            if num_shared > (1.5733 + (2 * 2.1422)):
                self.large_users_followers.append(num_followers)
                self.large_users_followings.append(num_followings)

        for user in user_dist['fake-users']:
            num_followers = database['users']['counts'][user]['followers']['count']
            num_shared = database['users']['counts'][user]['articles']['num-shared']
            num_followings = database['users']['counts'][user]['following']['count']

            self.fake_users_followers.append(num_followers)
            self.fake_users_followings.append(num_followings)

            if num_shared > (1.373 + (2 * 1.2792)):
                self.large_fake_users_followers.append(num_followers)
                self.large_fake_users_followings.append(num_followings)

        for user in user_dist['real-users']:
            num_followers = database['users']['counts'][user]['followers']['count']
            num_shared = database['users']['counts'][user]['articles']['num-shared']
            num_followings = database['users']['counts'][user]['following']['count']

            self.real_users_followers.append(num_followers)
            self.real_users_followings.append(num_followings)

            if num_shared > (1.5899 + (2 * 2.7163)):
                self.large_real_users_followers.append(num_followers)
                self.large_real_users_followings.append(num_followings)

    def mean(self):
        """ Returns the average number of shares per article, the average number of shares per

        Returns:
            `dict`: A dictionary containing the mean values outlined above.
        """
        return {
            # Followers per all users
            "mean-followers-per-user": statistics.mean(self.all_users_followers),
            "mean-followers-per-fake-user": statistics.mean(self.fake_users_followers),
            "mean-followers-per-real-user": statistics.mean(self.real_users_followers),

            # Followers per large users
            "mean-followers-per-large-user": statistics.mean(self.large_users_followers),
            "mean-followers-per-large-fake-user": statistics.mean(self.large_fake_users_followers),
            "mean-followers-per-large-real-user": statistics.mean(self.large_real_users_followers),

            # Followings per all users
            "mean-followings-per-user": statistics.mean(self.all_users_followings),
            "mean-followings-per-fake-user": statistics.mean(self.fake_users_followings),
            "mean-followings-per-real-user": statistics.mean(self.real_users_followings),

            # Followings per large users
            "mean-followings-per-large-user": statistics.mean(self.large_users_followers),
            "mean-followings-per-large-fake-user": statistics.mean(self.large_fake_users_followers),
            "mean-followings-per-large-real-user": statistics.mean(self.large_real_users_followers),
        }

    def median(self):
        """ Returns the median number of shares per article, the median number of shares per fake
            article, and the median number of shares per real article.

        Returns:
            `dict`: A dictionary containing the median values outlined above.
        """
        return {
            # Followers per all users
            "median-followers-per-user": statistics.median(self.all_users_followers),
            "median-followers-per-fake-user": statistics.median(self.fake_users_followers),
            "median-followers-per-real-user": statistics.median(self.real_users_followers),

            # Followers per large users
            "median-followers-per-large-user": statistics.median(self.large_users_followers),
            "median-followers-per-large-fake-user": statistics.median(self.large_fake_users_followers),
            "median-followers-per-large-real-user": statistics.median(self.large_real_users_followers),

            # Followings per all users
            "median-followings-per-user": statistics.median(self.all_users_followings),
            "median-followings-per-fake-user": statistics.median(self.fake_users_followings),
            "median-followings-per-real-user": statistics.median(self.real_users_followings),

            # Followings per large users
            "median-followings-per-large-user": statistics.median(self.large_users_followers),
            "median-followings-per-large-fake-user": statistics.median(self.large_fake_users_followers),
            "median-followings-per-large-real-user": statistics.median(self.large_real_users_followers),
        }

    def mode(self):
        """ Returns the mode number of shares per article, the mode number of shares per fake 
            article, and the mode number of shares per real article.

        Returns:
            `dict`: A dictionary containing the mode values outlined above.
        """
        return {
            # Followers per all users
            "mode-followers-per-user": statistics.mode(self.all_users_followers),
            "mode-followers-per-fake-user": statistics.mode(self.fake_users_followers),
            "mode-followers-per-real-user": statistics.mode(self.real_users_followers),

            # Followers per large users
            "mode-followers-per-large-user": statistics.mode(self.large_users_followers),
            "mode-followers-per-large-fake-user": statistics.mode(self.large_fake_users_followers),
            "mode-followers-per-large-real-user": statistics.mode(self.large_real_users_followers),

            # Followings per all users
            "mode-followings-per-user": statistics.mode(self.all_users_followings),
            "mode-followings-per-fake-user": statistics.mode(self.fake_users_followings),
            "mode-followings-per-real-user": statistics.mode(self.real_users_followings),

            # Followings per large users
            "mode-followings-per-large-user": statistics.mode(self.large_users_followers),
            "mode-followings-per-large-fake-user": statistics.mode(self.large_fake_users_followers),
            "mode-followings-per-large-real-user": statistics.mode(self.large_real_users_followers),
        }

    def stdev(self):
        """ Returns the stdev of the number of shares per article, the stdev of the number of 
            shares per fake article, and the stdev of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the variance values outlined above.
        """
        return {
            # Followers per all users
            "stdev-followers-per-user": statistics.stdev(self.all_users_followers),
            "stdev-followers-per-fake-user": statistics.stdev(self.fake_users_followers),
            "stdev-followers-per-real-user": statistics.stdev(self.real_users_followers),

            # Followers per large users
            "stdev-followers-per-large-user": statistics.stdev(self.large_users_followers),
            "stdev-followers-per-large-fake-user": statistics.stdev(self.large_fake_users_followers),
            "stdev-followers-per-large-real-user": statistics.stdev(self.large_real_users_followers),

            # Followings per all users
            "stdev-followings-per-user": statistics.stdev(self.all_users_followings),
            "stdev-followings-per-fake-user": statistics.stdev(self.fake_users_followings),
            "stdev-followings-per-real-user": statistics.stdev(self.real_users_followings),

            # Followings per large users
            "stdev-followings-per-large-user": statistics.stdev(self.large_users_followers),
            "stdev-followings-per-large-fake-user": statistics.stdev(self.large_fake_users_followers),
            "stdev-followings-per-large-real-user": statistics.stdev(self.large_real_users_followers),
        }

    def range(self):
        """ Returns the range of the number of shares per article, the range of the number of 
            shares per fake article, and the range of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the range values outlined above.
        """
        return {
            # Followers per all users
            "range-followers-per-user": max(self.all_users_followers) -
            min(self.all_users_followers),
            "range-followers-per-fake-user": max(self.fake_users_followers) -
            min(self.fake_users_followers),
            "range-followers-per-real-user": max(self.real_users_followers) -
            min(self.real_users_followers),

            # Followers per large users
            "range-followers-per-large-user": max(self.large_fake_users_followers) -
            min(self.large_fake_users_followers),
            "range-followers-per-large-fake-user": max(self.large_fake_users_followers) -
            min(self.large_fake_users_followers),
            "range-followers-per-large-real-user": max(self.large_real_users_followers) -
            min(self.large_real_users_followers),

            # Followings per all users
            "range-followings-per-user": max(self.all_users_followings) -
            min(self.all_users_followings),
            "range-followings-per-fake-user": max(self.fake_users_followings) -
            min(self.fake_users_followings),
            "range-followings-per-real-user": max(self.real_users_followings) -
            min(self.real_users_followings),

            # Followings per large users
            "range-followings-per-large-user": max(self.large_users_followings) -
            min(self.large_users_followings),
            "range-followings-per-large-fake-user": max(self.large_fake_users_followings) -
            min(self.large_fake_users_followings),
            "range-followings-per-large-real-user": max(self.large_real_users_followings) -
            min(self.large_real_users_followings),
        }

    def iqr(self):
        """ Returns the IQR of the number of shares per article, the IQR of the number of shares 
            per fake article, and the IQR of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the IQR values outlined above.
        """
        print(statistics.quantiles(self.all_users_followers, n=4)[2], "Q3 all")
        print(statistics.quantiles(
            self.fake_users_followers, n=4)[2], "Q3 fake")
        print(statistics.quantiles(
            self.real_users_followers, n=4)[2], "Q3 real")
        return {
            # Followers per all users
            "iqr-followers-per-user": statistics.quantiles(self.all_users_followers, n=4)[2] -
            statistics.quantiles(self.all_users_followers, n=4)[0],
            "iqr-followers-per-fake-user": statistics.quantiles(self.fake_users_followers, n=4)[2] -
            statistics.quantiles(self.fake_users_followers, n=4)[0],
            "iqr-followers-per-real-user": statistics.quantiles(self.real_users_followers, n=4)[2] -
            statistics.quantiles(self.real_users_followers, n=4)[0],

            # Followers per large users
            "iqr-followers-per-large-user": statistics.quantiles(self.large_fake_users_followers, n=4)[2] -
            statistics.quantiles(self.large_fake_users_followers, n=4)[0],
            "iqr-followers-per-large-fake-user": statistics.quantiles(self.large_fake_users_followers, n=4)[2] -
            statistics.quantiles(self.large_fake_users_followers, n=4)[0],
            "iqr-followers-per-large-real-user": statistics.quantiles(self.large_real_users_followers, n=4)[2] -
            statistics.quantiles(self.large_real_users_followers, n=4)[0],

            # Followings per all users
            "iqr-followings-per-user": statistics.quantiles(self.all_users_followings, n=4)[2] -
            statistics.quantiles(self.all_users_followings, n=4)[0],
            "iqr-followings-per-fake-user": statistics.quantiles(self.fake_users_followings, n=4)[2] -
            statistics.quantiles(self.fake_users_followings, n=4)[0],
            "iqr-followings-per-real-user": statistics.quantiles(self.real_users_followings, n=4)[2] -
            statistics.quantiles(self.real_users_followings, n=4)[0],

            # Followings per large users
            "iqr-followings-per-large-user": statistics.quantiles(self.large_users_followings, n=4)[2] -
            statistics.quantiles(self.large_users_followings, n=4)[0],
            "iqr-followings-per-large-fake-user": statistics.quantiles(self.large_fake_users_followings, n=4)[2] -
            statistics.quantiles(self.large_fake_users_followings, n=4)[0],
            "iqr-followings-per-large-real-user": statistics.quantiles(self.large_real_users_followings, n=4)[2] -
            statistics.quantiles(self.large_real_users_followings, n=4)[0],
        }

    def skew(self):
        """ Returns the skew of the number of shares per article, the skew of the number of shares 
            per fake article, and the skew of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the skew values outlined above.
        """
        return {
            # Followers per all users
            "skew-followers-per-user": stats.skew(self.all_users_followers),
            "skew-followers-per-fake-user": stats.skew(self.fake_users_followers),
            "skew-followers-per-real-user": stats.skew(self.real_users_followers),

            # Followers per large users
            "skew-followers-per-large-user": stats.skew(self.large_users_followers),
            "skew-followers-per-large-fake-user": stats.skew(self.large_fake_users_followers),
            "skew-followers-per-large-real-user": stats.skew(self.large_real_users_followers),

            # Followings per all users
            "skew-followings-per-user": stats.skew(self.all_users_followings),
            "skew-followings-per-fake-user": stats.skew(self.fake_users_followings),
            "skew-followings-per-real-user": stats.skew(self.real_users_followings),

            # Followings per large users
            "skew-followings-per-large-user": stats.skew(self.large_users_followers),
            "skew-followings-per-large-fake-user": stats.skew(self.large_fake_users_followers),
            "skew-followings-per-large-real-user": stats.skew(self.large_real_users_followers),
        }

    def kurtosis(self):
        """ Returns the kurtosis of the number of shares per article, the kurtosis of the number of 
            shares per fake article, and the kurtosis of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the kurtosis values outlined above.
        """
        return {
            # Followers per all users
            "kurtosis-followers-per-user": stats.kurtosis(self.all_users_followers),
            "kurtosis-followers-per-fake-user": stats.kurtosis(self.fake_users_followers),
            "kurtosis-followers-per-real-user": stats.kurtosis(self.real_users_followers),

            # Followers per large users
            "kurtosis-followers-per-large-user": stats.kurtosis(self.large_users_followers),
            "kurtosis-followers-per-large-fake-user": stats.kurtosis(self.large_fake_users_followers),
            "kurtosis-followers-per-large-real-user": stats.kurtosis(self.large_real_users_followers),

            # Followings per all users
            "kurtosis-followings-per-user": stats.kurtosis(self.all_users_followings),
            "kurtosis-followings-per-fake-user": stats.kurtosis(self.fake_users_followings),
            "kurtosis-followings-per-real-user": stats.kurtosis(self.real_users_followings),

            # Followings per large users
            "kurtosis-followings-per-large-user": stats.kurtosis(self.large_users_followers),
            "kurtosis-followings-per-large-fake-user": stats.kurtosis(self.large_fake_users_followers),
            "kurtosis-followings-per-large-real-user": stats.kurtosis(self.large_real_users_followers),
        }

# TODO: IMPLIMENT POPULAR USERS
