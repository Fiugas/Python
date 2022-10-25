import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(0,8))
G.add_edges_from([(1,2),(2,3),(3,4),(3,5),(3,6),(4,5),(5,6)])
fig,ax = plt.subplots()
layout = nx.shell_layout(G)
nx.draw(G,ax = ax, pos = layout, with_labels = True)
for i in [0,2,7]:
    degree = G.degree[i]
    print(f"Degree of {i}:{degree}")

print(list(nx.connected_components(G)))
print(nx.density(G))
is_planar,_ = nx.check_planarity(G)
print("Is Planar", is_planar)
print(nx.adjacency_matrix(G))
print(nx.adjacency_matrix(G).todense())
print() 
ax.set_title("seimple network drawing")
plt.show()


G = nx.Graph()
G.add_nodes_from(["A","B","C","D","F"])
G.add_edges_from([("A","B"),("C","D")])
print(nx.info(G))

