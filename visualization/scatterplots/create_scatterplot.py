"""


    Author: Daniel Markusson


"""

import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from visualization.directory_finder import get_file_to_export_path


def create_scatterplot(points: list[tuple[int, int]], x_label: str, y_label: str, title: str,
                       file_name: str, r_and_r2_loc: tuple[int, int] = (0.05, 0.8)):
    """ Creates a scatterplot of `points`.

    Args:
        points (`list[tuple[int, int]]`):   A list of tuples with the x and y values for the 
                                            scatterplot.
        x_label (str):  The label for the x-axis.
        y_label (str):  The label for the y-axis.
    """
    r, r2 = get_r_and_r2(points)

    sns.set_theme()
    data = pd.DataFrame(points, columns=[x_label, y_label])

    sns.scatterplot(
        data=data,
        x=x_label, y=y_label,
    ).set(title=title)

    ax = plt.gca()
    plt.text(r_and_r2_loc[0], r_and_r2_loc[1],
             f"r = {r:0.2f}\nr^2 = {r2:0.2f}", transform=ax.transAxes)

    plt.savefig(get_file_to_export_path(file_name, "scatterplot"))


def get_r_and_r2(points: list[tuple[int, int]]):
    """ Get the r and r^2 values for the points.

    Args:
        points (`list[tuple[int, int]]`):   A list of tuples with the x and y values for the 
                                            scatterplot.

    Returns:
        `tuple[float, float]`:  A tuple with the r and r^2 values.
    """
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    r, _ = sp.stats.pearsonr(x, y)
    r2 = r**2

    return r, r2


def main():
    """ Main function for testing the scatterplot functions.s"""
    create_scatterplot([(2001, 100000), (2002, 100000),
                        (2003, 12103), (2004, 12093128)], 'year', 'income', "Test", "test", (0.05, 0.8))


if __name__ == '__main__':
    main()
