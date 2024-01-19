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

def get_largest_neighbor(n):
    largest_neighbor, *neighbors = list(nx.neighbors(main, n))
    for neighbor in neighbors:
        if nx.degree(main, largest_neighbor) < nx.degree(main, neighbor):
            largest_neighbor = neighbor
    return largest_neighbor

def get_communities():
    communities = dict([(n, list(nx.neighbors(main, n))) for n in nodes])
    print(communities)

    ns = sorted([(nx.degree(main, n), n) for n in nodes])
    print(ns)
    for _, n in ns[:-2]:
        largest_neighbor = get_largest_neighbor(n)
        communities[largest_neighbor].append(n)
        del communities[n]

    print(communities)
    return [[k]+v for k, v in communities.items()]

community_1, community_2 = get_random_communities()

community_1, community_2 = get_communities()

pos = nx.spring_layout(main)
nx.draw_networkx_nodes(main, pos, nodelist=community_1, node_shape="s", node_color="red")
nx.draw_networkx_nodes(main, pos, nodelist=community_2, node_shape="o")
nx.draw_networkx_edges(main, pos)
nx.draw_networkx_labels(main, pos)

plt.show()