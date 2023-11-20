# Glossary of Network Terms

### Centrality

*Centrality* is a measure of a node's "importance" in the network.

Common measures are:

- Degree
- Closeness
- Betweenness
- Katz or Decay

### Closeness (Centrality)

Closeness centrality measures the distance (or length) from ego to all other nodes.

$$C^{C}_{i} = \frac {n-1} {\sum_{\substack{i, j\\i \not = j}} l(i, j)} $$

$$C^{C}_{i} = \sum_{\substack{i, j\\i \not = j}} l(i, j) $$

### Degree

The number of edges connected to a node.

### Degree Centrality

Degree centrality measures the node's importance on the number of edges it has.

$$C^{D}_{i} = \frac {d(i)} {n-1} $$

### Distance

Distance the count of edges in a path between 2 nodes.

Aliases: *Length*

### Dyad

Two *nodes* connect by an *edge*.

### Edge

An *edge* is the relationship in a *dyad*.

Aliases: *Tie*

### Ego

Ego is often used as the "name" of a node that is under investigation.

### Network

A set of *nodes* connected by *edges*.

Aliases: *Graph*

### Node

A *node* is one of the 2 primitive elements of a *network*.

Nodes are usually "things" or nouns such as:

- People - when part of a social network; other examples include:
  - Plants and animals in an ecosystem
- Computers: when part of a physical network; other examples include:
  - Cities, ports, stores, etc - as part of a transportation, distribution, supply chain
- Webpages - when part of an informational network; other examples include:
  - Academic papers, 

### Path

A path is a set of edges that connect 2 nodes.

### Tie

See *Edge*.