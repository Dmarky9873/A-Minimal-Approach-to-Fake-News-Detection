"""

    Author: Daniel Markusson


"""


import os
import sys
from rich.console import Console
from definitions import ROOT_DIR, THEME


CONSOLE = Console(theme=THEME)


def __get_tables_directory():
    """ Returns the path to the tables directory.

    Returns:
        str: The path to the tables directory.
    """
    location = os.path.join(ROOT_DIR, "visualization", "exports", "tables")
    if os.path.exists(location):
        return location
    CONSOLE.print(
        f"""The directory [file]graphs[/file] does not exist. Please create it in [file]{
            location}[/file]""", style="alert")
    raise FileNotFoundError


def __get_scatterplots_directory():
    """ Returns the path to the scatterplots directory.

    Returns:
        str: The path to the scatterplots directory.
    """
    location = os.path.join(ROOT_DIR, "visualization",
                            "exports", "scatterplots")
    if os.path.exists(location):
        return location
    CONSOLE.print(
        f"""The directory [file]graphs[/file] does not exist. Please create it in [file]{
            location}[/file]""", style="alert")
    raise FileNotFoundError


def __get_ecdfs_directory():
    """ Returns the path to the scatterplots directory.

    Returns:
        str: The path to the scatterplots directory.
    """
    location = os.path.join(ROOT_DIR, "visualization",
                            "exports", "ecdfs")
    if os.path.exists(location):
        return location
    CONSOLE.print(
        f"""The directory [file]graphs[/file] does not exist. Please create it in [file]{
            location}[/file]""", style="alert")
    raise FileNotFoundError


def __get_histograms_directory():
    """ Returns the path to the scatterplots directory.

    Returns:
        str: The path to the scatterplots directory.
    """
    location = os.path.join(ROOT_DIR, "visualization",
                            "exports", "histograms")
    if os.path.exists(location):
        return location
    CONSOLE.print(
        f"""The directory [file]graphs[/file] does not exist. Please create it in [file]{
            location}[/file]""", style="alert")
    raise FileNotFoundError


TABLES_DIRECTORY = __get_tables_directory()
SCATTERPLOTS_DIRECTORY = __get_scatterplots_directory()
ECDFS_DIRECTORY = __get_ecdfs_directory()
HISTOGRAMS_DIRECTORY = __get_histograms_directory()


def get_file_to_export_path(file_name: str, file_type: str):
    """ Returns the path of the file to be exported.

    Args:
        file_name (str): The name of the file to be exported.
        file_type (str): The type of file to be exported ('graph' or 'table').

    Returns:
        str: The path to the file to be exported.
    """
    match file_type:
        case "table":
            path = os.path.join(TABLES_DIRECTORY, file_name)
        case "scatterplot":
            path = os.path.join(SCATTERPLOTS_DIRECTORY, file_name)
        case "ecdfs":
            path = os.path.join(ECDFS_DIRECTORY, file_name)
        case "histograms":
            path = os.path.join(HISTOGRAMS_DIRECTORY, file_name)
        case _:
            raise ValueError(
                "Invalid arg `file_type`. `file_type` must be 'table', 'ecdfs', 'histograms' or 'scatterplot'.")

    if not '.' in file_name:
        CONSOLE.print(
            "Please provide a file name with an extension.", style="alert")
        raise ValueError
    if os.path.exists(path):
        CONSOLE.print(f"""It seems that a file named [file]{
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
                        os.path.dirname(path)}[/file] to prevent it from being overwritten.""",
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
    print(get_file_to_export_path("test.png", "graph"))


if __name__ == "__main__":
    main()
