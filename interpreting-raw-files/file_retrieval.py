"""

    Author: Daniel Markusson


"""

import os
from rt.rich_terminal import RichTerminal

FILE_LOCATIONS_DB_NAME = "file-locations.db"


def get_file_location(file: str):
    """ Retrieves the directory of the raw files to be interpreted by the `get_articles_dataframe`
        function.

    Returns:
        `str`: The path that leads to the location of `file`.
    """

    p = os.path.join(os.getcwd(), os.path.join("raw-files", file))
    if os.path.exists(p):
        return p

    os.chdir("..")
    p = os.path.join(os.getcwd(), os.path.join("raw-files", file))

    if os.path.exists(p):
        return p

    rt = RichTerminal()

    raise FileNotFoundError(rt.get_string_alert(
        f"File: {file} does not exist!"))
