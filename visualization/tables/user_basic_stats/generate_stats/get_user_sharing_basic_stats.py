"""

    Author: Daniel Markusson


"""

import statistics
from scipy import stats
from visualization.utils import get_user_distribution


class UserSharingStats:
    """ Contains functions to get statistics about how users share articles. 

        "Mean", "Median", "Mode",
        "Stdevstdev", "Range", "IQR",
        "Skew", "Kurtosis"
    """

    def __init__(self, database):
        """ Initializes the AuthorsPerArticleStats class.

        Args:
            database (`dict`):  The main database containing all information.
        """

        self.shares_per_user = []
        self.shares_per_fake_user = []
        self.shares_per_real_user = []

        dist = get_user_distribution(database)

        for user in dist['all-users']:
            shares = database['users']['counts'][user]['articles']['num-shared']
            self.shares_per_user.append(shares)

        for fake_user in dist['fake-users']:
            shares = database['users']['counts'][fake_user]['articles']['num-shared']
            self.shares_per_fake_user.append(shares)

        for real_user in dist['real-users']:
            shares = database['users']['counts'][real_user]['articles']['num-shared']
            self.shares_per_real_user.append(shares)

    def mean(self):
        """ Returns the average number of shares per article, the average number of shares per

        Returns:
            `dict`: A dictionary containing the mean values outlined above.
        """
        return {"mean-shares-per-user": statistics.mean(self.shares_per_user),
                "mean-shares-per-fake-user": statistics.mean(self.shares_per_fake_user),
                "mean-shares-per-real-user": statistics.mean(self.shares_per_real_user)}

    def median(self):
        """ Returns the median number of shares per article, the median number of shares per fake
            article, and the median number of shares per real article.

        Returns:
            `dict`: A dictionary containing the median values outlined above.
        """
        return {"median-shares-per-user": statistics.median(self.shares_per_user),
                "median-shares-per-fake-user": statistics.median(self.shares_per_fake_user),
                "median-shares-per-real-user": statistics.median(self.shares_per_real_user)}

    def mode(self):
        """ Returns the mode number of shares per article, the mode number of shares per fake 
            article, and the mode number of shares per real article.

        Returns:
            `dict`: A dictionary containing the mode values outlined above.
        """
        return {"mode-shares-per-user": statistics.mode(self.shares_per_user),
                "mode-shares-per-fake-user": statistics.mode(self.shares_per_fake_user),
                "mode-shares-per-real-user": statistics.mode(self.shares_per_real_user)}

    def stdev(self):
        """ Returns the stdev of the number of shares per article, the stdev of the number of 
            shares per fake article, and the stdev of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the variance values outlined above.
        """
        return {"stdev-shares-per-user": statistics.stdev(self.shares_per_user),
                "stdev-shares-per-fake-user": statistics.stdev(self.shares_per_fake_user),
                "stdev-shares-per-real-user": statistics.stdev(self.shares_per_real_user)}

    def range(self):
        """ Returns the range of the number of shares per article, the range of the number of 
            shares per fake article, and the range of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the range values outlined above.
        """
        return {"range-shares-per-user": max(self.shares_per_user) -
                min(self.shares_per_user),
                "range-shares-per-fake-user": max(self.shares_per_fake_user) -
                min(self.shares_per_fake_user),
                "range-shares-per-real-user": max(self.shares_per_real_user) -
                min(self.shares_per_real_user)}

    def iqr(self):
        """ Returns the IQR of the number of shares per article, the IQR of the number of shares 
            per fake article, and the IQR of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the IQR values outlined above.
        """
        return {"iqr-shares-per-user": statistics.quantiles(self.shares_per_user, n=4)[2] -
                statistics.quantiles(self.shares_per_user, n=4)[0],
                "iqr-shares-per-fake-user": statistics.quantiles(self.shares_per_fake_user,
                                                                 n=4)[2] -
                statistics.quantiles(self.shares_per_fake_user, n=4)[0],
                "iqr-shares-per-real-user": statistics.quantiles(self.shares_per_real_user,
                                                                 n=4)[2] -
                statistics.quantiles(self.shares_per_real_user, n=4)[0]}

    def skew(self):
        """ Returns the skew of the number of shares per article, the skew of the number of shares 
            per fake article, and the skew of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the skew values outlined above.
        """
        return {"skew-shares-per-user": stats.skew(self.shares_per_user),
                "skew-shares-per-fake-user": stats.skew(self.shares_per_fake_user),
                "skew-shares-per-real-user": stats.skew(self.shares_per_real_user)}

    def kurtosis(self):
        """ Returns the kurtosis of the number of shares per article, the kurtosis of the number of 
            shares per fake article, and the kurtosis of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the kurtosis values outlined above.
        """
        return {"kurtosis-shares-per-user": stats.kurtosis(self.shares_per_user),
                "kurtosis-shares-per-fake-user": stats.kurtosis(self.shares_per_fake_user),
                "kurtosis-shares-per-real-user": stats.kurtosis(self.shares_per_real_user)}
