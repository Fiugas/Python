import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from(["A","B","C","D","E","F"])
G.add_weighted_edges_from([("A","B",4),("A","C",2),("B","C",5),("B","D",10),("C","E",3),("D","F",11),("E","D",4)])
fig, ax = plt.subplots()
pos = nx.shell_layout(G)
nx.draw(G, ax = ax, pos = pos, with_labels = True)
ax.set_title("Weighted, directed network")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)
print(nx.shortest_path(G, source="A",target="F",weight= "weight"))
plt.show()