"""

    Author: Daniel Markusson

"""


def get_all_article_ids(database):
    """ Get all article ids from the database.

    Args:
        database (`dict`): The database containing the articles.

    Yields:
        `str`: A unique article id.
    """
    uids = database["articles"]["fake-articles"]["ids"] + \
        database["articles"]["real-articles"]["ids"]

    for uid in uids:
        yield uid


def get_user_distribution(database):
    """ Get the distribution of users in the database.

    Returns:
        `dict`: A dictionary containing the distribution of users.
    """
    all_users = set()
    only_fake_users = set()
    only_real_users = set()

    users = database['users']['counts'].keys()

    for user in users:
        all_users.add(user)
        if (database['users']['counts'][user]['articles']['num-fake-shared'] == 0) and \
                (database['users']['counts'][user]['articles']['num-real-shared'] >= 1):
            only_real_users.add(user)
        elif (database['users']['counts'][user]['articles']['num-real-shared'] == 0) and \
                (database['users']['counts'][user]['articles']['num-fake-shared'] >= 1):
            only_fake_users.add(user)

    return {'all-users': all_users, 'fake-users': only_fake_users, 'real-users': only_real_users}


def get_authors(database):
    """ Returns all authors in the database, authors who publish both fake and real articles,
        authors who exclusively publish fake articles, and authors who exclusively publish real
        articles.

        Returns:
            `dict`: A dictionary containing values outlined above.
        """
    fake_authors = set()
    real_authors = set()

    for author in database["articles"]["fake-articles"]["authors"]:
        fake_authors.update(author)
    for author in database["articles"]["real-articles"]["authors"]:
        real_authors.update(author)

    authors_who_publish_both = fake_authors.intersection(real_authors)
    authors = fake_authors.union(real_authors)
    exclusively_fake_authors = fake_authors.difference(real_authors)
    exclusively_real_authors = real_authors.difference(fake_authors)

    return {"every-author": authors,
            "authors-who-publish-both": authors_who_publish_both,
            "exclusively-fake-authors": exclusively_fake_authors,
            "exclusively-real-authors": exclusively_real_authors}


def is_article_fake(uid: str):
    """Returns `True` if article `name` is fake, and `False` if it is true.

    Args:
        name (`str`): The unique name of an article.

    Returns:
        `bool`: Returns `True` if article `name` is fake, and `False` if it is true.
    """
    if "Fake" in uid:
        return True
    return False
