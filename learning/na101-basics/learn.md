---
marp: true
size: 16:9
theme: uncover
class: invert
math: katex
style: |
  section {
    font-size: 20pt;
  }
---

# Network Analysis 101: Basics

Quentin Crain

---

## Agenda

Networks

- by way of Example and Discussion
- in the Real World
- defined
- deconstructed
  - Centrality
- synthesized
  - Density
  - 


---

### Objectives

- Selfish: I love network science!
  - Practicing the Feynman method
- Educative: Want to spread the knowledge!
- Preferential: What sorts of presentations do people want?
  - "Academic" vs "Project"
  - "Informational" vs "Interactive"

---

### Let's Talk about this Network

![1st Network](../../images/net-centralities-blank.png)

|Most Important?|1|2|3|
|--:|---|---|---|

---

### Let's Talk about this Network

![1st Network with Centralities](../../images/net-centralities.png)

|"Centrality"|1|2|3|
|--:|---|---|---|
|Degree|**0.44**|0.19|0.25|
|Closeness|0.42|**0.46**|0.44|
|Betweenness|0.62|0.59|**0.65**|

---

### What is a network?

<table>
  <tr>
    <td><img alt="10x13 Random" src="../../images/net-10x13-random.png"/></td>
    <td>A <i>network</i> is a set of <i>nodes</i> and <i>edges</i> that connect them.
    <br/><br/>
    <i>Network Analysis</i> is the study of the *structure* of the network.</td>
    <td><img alt="10x13 Random with Centralities" src="../../images/net-10x13-random-withcentralities.png" height="256"/></td>
  </tr>
</table>

<table>
  <tr>
    <td colspan="2">
      https://en.wikipedia.org/wiki/Network_science
      <br/>
      <a href="ref/2003-TheStructureAndFunctionOfComplexNetworks-Newman.pdf">The Structure and Function of Complex Networks</a>
    </td>
  </tr>
  <tr>
    <td><img src="../../images/stanford-cs102-network-basicdef.png" width="512" /></td>
    <td><img src="../../images/stanfor-cs224w-componentsofanetwork.png" width="512" /></td>
  </tr>
</table>

---

### Networks in the Real World

<table>
  <tr><th colspan="3">Networks Everywhere</th>
  </tr>
  <tr>
    <td><u>Technological</u><br/>The Internet</td>
    <td><u>Biological</u><br/>Organisms/Metabolic</td>
    <td><u>Social</u><br/>Florentine families</td>
  </tr>
  <tr>
    <td><img src="../../images/net-opte-2010-internetnetwork.png" width="384" alt="The Internet in 2010 from opte.org"/></td>
    <td><img src="../../images/net-example-biologicalnetwork.png" width="384" alt="Example of Biological Network"/></td>
    <td><img src="../../images/net-example-socialnetwork.png" width="384" alt="Florentine family connections"/></td>
  </tr>
</table>

https://www.youtube.com/watch?v=yAtsm5xkb5c

---

## Basic Network Analysis: Analytic

### Centrality

<table>
  <tr>
    <td><img src="../../images/network-centralities.png" alt="Common Centrality Measures" height="512"/></td>
    <td>
    <p>The basic analytic statistics on networks are measures that have their focus on nodes and their "importance" in the network.</p>
    <br>
    <p>The technical term for this is called <a href="https://github.com/czrpb/networkanalysis/blob/main/glossary.md#centrality">centrality</a> and thus these are <i>centrality measures</i>.</p>
    <br>
    <p><a href="https://en.wikipedia.org/wiki/Centrality">https://en.wikipedia.org/wiki/Centrality</a></p>
    <br>
    <p><a href="https://www.youtube.com/watch?v=NgUj8DEH5Tc">https://www.youtube.com/watch?v=NgUj8DEH5Tc</a></p>
    </td>
  </tr>
</table>

---

### Degree Centrality

