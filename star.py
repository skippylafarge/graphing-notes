import matplotlib.pyplot as plt
import networkx as nx

nodes = [n for n in range(0,5)]
hub_node = 'H'
edges = [(hub_node, n) for n in nodes]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_node(hub_node)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='orange', edge_color='black', font_weight='bold')
plt.show()
