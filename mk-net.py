import sys
import networkx as nx
import matplotlib.pyplot as plt

def sum_of_weighted_paths_by_node(g, decay=1):
  sums = {}
  nodes = list(g)
  for i in nodes:
    i_sum = 0
    nodes_without_i = nodes.copy()
    nodes_without_i.remove(i)
    for j in nodes_without_i:
      i_sum += decay ** (len(list(nx.shortest_simple_paths(g, i, j))[0])-1)
    sums[i] = i_sum / (decay * (len(nodes)-1))
  return sums

nx.decay_centrality = lambda g, decay=0.5: sum_of_weighted_paths_by_node(g, decay)

c_func = []

def mk_pairs(l):
  #print(l)
  match l:
    case [(_, _), *_]:
      pass
    case [centrality, *_] if centrality.startswith("--"):
      c_func.append(getattr(nx, f"{centrality[2:]}"))
      l.pop(0)
      mk_pairs(l)
    case _:
      l.append((l.pop(0), l.pop(0)))
      mk_pairs(l)

edges = sys.argv[1:]

mk_pairs(edges)

g = nx.Graph()
g.add_edges_from(edges)

if c_func:
    centralities = c_func[0](g)
    g = nx.relabel_nodes(g, dict([(n, f"{n}\n{centralities[n]:.2f}") for n in g]))

plt.subplots(figsize=(3, 3))
nx.draw_networkx(g)
plt.show()