|The *degree* of a node is the number of connected edges|The most basic centrality statistics is called *degree centrality*|
|:-:|:-:|
|$d(i) = \text{number of edges connected to node} \ i$|$C^{D}_{i} = \frac {d(i)} {n-1}$|
|<img src="../../images/net-basic-001-degrees.png" />|<img src="../../images/net-basic-001-degree_centrality.png" />|

A related wholistic measure is [density]().

---

#### Degree Centrality: More Examples

Here are more networks, which will be used in later measures also as the above network is pretty simple.

||Star|Clique|Bridge|Complete|
|---|---|---|---|---|
|Degree|<img src="../../images/net-ego-abcd-degrees.png" alt="Basic001" width="196"/>|<img src="../../images/net-ego-abcd-ab-degrees.png" alt="Basic002" width="196"/>|<img alt="Basic003" src="../../images/net-ego-abcd-ab-cd-degrees.png" width="196"/>|<img alt="Basic004" src="../../images/net-ego-abcd-complete-degrees.png" width="196"/>|
|Degree Centrality|<img alt="Basic010" src="../../images/net-ego-abcd-degree_centrality.png" width="196" />|<img alt="Basic020" src="../../images/net-ego-abcd-ab-degree_centrality.png"  width="196"/>|<img alt="Basic030" src="../../images/net-ego-abcd-ab-cd-degree_centrality.png" width="196"/>|<img alt="Basic040" src="../../images/net-ego-abcd-complete-degree_centrality.png" width="196"/>|

---

#### Closeness

[Closeness](https://github.com/czrpb/networkanalysis/blob/main/glossary.md#closeness-centrality) is a measure that means to capture a notion of proximity of a node to all other nodes.

So, if *ego* is 1 step away from all other nodes (ie: the center in a star network) the sum would be $n - 1$. Since generally we want measures $0 \leq c \leq 1$, let us consider this to be the maximum of $1$ and thus closeness would be defined as:

$$
Cent^{C}_{i} = \frac {n-1} {\sum l(i, j)}
$$


|$n-1$|$\sum l(i, j)$||
|:-:|:-:|:-:|
|3|3|<img src="../../images/net-basic-001-closeness_centrality.png" />|

##### More Examples

||Star|Clique|Bridge|Complete|
|---|---|---|---|---|
|Closeness Centrality|![Basic011](../../images/net-ego-abcd-closeness_centrality.png)|![Basic021](../../images/net-ego-abcd-ab-closeness_centrality.png)|![Basic031](../../images/net-ego-abcd-ab-cd-closeness_centrality.png)|![Basic041](../../images/net-ego-abcd-complete-closeness_centrality.png)|

##### References

https://www.youtube.com/watch?v=89mxOdwPfxA&t=810

---

#### Decay

##### More Examples

||Star|Clique|Bridge|Complete|
|---|---|---|---|---|
|Decay Centrality|![Basic011](../../images/net-ego-abcd-decay_centrality.png)|![Basic021](../../images/net-ego-abcd-ab-decay_centrality.png)|![Basic031](../../images/net-ego-abcd-ab-cd-decay_centrality.png)|![Basic041](../../images/net-ego-abcd-complete-decay_centrality.png)|

---

#### Betweenness

.

---

## Basic Network Analysis: Synthetic

The basic synthetic, or wholistic, statistics on networks are measures meant to give information to the overall structure of the network.

---

### Density

.

---

### Clusters

.

---

### References

- Stanford CS102 class slide
  - https://web.stanford.edu/class/cs102/lectureslides/NetworksSlides.pdf
- Stanford CS224W class slides
  - https://web.stanford.edu/class/cs102/readings/CS224W-intro.pdf
- "Map" of the Internet from opte.org
  - http://content.opte.org/content/opte/maps/static/opte-2010.png
- Florentine families
  - https://journals.plos.org/plosone/article/figure?id=10.1371/journal.pone.0233276.g005
- Biological network image
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4833320/

---