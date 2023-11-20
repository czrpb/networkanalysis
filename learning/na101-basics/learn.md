# Network Analysis 101: Basics

## Overview


### What is a network?

A network, or graph, are a set of *nodes* and *edges*:

> .

> .

### Networks in the Real World

Networks are everywhere, such as:

- Information, ie: the Web
- Social, ie: Twitter, Facebook
- Biological, ie: Ecosystems, Neuronal, Metabolism

https://www.youtube.com/watch?v=yAtsm5xkb5c

### Uses and Usefulness of Network Analysis


### Basic Network Analysis: Analytic

|||
|---|---|
|<img src="network-centralities.png" alt="Common Centrality Measures" width="512"/>|The basic analytic statistics on networks are measures that have their focus on nodes and their "importance" in the network. The technical term for this is called *centrality* and thus these are *centrality measures*.|

#### Degree

The *degree* of a node are the number of connected edges:

$$d\(i\) = \text{number of edges connected to node} \ i$$

```mermaid
mindmap
  root(("Ego: 3"))
    A
    B
    C
```

The most basic centrality statistics is called *degree centrality*:

$$C^{D}_{i} = \frac {d\(i\)} {n-1} $$

##### Some Examples

```mermaid
mindmap
  root(("1"))
    A
    B
    C
```

<details>
<summary>Closeness</summary>
</details>

<details>
<summary>Betweenness</summary>
</details>


### Basic Network Analysis: Synthetic

The basic synthetic, or wholistic, statistics on networks are measures meant to give information to the overall structure of the network.

- Density

- Clusters






<details>
<summary></summary>
</details>
