"""

    Author: Daniel Markusson


"""

import statistics
from scipy import stats
from visualization.utils import get_all_article_ids, is_article_fake


class SharesPerArticleStats:
    """ Contains functions to get statistics about the number of shares per article. 

        "Mean", "Median", "Mode",
        "Stdevstdev", "Range", "IQR",
        "Skew", "Kurtosis"
    """

    def __init__(self, database):
        """ Initializes the AuthorsPerArticleStats class.

        Args:
            database (`dict`):  The main database containing all information.
        """

        self.shares_per_article = []
        self.shares_per_fake_article = []
        self.shares_per_real_article = []

        for uid in get_all_article_ids(database):
            shares = database["articles"]["counts"][uid]["shares"]
            self.shares_per_article.append(shares)
            if is_article_fake(uid):
                self.shares_per_fake_article.append(shares)
            else:
                self.shares_per_real_article.append(shares)

    def mean(self):
        """ Returns the average number of shares per article, the average number of shares per

        Returns:
            `dict`: A dictionary containing the mean values outlined above.
        """
        return {"mean-shares-per-article": statistics.mean(self.shares_per_article),
                "mean-shares-per-fake-article": statistics.mean(self.shares_per_fake_article),
                "mean-shares-per-real-article": statistics.mean(self.shares_per_real_article)}

    def median(self):
        """ Returns the median number of shares per article, the median number of shares per fake
            article, and the median number of shares per real article.

        Returns:
            `dict`: A dictionary containing the median values outlined above.
        """
        return {"median-shares-per-article": statistics.median(self.shares_per_article),
                "median-shares-per-fake-article": statistics.median(self.shares_per_fake_article),
                "median-shares-per-real-article": statistics.median(self.shares_per_real_article)}

    def mode(self):
        """ Returns the mode number of shares per article, the mode number of shares per fake 
            article, and the mode number of shares per real article.

        Returns:
            `dict`: A dictionary containing the mode values outlined above.
        """
        return {"mode-shares-per-article": statistics.mode(self.shares_per_article),
                "mode-shares-per-fake-article": statistics.mode(self.shares_per_fake_article),
                "mode-shares-per-real-article": statistics.mode(self.shares_per_real_article)}

    def stdev(self):
        """ Returns the stdev of the number of shares per article, the stdev of the number of 
            shares per fake article, and the stdev of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the variance values outlined above.
        """
        return {"stdev-shares-per-article": statistics.stdev(self.shares_per_article),
                "stdev-shares-per-fake-article": statistics.stdev(self.shares_per_fake_article),
                "stdev-shares-per-real-article": statistics.stdev(self.shares_per_real_article)}

    def range(self):
        """ Returns the range of the number of shares per article, the range of the number of 
            shares per fake article, and the range of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the range values outlined above.
        """
        return {"range-shares-per-article": max(self.shares_per_article) -
                min(self.shares_per_article),
                "range-shares-per-fake-article": max(self.shares_per_fake_article) -
                min(self.shares_per_fake_article),
                "range-shares-per-real-article": max(self.shares_per_real_article) -
                min(self.shares_per_real_article)}

    def iqr(self):
        """ Returns the IQR of the number of shares per article, the IQR of the number of shares 
            per fake article, and the IQR of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the IQR values outlined above.
        """
        return {"iqr-shares-per-article": statistics.quantiles(self.shares_per_article, n=4)[2] -
                statistics.quantiles(self.shares_per_article, n=4)[0],
                "iqr-shares-per-fake-article": statistics.quantiles(self.shares_per_fake_article,
                                                                    n=4)[2] -
                statistics.quantiles(self.shares_per_fake_article, n=4)[0],
                "iqr-shares-per-real-article": statistics.quantiles(self.shares_per_real_article,
                                                                    n=4)[2] -
                statistics.quantiles(self.shares_per_real_article, n=4)[0]}

    def skew(self):
        """ Returns the skew of the number of shares per article, the skew of the number of shares 
            per fake article, and the skew of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the skew values outlined above.
        """
        return {"skew-shares-per-article": stats.skew(self.shares_per_article),
                "skew-shares-per-fake-article": stats.skew(self.shares_per_fake_article),
                "skew-shares-per-real-article": stats.skew(self.shares_per_real_article)}

    def kurtosis(self):
        """ Returns the kurtosis of the number of shares per article, the kurtosis of the number of 
            shares per fake article, and the kurtosis of the number of shares per real article.

        Returns:
            `dict`: A dictionary containing the kurtosis values outlined above.
        """
        return {"kurtosis-shares-per-article": stats.kurtosis(self.shares_per_article),
                "kurtosis-shares-per-fake-article": stats.kurtosis(self.shares_per_fake_article),
                "kurtosis-shares-per-real-article": stats.kurtosis(self.shares_per_real_article)}
