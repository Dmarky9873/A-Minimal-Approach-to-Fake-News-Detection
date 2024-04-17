"""

    Author: Daniel Markusson


"""
import plotly.graph_objects as go
from directory_finder import get_file_to_export_path
TABLE_THEME = {
    "light_row_color": "#EAEAF1",
    "dark_row_color": "#dedeea",
    "line_color": "white",
    "text_color": "#232235",
    "header_color": "#afaecb",
}


def create_table(file_name: str, table_title: str,
                 independent_vars: list,
                 dependent_vars: list,
                 values: list[list],
                 ):
    """ Creates a table with the given parameters.

    Args:
        table_title (str): The title to be given to the table.
        independent_vars (list): The independent variables (top) of the table.
        dependent_vars (list): The dependent variables (left) of the table.
        values (list[list]): The values to be displayed in the body of table.
    """

    values_list = [add_br_suffix(dependent_vars)]
    for value in values:
        values_list.append(add_br_suffix(value))
    table = go.Figure(data=[go.Table(
        header=dict(
            values=[f"<b>{var}<b>" for var in independent_vars],
            line_color=TABLE_THEME["line_color"],
            fill_color=TABLE_THEME["header_color"],
            align=["center"],
            font=dict(color=TABLE_THEME["text_color"], size=14),
        ),

        cells=dict(
            values=values_list,
            line_color=TABLE_THEME["line_color"],
            fill_color=[[TABLE_THEME["light_row_color"],
                         TABLE_THEME["dark_row_color"]]*len(dependent_vars)],
            align=["center"],
            font=dict(color=TABLE_THEME["text_color"], size=14),

        ))
    ])

    table.update_layout(title={
        'text': f"<b>{table_title}<b>",
        'y': 0.8,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=20, color=TABLE_THEME["text_color"])})

    if '.' not in file_name:
        file_name += ".png"
    table.write_image(get_file_to_export_path(file_name, "table"),
                      scale=2, width=750, height=385)


def add_br_suffix(value: any):
    """ Adds an HTML line break `<br>` to the end of `value`. If `value` is a list, a line break 
        is added to each element.

    Args:
        `value` (any):  The `value` to add a line break to. If `value` is a list, the line break is 
                        added to each element.

    Returns:
        `str`:  `value` with a line break `<br>` at the end. If `value` is a list, a line break is 
                added to the end of each element.
    """
    if isinstance(value, list):
        for index, v in enumerate(value):
            value[index] = f"{v}<br>"
        return value
    return f"{value}<br>"


def main():
    """ Main method to be run if this file is ran.
    """
    create_table("ex", "Analyzing", ["EXPENSES", "Q1", "Q2", "Q3", "Q4"], [
                 "Salaries", "Office", "Merchandise", "Legal", "TOTAL"],
                 [[120000, 20000, 80000, 2000, 12120000],
                 [1300000, 20000, 70000, 2000, 130902000],
                 [1300000, 20000, 120000, 2000, 131222000],
                 [1400000, 20000, 90000, 2000, 14102000]])


if __name__ == "__main__":
    main()
