import networkx as nx
from matplotlib import pyplot as plt

G = nx.read_adjlist("My_graph.txt")

my_layout = {
    "1": (3, 15),
    "2": (10, 17),
    "3": (10, 9),
    "4": (4, 5),
    "5": (1, 10),
    "6": (9, 3),
    "7": (17, 5),
    "8": (15, 1),
    "9": (16, 12),
    "10": (18, 18),
    "11": (22, 11)
}

nx.draw(G, pos=my_layout, with_labels=True, node_color="white", edgecolors="black", edge_color="black")
plt.show()

print("Amount of connected components: " + str(nx.number_connected_components(G)))

for component in nx.connected_components(G):
    subgraph = G.subgraph(component)
    print("Nodes: " + str(sorted(list(subgraph.nodes))))
    print("Edges: " + str(list(subgraph.edges)))
    print("Degrees: " + str(dict(subgraph.degree())))
    print("Eccentricities: " + str(dict(nx.eccentricity(subgraph))))
    print("Radius: " + str(nx.radius(subgraph)))
    print("Diameter: " + str(nx.diameter(subgraph)))
    print()


spanning_forest = nx.dfs_tree(G)
f_nodes = spanning_forest.nodes()
f_edges = spanning_forest.edges()
print("List of edges for a spanning forest: " + str(sorted(f_edges)))

edge_colors = []

for v1, v2 in G.edges:
    if (v1, v2) in f_edges:
        edge_colors.append("red")
    elif (v2, v1) in f_edges:
        edge_colors.append("red")
    else:
        edge_colors.append("black")

nx.draw(G, pos=my_layout, with_labels=True, node_color="white", edge_color=edge_colors, edgecolors="black")
plt.show()
