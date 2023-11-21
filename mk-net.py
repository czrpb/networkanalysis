import sys
import networkx as nx
import matplotlib.pyplot as plt

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
print(edges)

g = nx.Graph()
g.add_edges_from(edges)

g = nx.relabel_nodes(g, dict([(n, f"{n}\n{c_func[0](g)[n]:.2f}") for n in g]))

plt.subplots(figsize=(3, 3))
nx.draw_networkx(g)
plt.show()