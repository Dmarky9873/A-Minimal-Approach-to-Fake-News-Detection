"""_summary_
"""

import json
import networkx as nx
import matplotlib.pyplot as plt

with open("./cleaned_data.json", encoding="UTF-8") as f:
    DATABASE = json.load(f)


def create_network_graph_followers():
    # TODO: Docstring
    graph = nx.Graph()
    graph.add_node(1)
    graph.add_node(2)

    nx.draw(graph)

    plt.show()


def main():
    """Main function; to be ran whenever the file is ran.
    """
    create_network_graph_followers()


if __name__ == "__main__":
    main()
