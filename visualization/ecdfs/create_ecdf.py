"""

    Author: Daniel Markusson


"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from visualization.directory_finder import get_file_to_export_path


def create_single_ecdf(points: list[int], data_label: str, title: str, file_name: str):
    """ Provided with a list of datapoints, `points`, this function will create an ECDF plot with 
        those datapoints.

    Args:
        points (list[int]): The points to be plotted on the ECDF.
        data_label (str): The label for the data on the final plot.
        title (str): The title of the plot.
        file_name (str): The name of the file to be saved.
    """
    sns.set_theme()
    data = pd.DataFrame(points, columns=[data_label])

    sns.ecdfplot(
        data=data,
        x=data_label,
    ).set(title=title)

    plt.savefig(get_file_to_export_path(file_name, "ecdfs"))


def create_comparitive_ecdf(points_to_plot: list[any], labels: list[str], column_labels: list[str], to_compare: str, to_plot: str, title: str, file_name: str, xlabel=None, log_scale=True):
    """ Provided with a list of datapoints, `points_to_plot`, and labels for each datapoint, 
        `labels`, this function will create an ECDF plot comparing datapoints for each categorical 
        label.

    Args:
        points_to_plot (list[int]): The points to be plotted on the ECDF.
        labels (list[str]): The labels for the data on the final plot.
        column_labels (list[str]): The labels for the columns in the final plot.
        to_compare (str): The column to compare the data on.
        to_plot (str): The column to plot the data on.
        title (str): The title of the plot.
        file_name (str): The name of the file to be saved.
    """
    if xlabel is None:
        xlabel = to_plot

    sns.set_theme(rc={
        'figure.figsize': (6.5, 6.5)
    })

    cleaned_data = []
    for point, label in zip(points_to_plot, labels):
        cleaned_data.append((point, label))

    data = pd.DataFrame(cleaned_data, columns=column_labels)

    if log_scale:
        sns.ecdfplot(
            data=data,
            x=to_plot,
            hue=to_compare,
            log_scale=True,
            hue_order=["Fake", "Real"],
        ).set(title=title, ylabel="ECDF", xlabel=xlabel)
    else:
        sns.ecdfplot(
            data=data,
            x=to_plot,
            hue=to_compare,
            hue_order=["Fake", "Real"],
        ).set(title=title, ylabel="ECDF", xlabel=xlabel)

    plt.savefig(get_file_to_export_path(file_name, "ecdfs"))


def main():
    """ Main function for testing the ecdf functions"""

    create_comparitive_ecdf([1, 1, 2, 3, 2], ['fake', 'fake', 'fake', 'real', 'real'], [
                            'num_authors', 'is_fake_real'], 'is_fake_real', 'num_authors', "Hello",
                            'hello.png', True, "hello")


if __name__ == '__main__':
    main()
