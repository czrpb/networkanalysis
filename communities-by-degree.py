import matplotlib.pyplot as plt

import networkx as nx

kc = nx.karate_club_graph()

nodes_by_degree = list(reversed(sorted(list((d,n) for n,d in kc.degree()))))
print(nodes_by_degree)

#g_copy = nx.Graph(g)

communities = {}

for d, n in nodes_by_degree:
    n_neighbors = set(nx.neighbors(kc, n))
    communities[n] = [d, n_neighbors]

print(communities)

#countdown = 30
# algo: starting w/ nodes with smallest degree, add them to the largest degreed node they connect to
while nodes_by_degree:
    #countdown -= 1
    d, n = nodes_by_degree.pop()
    n_neighbors = communities[n][1]
    print(n, n_neighbors)

    # find neighbor w/ the most neighbors
    while n_neighbors:
        n_neighbor_with_largest_neighbors = n_neighbors.pop()
        print(f"\t{n_neighbor_with_largest_neighbors}")
        if n_neighbor_with_largest_neighbors not in communities:
            continue

        while n_neighbors:
            n_neighbor_possibly_largest = n_neighbors.pop()
            if n_neighbor_possibly_largest not in communities:
                continue

            if (len(communities[n_neighbor_with_largest_neighbors][1]) <
                len(communities[n_neighbor_possibly_largest][1])):
                n_neighbor_with_largest_neighbors = n_neighbor_possibly_largest

    print(n, n_neighbor_with_largest_neighbors)

    # add n as a neighbor to largest
    if (len(communities[n_neighbor_with_largest_neighbors][1]) > len(communities[n][1])):
        communities[n_neighbor_with_largest_neighbors][1].add(n)
        del communities[n]

    #1/countdown
    if len(communities) == 2:
        break

print(communities)

k1, k2 = communities.keys()
print(k1)
print(k2)

communities[k2][1] = communities[k2][1] - communities[k1][1]

print(communities)

el = [[k1, _] for _ in communities[k1][1]]
print(el)
el += [[k2, _] for _ in communities[k2][1]]
print(el)

g = nx.Graph(el)
print(sorted(kc.nodes))
print(sorted(g.nodes))

nx.draw_networkx(g)
plt.show()

pos = nx.spring_layout(kc)
nx.draw_networkx_nodes(kc, pos, nodelist=[k1]+list(communities[k1][1]), node_shape="s")
nx.draw_networkx_nodes(kc, pos, label=k2, nodelist=[k2]+list(communities[k2][1]), node_shape="o")
nx.draw_networkx_edges(kc, pos)
nx.draw_networkx_labels(kc, pos)

print(list(nx.neighbors(kc, 8)))

plt.show()