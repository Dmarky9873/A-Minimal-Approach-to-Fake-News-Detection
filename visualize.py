import matplotlib.pyplot as plt
import networkx as nx
import json

with open("./cleaned_data.json") as f:
    DATABASE = json.load(f)


def createFollowersNetworkGraph():
    graph = nx.Graph()
    graph.add_node(1)
    graph.add_node(2)

    nx.draw(graph)

    plt.show()


def main():
    createFollowersNetworkGraph()


if __name__ == "__main__":
    main()
