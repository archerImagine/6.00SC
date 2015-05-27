# MIT 6.00SC | Lecture 22 | Using Graphs to Model Problems, Part 2 #

## Introduction ##

This section will explain the code of Graph which Started in Lecture 22.

````python
import random

class Node(object):
    """The base class for node"""
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    """docstring for Edge"""
    def __init__(self, src,dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + "->" + str(self.dest)
        
class Digraph(object):
    """docstring for Digraph"""
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self,node):
        if node.getName() in self.nodes:
            raise ValueError('Duplicate Node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self,edge):
        src = edge.getSource()
        dst = edge.getDestination()
        if not(src in self.nodes and dst in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dst)
    def childrenOf(self,node):
        return self.edges[node]
    def hadNode(self,node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self,rev)

def test1(kind):
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    print 'The graph:', type(g)
    print g            

test1(Digraph)
test1(Graph)    
````

So lets examine the code.

* `Node`: This is a starting point, this class does not do anything special other than assigning a name to the `Node`. This can be done by using a string, but in future we may want to store some complex attributes as `Node`, in that case we may be able to extend it.
* `Edge`: This is a little complicated class, it has these attributes.
    - `source` : Source Node
    - `dest` : Destination Node
    - `weight` : Weight on the node, default weight is `0`
    - These 3 attributes help in representing, Graph, DiGraph and also weighted Graph or DiGraph.
    - There are `getter ` methods for all the above property.
* `Digraph `: This has two attributes.
    - `nodes`: This is a set of Nodes in the Graph.
    - `Edges`: A dict of Edges.
    - The various methods in the Class are:-
        + `addNodes(self, node)` : This checks if a `node` is already added or not else it add the node to the set.
        + `addEdge(self, edge)` : This adds the `src` and `dest` nodes as a dict value in the Edge dictionary. It also checks that the nodes are already present in the graph.
        + `childrenOf(self, node)`: Gives all the children of the `node`.
        + `hadNode(self, node)` : returns `true ` or `false ` depending on if the `node` is in the graph.
* `Graph(Digraph)` : The class `Graph ` is a subclass of `Digraph `. Now this is interesting, because common sense tells us `Digraph ` is a sub class of Graph. The reason being, Digraph's are more general than Graphs i.e A Graph is a specialization of a DiGraph.
* We are making a adjacency list to show the edges, as shown in this code:-
    - `self.edges[src].append(dst)` and `self.edges[node] = []`

Some good problems which uses Graph to solve are:-

* [Shortest path problem ](http://en.wikipedia.org/wiki/Shortest_path_problem)
    - > In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.
    - Shortest weighted path problem
* [Finding Clique ](http://en.wikipedia.org/wiki/Clique_problem)
    - >  In computer science, the clique problem refers to any of the problems related to finding particular complete subgraphs ("cliques") in a graph, i.e., sets of elements where each pair of elements is connected.

* [Minimum cut ](http://en.wikipedia.org/wiki/Minimum_cut)
    - > In graph theory, a minimum cut of a graph is a cut (a partition of the vertices of a graph into two disjoint subsets that are joined by at least one edge) whose cut set has the smallest number of edges (unweighted case) or smallest sum of weights possible. Several algorithms exist to find minimum cuts.

The shortest path problem can be solved using Depth First Algorithm.

## [Depth first Algorithm ](https://youtu.be/hmtXhZTfAes?list=PLB2BE3D6CA77BB8F7&t=1431) ##

## Memoization : 37:31 ##

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2/MIT6_00SCS11_lec22.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2/lec22.py)

### Problem Sets ###

1. Problem Set 10: Clustering (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2/MIT6_00SCS11_ps10.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2/ps10.zip)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2/ps10_sol.zip)
2. Problem Set 11 (Assigned)
    1. [Problem Set 11 Due on Lecture 24](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-24-avoiding-statistical-fallacies)

### Check Yourself ###
### What is memoization? ###
### Why is memoization important? ###

