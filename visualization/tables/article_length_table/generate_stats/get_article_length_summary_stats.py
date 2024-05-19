"""

    Author: Daniel Markusson

"""

import statistics
from scipy import stats


class LengthOfArticleStats:
    """ Contains functions to get statistics about the length of articles. 

        "Mean", "Median", "Mode",
        "Stdevstdev", "Range", "IQR",
        "Skew", "Kurtosis"
    """

    def __init__(self, database):
        """ Initializes the AuthorsPerArticleStats class.

        Args:
            database (`dict`): The main database containing all information.
        """

        self.lengths_of_articles = []
        self.lengths_of_fakes = []
        self.lengths_of_reals = []

        for body, title in zip(database["articles"]["fake-articles"]["bodies"],
                               database["articles"]["fake-articles"]["titles"]):
            self.lengths_of_fakes.append(len(body) + len(title))
            self.lengths_of_articles.append(len(body) + len(title))
        for body, title in zip(database["articles"]["real-articles"]["bodies"],
                               database["articles"]["real-articles"]["titles"]):
            self.lengths_of_reals.append(len(body) + len(title))
            self.lengths_of_articles.append(len(body) + len(title))

    def mean(self):
        """ Returns the average length of articles, the average length of fake articles, and the
            average length of real articles.

        Returns:
            `dict`: A dictionary containing the mean values outlined above.
        """
        return {"mean-article-length": statistics.mean(self.lengths_of_articles),
                "mean-fake-article-length": statistics.mean(self.lengths_of_fakes),
                "mean-real-article-length": statistics.mean(self.lengths_of_reals)}

    def median(self):
        """ Returns the median length of articles, the median length of fake articles, and the
            median length of real articles.

        Returns:
            `dict`: A dictionary containing the median values outlined above.
        """
        return {"median-article-length": statistics.median(self.lengths_of_articles),
                "median-fake-article-length": statistics.median(self.lengths_of_fakes),
                "median-real-article-length": statistics.median(self.lengths_of_reals)}

    def mode(self):
        """ Returns the mode length of articles, the mode length of fake articles, and the
            mode length of real articles.

        Returns:
            `dict`: A dictionary containing the mode values outlined above.
        """
        return {"mode-article-length": statistics.mode(self.lengths_of_articles),
                "mode-fake-article-length": statistics.mode(self.lengths_of_fakes),
                "mode-real-article-length": statistics.mode(self.lengths_of_reals)}

    def stdev(self):
        """ Returns the stdev of the length of articles, the stdev of the length of fake articles,
            and the stdev of the length of real articles.

        Returns:
            `dict`: A dictionary containing the stdev values outlined above.
        """
        return {"stdev-article-length": statistics.stdev(self.lengths_of_articles),
                "stdev-fake-article-length": statistics.stdev(self.lengths_of_fakes),
                "stdev-real-article-length": statistics.stdev(self.lengths_of_reals)}

    def range(self):
        """ Returns the range of the length of articles, the range of the length of fake articles,
            and the range of the length of real articles.

        Returns:
            `dict`: A dictionary containing the range values outlined above.
        """
        return {"range-article-length": max(self.lengths_of_articles) - min(self.lengths_of_articles),
                "range-fake-article-length": max(self.lengths_of_fakes) - min(self.lengths_of_fakes),
                "range-real-article-length": max(self.lengths_of_reals) - min(self.lengths_of_reals)}

    def iqr(self):
        """ Returns the IQR of the length of each article, the IQR of the length of each fake 
            article, and the IQR of the length of each real article.

        Returns:
            `dict`: A dictionary containing the IQR values outlined above.
        """
        return {"iqr-article-length": statistics.quantiles(self.lengths_of_articles, n=4)[2] -
                statistics.quantiles(self.lengths_of_articles, n=4)[0],
                "iqr-fake-article-length": statistics.quantiles(self.lengths_of_fakes,
                                                                n=4)[2] -
                statistics.quantiles(self.lengths_of_fakes, n=4)[0],
                "iqr-real-article-length": statistics.quantiles(self.lengths_of_reals,
                                                                n=4)[2] -
                statistics.quantiles(self.lengths_of_reals, n=4)[0]}

    def skew(self):
        """ Returns the skew of the length of articles, the skew of the length of fake articles,
            and the skew of the length of real articles.

        Returns:
            `dict`: A dictionary containing the skew values outlined above.
        """
        return {"skew-article-length": stats.skew(self.lengths_of_articles),
                "skew-fake-article-length": stats.skew(self.lengths_of_fakes),
                "skew-real-article-length": stats.skew(self.lengths_of_reals)}

    def kurtosis(self):
        """ Returns the kurtosis of the length of articles, the kurtosis of the length of fake 
            articles, and the kurtosis of the length of real articles.

        Returns:
            `dict`: A dictionary containing the kurtosis values outlined above.
        """
        return {"kurtosis-article-length": stats.kurtosis(self.lengths_of_articles),
                "kurtosis-fake-article-length": stats.kurtosis(self.lengths_of_fakes),
                "kurtosis-real-article-length": stats.kurtosis(self.lengths_of_reals)}
