"""


    Author: Daniel Markusson


"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from visualization.directory_finder import get_file_to_export_path


# class Scatterplot:
#     pass


def create_scatterplot(points: list[tuple[int, int]], x_label: str, y_label: str, title: str, file_name: str):
    """ Creates a scatterplot of `points`.

    Args:
        points (`list[tuple[int, int]]`):   A list of tuples with the x and y values for the 
                                            scatterplot.
        x_label (str):  The label for the x-axis.
        y_label (str):  The label for the y-axis.
    """
    sns.set_theme()
    data = pd.DataFrame(points, columns=[x_label, y_label])

    sns.scatterplot(
        data=data,
        x=x_label, y=y_label,
    ).set(title=title)

    plt.savefig(get_file_to_export_path(file_name, "scatterplot"))


def main():
    """ Main function for testing the scatterplot functions.s"""
    create_scatterplot([(2001, 100000), (2002, 100000),
                        (2003, 12103), (2004, 12093128)], 'year', 'income', "Test", "test")


if __name__ == '__main__':
    main()
