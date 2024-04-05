"""

    Author: Daniel Markusson

"""

import json
import random as r
import networkx as nx
from display_network_graph import display_network_graph

with open("./cleaned_data.json", encoding="UTF-8") as f:
    DATABASE = json.load(f)


def network_graph_followers():
    # TODO: Docstring
    people = ["Alice", "Bob", "Charlie", "Xavier", "Warren"]
    a_follows_b = set()

    for _ in range(50):
        person1 = r.choices(
            people, [0.8, 0.2/4, 0.2/4, 0.2/4, 0.2/4], k=1)[0]
        person2 = r.choices(
            people, [0.2/4, 0.8, 0.2/4, 0.2/4, 0.2/4], k=1)[0]
        a_follows_b.add((person1, person2))

    followers_network_graph = nx.Graph()
    followers_network_graph.add_nodes_from(people)
    followers_network_graph.add_edges_from(a_follows_b)

    display_network_graph(followers_network_graph)


def main():
    """Main function; to be ran whenever the file is ran.
    """
    network_graph_followers()


if __name__ == "__main__":
    main()
