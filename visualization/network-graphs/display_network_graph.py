"""
    
    Author: Daniel Markusson
    
    
"""

import networkx as nx
import matplotlib.pyplot as plt

import matplotlib.colors as matplotlib_colors


def get_colors(graph: nx.Graph):
    """ Gets a colormap for the network graph to be displayed based on the degrees of the nodes.

    Args:
        graph (NetworkX Graph Object): The graph which we are trying to display

    Returns:
        `list`: A list of color values based on the degrees of the nodes.
    """
    degrees = dict(graph.degree())
    max_degree = max(degrees.values())

    # Change this to whatever shades of a color you want the nodes to be.
    color_map = plt.colormaps["coolwarm"]

    normalize = matplotlib_colors.Normalize(0, max_degree)

    colors_for_nodes = [color_map(normalize(degrees[node]))
                        for node in graph.nodes()]

    return colors_for_nodes


def display_network_graph(graph):
    """ Generates a network graph with my specifications (e.g. nodes with higher degrees get warmer 
        colors).

    Args:
        graph (NetworkX Graph Object): The graph which is to be displayed.
    """

    positioning = nx.spring_layout(graph)

    nx.draw_networkx(graph, positioning, with_labels=True, node_size=7000/len(graph.nodes()),
                     node_color=get_colors(graph), font_size=55/len(graph.nodes()))

    plt.show()
