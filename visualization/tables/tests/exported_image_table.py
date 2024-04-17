"""

    Source: https://plotly.com/python/table/#table-with-alternating-row-colors

"""


import plotly.graph_objects as go

HEADER_COLOR = 'grey'
ROW_EVEN_COLOR = 'lightgrey'
ROW_ODD_COLOR = 'white'

x = []

fig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>EXPENSES</b>', '<b>Q1</b>',
                '<b>Q2</b>', '<b>Q3</b>', '<b>Q4</b>'],
        line_color='#7490C0',
        fill_color="#7490C0",
        align=['left', 'center'],
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[
            ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
            [1200000, 20000, 80000, 2000, 12120000],
            [1300000, 20000, 70000, 2000, 130902000],
            [1300000, 20000, 120000, 2000, 131222000],
            [1400000, 20000, 90000, 2000, 14102000]
        ],
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color=[[ROW_ODD_COLOR, ROW_EVEN_COLOR,
                     ROW_ODD_COLOR, ROW_EVEN_COLOR, ROW_ODD_COLOR]*5],
        align=['left', 'center'],
        font=dict(color='darkslategray', size=11)
    ))
])

fig.update_layout(title="Hello")

fig.write_image("exported_image_table.png", scale=2, width=1000, height=500)
