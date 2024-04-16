"""

    Author: Daniel Markusson


"""


import os
import sys
from rich.console import Console
from definitions import ROOT_DIR, THEME


CONSOLE = Console(theme=THEME)


def get_graphs_directory():
    """ Returns the path to the graphs directory.

    Returns:
        str: The path to the graphs directory.
    """
    location = os.path.join(ROOT_DIR, "visualization", "exports", "graphs")
    if os.path.exists(location):
        return location
    CONSOLE.print(
        f"""The directory [file]graphs[/file] does not exist. Please create it in [file]{
            location}[/file]""", style="alert")
    raise FileNotFoundError


GRAPHS_DIRECTORY = get_graphs_directory()


def get_file_to_export_path(file_name: str):
    """ Returns the path of the file to be exported.

    Args:
        file_name(str): The name of the file to be exported.

    Returns:
        str: The path to the file to be exported.
    """
    path = os.path.join(GRAPHS_DIRECTORY, file_name)
    if not '.' in file_name:
        CONSOLE.print(
            "Please provide a file name with an extension.", style="alert")
        raise ValueError
    if os.path.exists(path):
        CONSOLE.print(f"""It seems that a JSON file named [file]{
            file_name}[/file] already exists. Are you fine with this being overwritten?""",
            style="warn"
        )
        CONSOLE.print(
            "(yes or no)\n[bold]y[/bold]: continue\n[bold]n[/bold]: quit", style="info")
        response = input()
        while True:
            if response.lower() == 'y':
                CONSOLE.print("Continuing...", style="info")
                return path

            if response.lower() == 'n':
                CONSOLE.print(f"""Aborting...please remove [file]{
                    file_name}[/file] from [file]{
                        ROOT_DIR}[/file] to prevent it from being overwritten.""",
                    style="warn")
                sys.exit()

            CONSOLE.print(
                f"Response of '{response}' is not y or n.", style="warn")
            CONSOLE.print(
                "(yes or no)\n[bold]y[/bold]: continue\n[bold]n[/bold]: quit", style="info")

            response = input()

    return path


def main():
    """ Main method to be run if this file is ran.
    """
    print(get_file_to_export_path("test.png"))


if __name__ == "__main__":
    main()
