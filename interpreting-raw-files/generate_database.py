"""

    Author: Daniel Markusson

"""

import uuid
import os
import simplejson as json
from counts import USER_COUNTS, ARTICLE_COUNTS
from summary_statistics import get_articles_summary_statistics, get_user_summary_statistics
from file_retrieval import get_json_location
from articles import ARTICLES_DICT
from rich.console import Console
from pathvalidate import ValidationError, validate_filename
from definitions import THEME, LOGO


CONSOLE = Console(theme=THEME)


def update_json(output_file: str):
    """ Uses data gathered from the raw files to produce a convenient JSON file with all the 
        information for further use.

    Args:
        output_file (str): The name of the output file.
    """
    json_location = get_json_location(output_file)

    data = dict()

    data["articles"] = {
        "fake-articles": dict(), "real-articles": dict(),
        "counts": ARTICLE_COUNTS,
        "statistics": get_articles_summary_statistics()
    }

    data["articles"]["fake-articles"] = ARTICLES_DICT["fake-articles"]
    data["articles"]["real-articles"] = ARTICLES_DICT["real-articles"]

    data["users"] = {"counts": USER_COUNTS,
                     "statistics": get_user_summary_statistics()}

    with open(json_location, 'w', encoding="UTF-8") as f:
        json.dump(data, f)


def main():
    """Main method to be run if this file is ran.
    """
    os.system("clear")
    CONSOLE.print(LOGO, style="bright_white")
    CONSOLE.print("[bold]Analyzing the Spread of Online Media (AweSOMe)[/bold]\n\n",
                  style="bright_white")

    CONSOLE.print(
        "Please enter the name of the output file: \n\n", style="info")
    name = input()
    try:
        validate_filename(name, platform='auto')

    except ValidationError as e:
        CONSOLE.print(f"The filename is invalid!\nError: {e}", style="alert")
    else:
        update_json(name)


def for_profiling():
    """ Exact same function as the main function but without the console input. This provides a 
        more accurate profile for testing.
    """
    os.system("clear")
    CONSOLE.print(LOGO, style="bright_white")
    CONSOLE.print("[bold]Analyzing the Spread of Online Media (AweSOMe)[/bold]\n\n",
                  style="bright_white")

    CONSOLE.print(
        "Please enter the name of the output file: \n\n", style="info")
    name = uuid.uuid4().hex
    CONSOLE.print(f"""Automatically setting name to [file]{
                  name}[/file] for profiling purposes""", style="info")
    update_json(name)


if __name__ == '__main__':
    main()
