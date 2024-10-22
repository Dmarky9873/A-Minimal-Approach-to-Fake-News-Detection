"""

    Author: Daniel Markusson

"""
from visualization.get_json_dict import DATABASE


def get_author_counts():
    """ Returns the number of authors in the DATABASE, the number of authors who publish both fake
        and real articles, the number of authors who exclusively publish fake articles, and the
        number of authors who exclusively publish real articles.

    Returns:
        `dict`: A dictionary containing values outlined above.
    """

    fake_authors = set()
    real_authors = set()

    for author in DATABASE["articles"]["fake-articles"]["authors"]:
        fake_authors.update(author)
    for author in DATABASE["articles"]["real-articles"]["authors"]:
        real_authors.update(author)

    authors_who_publish_both = fake_authors.intersection(real_authors)
    authors = fake_authors.union(real_authors)
    exclusively_fake_authors = fake_authors.difference(real_authors)
    exclusively_real_authors = real_authors.difference(fake_authors)

    return {"total-authors": len(authors),
            "authors-who-publish-both": len(authors_who_publish_both),
            "exclusively-fake-authors": len(exclusively_fake_authors),
            "exclusively-real-authors": len(exclusively_real_authors)}
