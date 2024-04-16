"""

    Author: Daniel Markusson


"""

import os
import sys
from rich.console import Console
from definitions import RAW_FILES_DIR, THEME, ROOT_DIR

console = Console(theme=THEME)


def get_raw_file_location(file: str):
    """ Retrieves the location of `file`.

    Returns:
        `str`: The path that leads to the location of `file`.
    """

    path = os.path.join(RAW_FILES_DIR, file)
    if os.path.exists(path):
        console.print(
            f"[file]{file}[/file] loaded from [file]{path}[/file]", style="success")
        return path
    elif os.path.exists(RAW_FILES_DIR):
        console.print(
            f"[file]{file}[/file] not found.",
            style="alert"
        )
        raise FileNotFoundError
    else:
        console.print(
            "[alert]raw-files[/alert] directory not found.",
            style="alert"
        )
        raise FileNotFoundError


def get_json_location(file: str):
    """
        TODO: Document
    """
    if ".json" not in file:
        file = str(file) + ".json"

    path = os.path.join(ROOT_DIR, file)

    if os.path.exists(path):
        console.print(f"""It seems that a JSON file named [file]{
                      file}[/file] already exists. Are you fine with this being overwritten?""",
                      style="warn"
                      )
        console.print(
            "(yes or no)\n[bold]y[/bold]: continue\n[bold]n[/bold]: quit", style="info")
        response = input()
        while True:
            if response.lower() == 'y':
                console.print("Continuing...", style="info")
                return path

            if response.lower() == 'n':
                console.print(f"""Aborting...please remove [file]{
                    file}[/file] from [file]{
                        ROOT_DIR}[/file] to prevent it from being overwritten.""",
                    style="warn")
                sys.exit()

            console.print(
                f"Response of {response} is not y or n.", style="warn")
            console.print(
                "(yes or no)\n[bold]y[/bold]: continue\n[bold]n[/bold]: quit", style="info")

            response = input()

    return path


def main():
    """
        Main function to be run when current file is ran.
    """
    get_raw_file_location("BuzzFeed_fake_news_content.csv")


if __name__ == "__main__":
    main()
