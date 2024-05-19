"""

    Author: Daniel Markusson


"""

import statistics
from scipy import stats


class AuthorsPerArticleStats:
    """ Contains functions to get statistics about the number of authors per article. 

        "Mean", "Median", "Mode",
        "Stdev", "Range", "IQR",
        "Skew", "Kurtosis"
        """

    def __init__(self, database):
        """ Initializes the AuthorsPerArticleStats class.

        Args:
            database (`dict`):  The database containing the articles.
        """
        self.authors_per_article = []
        self.authors_per_fake_article = []
        self.authors_per_real_article = []

        for authors in database["articles"]["fake-articles"]["authors"]:
            self.authors_per_article.append(len(authors))
            self.authors_per_fake_article.append(len(authors))

        for authors in database["articles"]["real-articles"]["authors"]:
            self.authors_per_article.append(len(authors))
            self.authors_per_real_article.append(len(authors))

    def mean(self):
        """ Returns the average number of authors per article, the average number of authors per 
            fake article, and the average number of authors per real article.

        Returns:
            `dict`: A dictionary containing the mean values outlined above.
        """

        return {"mean-authors-per-article": statistics.mean(self.authors_per_article),
                "mean-authors-per-fake-article": statistics.mean(self.authors_per_fake_article),
                "mean-authors-per-real-article": statistics.mean(self.authors_per_real_article)}

    def median(self):
        """ Returns the median number of authors per article, the median number of authors per fake 
            article, and the median number of authors per real article.

        Returns:
            `dict`: A dictionary containing the median values outlined above.
        """

        return {"median-authors-per-article": statistics.median(self.authors_per_article),
                "median-authors-per-fake-article": statistics.median(self.authors_per_fake_article),
                "median-authors-per-real-article": statistics.median(self.authors_per_real_article)}

    def mode(self):
        """ Returns the mode number of authors per article, the mode number of authors per fake 
            article, and the mode number of authors per real article.

        Returns:
            `dict`: A dictionary containing the mode values outlined above.
        """

        return {"mode-authors-per-article": statistics.mode(self.authors_per_article),
                "mode-authors-per-fake-article": statistics.mode(self.authors_per_fake_article),
                "mode-authors-per-real-article": statistics.mode(self.authors_per_real_article)}

    def stdev(self):
        """ Returns the variance of the number of authors per article, the variance of the number of 
            authors per fake article, and the variance of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the variance values outlined above.
        """

        return {"stdev-authors-per-article": statistics.stdev(
            self.authors_per_article
        ),
            "stdev-authors-per-fake-article": statistics.stdev(
            self.authors_per_fake_article
        ),
            "stdev-authors-per-real-article": statistics.stdev(
                self.authors_per_real_article
        )}

    def range(self):
        """ Returns the range of the number of authors per article, the range of the number of 
            authors per fake article, and the range of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the range values outlined above.
        """

        return {
            "range-authors-per-article":
                max(self.authors_per_article) -
                min(self.authors_per_article),
                "range-authors-per-fake-article":
                    max(self.authors_per_fake_article) -
            min(self.authors_per_fake_article),
                "range-authors-per-real-article":
                    max(self.authors_per_real_article) -
                    min(self.authors_per_real_article)
        }

    def iqr(self):
        """ Returns the interquartile range of the number of authors per article, the interquartile 
            range of the number of authors per fake article, and the interquartile range of the 
            number of authors per real article.

        Returns:
            `dict`: A dictionary containing the interquartile range values outlined above.
        """

        return {
            "iqr-authors-per-article":
                statistics.quantiles(self.authors_per_article, n=4)[2] -
                statistics.quantiles(self.authors_per_article, n=4)[0],
            "iqr-authors-per-fake-article":
                statistics.quantiles(self.authors_per_fake_article, n=4)[2] -
                statistics.quantiles(self.authors_per_fake_article, n=4)[0],
            "iqr-authors-per-real-article":
                statistics.quantiles(self.authors_per_real_article, n=4)[2] -
                statistics.quantiles(self.authors_per_real_article, n=4)[0]
        }

    def skew(self):
        """ Returns the skewness of the number of authors per article, the skewness of the number of 
            authors per fake article, and the skewness of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the skewness values outlined above.
        """

        return {
            "skew-authors-per-article": stats.skew(self.authors_per_article),
            "skew-authors-per-fake-article": stats.skew(self.authors_per_fake_article),
            "skew-authors-per-real-article": stats.skew(self.authors_per_real_article)
        }

    def kurtosis(self):
        """ Returns the kurtosis of the number of authors per article, the kurtosis of the number of 
            authors per fake article, and the kurtosis of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the kurtosis values outlined above.
        """

        return {
            "kurtosis-authors-per-article": stats.kurtosis(self.authors_per_article),
            "kurtosis-authors-per-fake-article": stats.kurtosis(self.authors_per_fake_article),
            "kurtosis-authors-per-real-article": stats.kurtosis(self.authors_per_real_article)
        }
