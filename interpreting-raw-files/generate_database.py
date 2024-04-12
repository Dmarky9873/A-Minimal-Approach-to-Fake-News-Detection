"""
    Author: Daniel Markusson

    Summary:
                
"""
import simplejson as json
from counts import USER_COUNTS, ARTICLE_COUNTS
from summary_statistics import get_articles_summary_statistics, get_user_summary_statistics
from file_retrieval import get_json_location
from articles import ARTICLES_DATAFRAME
from rich.console import Console
from pathvalidate import ValidationError, validate_filename
from definitions import THEME, LOGO


console = Console(theme=THEME)


def update_json(output_file: str):
    """Updates the JSON "database" with the information from the raw files.

    Args:
        verbose (bool, optional): Set `True` for more information during method call. Defaults to
        False.
    """
    json_location = get_json_location(output_file)

    data = dict()

    data["articles"] = {
        "fake-articles": dict(), "real-articles": dict(),
        "counts": ARTICLE_COUNTS,
        "statistics": get_articles_summary_statistics()
    }

    data["articles"]["fake-articles"] = ARTICLES_DATAFRAME["fake"].to_dict()
    data["articles"]["real-articles"] = ARTICLES_DATAFRAME["real"].to_dict()

    data["users"] = {"counts": USER_COUNTS,
                     "statistics": get_user_summary_statistics()}

    with open(json_location, 'w', encoding="UTF-8") as f:
        json.dump(data, f)


def main():
    """Main method to be run if this file is ran.
    """
    # os.system("clear")
    console.print(LOGO, style="bright_white")
    console.print("[bold]Analyzing the Spread of Online Media (AweSOMe)[/bold]\n\n",
                  style="bright_white")

    console.print(
        "Please enter the name of the output file: \n\n", style="info")
    name = input()
    try:
        validate_filename(name, platform='auto')

    except ValidationError as e:
        console.print(f"The filename is invalid!\nError: {e}", style="alert")
    else:
        update_json(name)


if __name__ == '__main__':
    main()
