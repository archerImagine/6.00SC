# MIT 6.00SC | Recitation 09 | Directed and Undirected Node Graphs #

## Graphs ##

Graphs is a formalization, which denotes a pair of vertices and edges.

````
G = (V, E) # V = set vertex, E = set of edges
V = {v1, v2, v3} # vertex are set of points.
E = {(v1, v2), (v2, v3)} # Edges are set of tuple showing relation between vertex
````

Vertices are also called Nodes.
Edges are also called arcs.

What are the types of Graph.

* Directed Graph
    - In a Directed Graph, we can traverse only in the direction of the edges, represented by a arrow on the edges.
* UnDirected Graph
    - In UnDirected Graph, we can go on either direction of the edges.
* Weighted Graph
    - In Weighted Graph, It attaches weight to the edges, denoting some extra relation between the nodes.

The most important question while dealing with graphs are, To find shortest path between two nodes. We have Two algorithms to solve this problem.

* Depth First.
* Breadth First.

## Depth First ##

This is same as the lecture 22 explanation of Depth First.

## Breadth First ##

As per [WikiPedia](http://en.wikipedia.org/wiki/Breadth-first_search), a Breadth First search 

> Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a `search key'[1]) and explores the neighbor nodes first, before moving to the next level neighbors. Compare BFS with the equivalent, but more memory-efficient Iterative deepening depth-first search and contrast with depth-first search.

### Lambda Function ###





