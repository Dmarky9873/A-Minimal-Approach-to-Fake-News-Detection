"""

    Author: Daniel Markusson


"""

import statistics
from scipy import stats
from visualization.utils import get_authors


class ArticlesPerAuthorStats:
    """ Contains functions to get statistics about the number of articles per author.

        "Mean", "Median", "Mode",
        "Stdev", "Range", "IQR",
        "Skew", "Kurtosis"
        """

    def __init__(self, database):
        """ Initializes the AuthorsPerArticleStats class.

        Args:
            database (`dict`):  The database containing the articles.
        """
        self.articles_per_author = []
        self.articles_per_fake_author = []
        self.articles_per_real_author = []

        author_types = get_authors(database)
        exclusively_fake_authors = author_types["exclusively-fake-authors"]
        exclusively_real_authors = author_types["exclusively-real-authors"]
        all_authors = author_types["every-author"]

        article_counts = dict()

        for author in all_authors:
            article_counts[author] = 0

        for fake_authors, real_authors in zip(database["articles"]["fake-articles"]["authors"],
                                              database["articles"]["real-articles"]["authors"]):
            for fake_author in fake_authors:
                article_counts[fake_author] += 1
            for real_author in real_authors:
                article_counts[real_author] += 1

        for author in all_authors:
            self.articles_per_author.append(article_counts[author])

            if author in exclusively_fake_authors:
                self.articles_per_fake_author.append(article_counts[author])

            if author in exclusively_real_authors:
                self.articles_per_real_author.append(article_counts[author])

    def mean(self):
        """ Returns the average number of authors per article, the average number of authors per
            fake article, and the average number of authors per real article.

        Returns:
            `dict`: A dictionary containing the mean values outlined above.
        """
        print(self.articles_per_real_author)
        return {"mean-articles-per-author": statistics.mean(self.articles_per_author),
                "mean-articles-per-fake-author": statistics.mean(self.articles_per_fake_author),
                "mean-articles-per-real-author": statistics.mean(self.articles_per_real_author)}

    def median(self):
        """ Returns the median number of authors per article, the median number of authors per fake
            article, and the median number of authors per real article.

        Returns:
            `dict`: A dictionary containing the median values outlined above.
        """

        return {"median-articles-per-author": statistics.median(self.articles_per_author),
                "median-articles-per-fake-author": statistics.median(self.articles_per_fake_author),
                "median-articles-per-real-author": statistics.median(self.articles_per_real_author)}

    def mode(self):
        """ Returns the mode number of authors per article, the mode number of authors per fake
            article, and the mode number of authors per real article.

        Returns:
            `dict`: A dictionary containing the mode values outlined above.
        """

        return {"mode-articles-per-author": statistics.mode(self.articles_per_author),
                "mode-articles-per-fake-author": statistics.mode(self.articles_per_fake_author),
                "mode-articles-per-real-author": statistics.mode(self.articles_per_real_author)}

    def stdev(self):
        """ Returns the variance of the number of authors per article, the variance of the number of
            authors per fake article, and the variance of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the variance values outlined above.
        """

        return {"stdev-articles-per-author": statistics.stdev(
            self.articles_per_author
        ),
            "stdev-articles-per-fake-author": statistics.stdev(
            self.articles_per_fake_author
        ),
            "stdev-articles-per-real-author": statistics.stdev(
                self.articles_per_real_author
        )}

    def range(self):
        """ Returns the range of the number of authors per article, the range of the number of
            authors per fake article, and the range of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the range values outlined above.
        """

        return {
            "range-articles-per-author":
                max(self.articles_per_author) -
                min(self.articles_per_author),
                "range-articles-per-fake-author":
                    max(self.articles_per_fake_author) -
            min(self.articles_per_fake_author),
                "range-articles-per-real-author":
                    max(self.articles_per_real_author) -
                    min(self.articles_per_real_author)
        }

    def iqr(self):
        """ Returns the interquartile range of the number of authors per article, the interquartile
            range of the number of authors per fake article, and the interquartile range of the
            number of authors per real article.

        Returns:
            `dict`: A dictionary containing the interquartile range values outlined above.
        """

        return {
            "iqr-articles-per-author":
                statistics.quantiles(self.articles_per_author, n=4)[2] -
                statistics.quantiles(self.articles_per_author, n=4)[0],
            "iqr-articles-per-fake-author":
                statistics.quantiles(self.articles_per_fake_author, n=4)[2] -
                statistics.quantiles(self.articles_per_fake_author, n=4)[0],
            "iqr-articles-per-real-author":
                statistics.quantiles(self.articles_per_real_author, n=4)[2] -
                statistics.quantiles(self.articles_per_real_author, n=4)[0]
        }

    def skew(self):
        """ Returns the skewness of the number of authors per article, the skewness of the number of
            authors per fake article, and the skewness of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the skewness values outlined above.
        """

        return {
            "skew-articles-per-author": stats.skew(self.articles_per_author),
            "skew-articles-per-fake-author": stats.skew(self.articles_per_fake_author),
            "skew-articles-per-real-author": stats.skew(self.articles_per_real_author)
        }

    def kurtosis(self):
        """ Returns the kurtosis of the number of authors per article, the kurtosis of the number of
            authors per fake article, and the kurtosis of the number of authors per real article.

        Returns:
            `dict`: A dictionary containing the kurtosis values outlined above.
        """

        return {
            "kurtosis-articles-per-author": stats.kurtosis(self.articles_per_author),
            "kurtosis-articles-per-fake-author": stats.kurtosis(self.articles_per_fake_author),
            "kurtosis-articles-per-real-author": stats.kurtosis(self.articles_per_real_author)
        }
