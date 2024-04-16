"""


    Author: Daniel Markusson


"""


from rich.console import Console
from rich.table import Table
from definitions import THEME
from get_json_dict import DATABASE

CONSOLE = Console(theme=THEME)


def display_counts_table():
    """ Generates a table with counts of unique authors, fake articles, real articles, unique 
        articles and unique users.
    """
    table = Table(title="Counts")

    table.add_column("Number of Unique Authors",
                     justify="center", style="cyan")
    table.add_column("Number of Fake Articles",
                     justify="center", style="magenta")
    table.add_column("Number of Real Articles",
                     justify="center", style="magenta")
    table.add_column("Number of Unique Articles",
                     justify="center", style="green")
    table.add_column("Number of Unique Users", justify="center", style="green")

    table.add_row()

    CONSOLE.print(table)


def get_num_authors():
    ...


def main():
    """ Function to be ran when the file is executed.
    """
    display_counts_table()


if __name__ == "__main__":
    main()
