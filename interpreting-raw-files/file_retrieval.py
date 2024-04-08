"""

    Author: Daniel Markusson


"""

import os


def get_file_directory(file: str):
    """ Retrieves the directory of the raw files to be interpreted by the `get_articles_dataframe`
        function.

    Returns:
        `str`: The path that leads to the directory of the raw files.
    """

    p = os.path.join(os.getcwd(), os.path.join("raw-files", file))
    if os.path.exists(p):
        return p

    return os.path.join(os.getcwd(), os.path.join("raw-files", file))
