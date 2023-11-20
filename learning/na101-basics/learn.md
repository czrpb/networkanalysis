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

<table>
  <tr>
    <td><img src="network-centralities.png" alt="Common Centrality Measures" width="576"/></td>
    <td>
    <p>The basic analytic statistics on networks are measures that have their focus on nodes and their "importance" in the network.</p>
    <br>
    <p>The technical term for this is called <i>centrality</i> and thus these are <i>centrality measures</i>.</p>
    <br>
<p><a href="https://en.wikipedia.org/wiki/Centrality">https://en.wikipedia.org/wiki/Centrality</a></p>
    </td>
  </tr>
</table>

#### Degree

The *degree* of a node are the number of connected edges:

$$d\(i\) = \text{number of edges connected to node} \ i$$

![Degrees](net-basic-001-degrees.png)

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
