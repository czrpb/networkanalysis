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

|The *degree* of a node is the number of connected edges|The most basic centrality statistics is called *degree centrality*|
|---|---|
|$$d(i) = \text{number of edges connected to node} \ i$$|$$C^{D}_{i} = \frac {d(i)} {n-1} $$|
|<img src="https://github.com/czrpb/networkanalysis/blob/main/learning/na101-basics/net-basic-001-degrees.png" />|<img src="https://github.com/czrpb/networkanalysis/blob/main/learning/na101-basics/net-basic-001-degree_centrality.png" />|


##### Some More Examples

Here are more networks, which will be used in later measures also as the above network is pretty simple.

|Star|Clique|Bridge|Complete|
|---|---|---|---|
|![Basic001](net-ego-abcd-degrees.png)|![Basic002](net-ego-abcd-ab-degrees.png)|![Basic003](net-ego-abcd-ab-cd-degrees.png)|![Basic004](net-ego-abcd-complete-degrees.png)|

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
