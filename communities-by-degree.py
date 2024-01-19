import sys
import random
import matplotlib.pyplot as plt
import networkx as nx

main = nx.read_gexf(sys.argv[1])

nodes = list(nx.nodes(main))

def get_random_communities():
    ns = list(nodes)
    c1 = ns[:len(ns)//2]
    c2 = ns[len(ns)//2:]
    return c1, c2

community_1, community_2 = get_random_communities()

pos = nx.spring_layout(main)
nx.draw_networkx_nodes(main, pos, nodelist=community_1, node_shape="s", node_color="red")
nx.draw_networkx_nodes(main, pos, nodelist=community_2, node_shape="o")
nx.draw_networkx_edges(main, pos)
nx.draw_networkx_labels(main, pos)

plt.show()