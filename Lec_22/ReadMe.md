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

* [Wiki Link](http://en.wikipedia.org/wiki/Depth-first_search)

The **DFS** as defined in Wikipedia tells that:-

> Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking.

Some points to keep in mind when using a Depth First Search Algorithm:-

* Since this is a recursive algorithms, the recursion ends when Start node is same as End Node.
* Recursion starts by choosing one child and continue till
    - It reaches a node with no Children.
        + Once it reaches here, and has not find the node it is searching for, it back tracks and takes the next child of the node it was at.
    - Reaches the Node which we are trying to search.
    - Important condition, It reaches a Node, It has already seen, i.e. already visited. This is done to avoid cycle in the graph.

Here is the code for recursive depth first algorithm.

````python
def shortestPath(graph,start,end,toPrint=False,visited = []):
    # global numCalls
    # numCalls += 1
    if toPrint: #for debugging
        print start, end
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    if start == end:
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited): #avoid cycles
            visited = visited + [str(node)] #new list
            newPath = shortestPath(graph, node, end, toPrint, visited)
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path
````

Lets examine the code, step by step.

* Arguments:-
    - `graph ` :  reference of the graph which need to be traversed is passed.
    - `start ` : The starting node of the graph, from where the search has to start.
    - `end ` : The end node, where the search has to end.
    - `toPrint `:  Decide if the debugging statement needs to be printed or not.
    - `visited ` : A list which stores the node already traversed.
* The house keeping is done in the first few line, like to decide if logs needs to be printed or not, check if the start or end node are present in graph or not.
* `path = [str(start)]` : stores the starting node into the list of path.
* `if start == end:` : If starting node is same as end node, exit the function and return the `path`.
* `shortest = None` : Since the traversal has not yet begun, there is no shortest path yet.
* `for node in graph.childrenOf(start):` iterate through all the children of the `start` node.
    - `if (str(node) not in visited):` check if the node is already visited, so to avoid cycle.
    - `visited = visited + [str(node)]` create a visited list, for the check mentioned above, with the current node under examination being added to it. This creates a new list, inplace of mutating the old list using append.
    - `newPath = shortestPath(graph, node, end, toPrint, visited)` start the recursion with the start node being the current node under investigation.
    - Check if the node is found or not, if found, check if the length is shortest or not.

So this `shortestPath`, we will execute on a small graph with `test2`, with very few nodes and edges.

````python
def test2(kind, toPrint = False):
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
    print 'The graph:'
    print g
    shortest = shortestPath(g, nodes[0], nodes[4], toPrint)
    print 'The shortest path:'
    print shortest
````

In this case we get the output very quickly, but we have a graph with `25` nodes and `200` edges, like in this example:-

````python
def bigTest1(kind, numNodes = 25, numEdges = 200):
    nodes = []
    for name in range(numNodes):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    for e in range(numEdges):
        src = nodes[random.choice(range(0, len(nodes)))]
        dest = nodes[random.choice(range(0, len(nodes)))]
        g.addEdge(Edge(src, dest))
    print g
    print shortestPath(g, nodes[0], nodes[4])
````

This takes a fairly large amount of time to find the shortest path. To check why is this taking so long, we will run the `test2` with the debugging statement `on`.

Here is the output of that.

````
0 4
 1 4
 0 4
 2 4
 3 4
 4 4
 5 4
 4 4
 2 4
 3 4
 4 4
 5 4
 2 4
 3 4
 4 4
 5 4
 0 4
 4 4
 4 4
````

Now if we see above, we find that, we are check a lot of Path which we have already checked, like `0 4` , `2 4`, `3 4` is also check trice and `4 4` is check 5 times. So we are solving the same problem multiple times.

The solution to this problem is Memoization. Where we store already solved problem and just look that up.

## [Memoization](https://youtu.be/hmtXhZTfAes?list=PLB2BE3D6CA77BB8F7&t=2212) ##

As per [wikipedia](http://en.wikipedia.org/wiki/Memoization)

> In computing, memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. Memoization has also been used in other contexts (and for purposes other than speed gains), such as in simple mutually recursive descent parsing[1] in a general top-down parsing algorithm[2][3] that accommodates ambiguity and left recursion in polynomial time and space. Although related to caching, memoization refers to a specific case of this optimization, distinguishing it from forms of caching such as buffering or page replacement. In the context of some logic programming languages, memoization is also known as tabling;[4] see also lookup table.

This is just a fancy way to tell we are going to use a Table look-up. 

The concept of Memoization is at the heart of a programming technique called [Dynamic Programming ](http://en.wikipedia.org/wiki/Dynamic_programming).

### [Dynamic Programming ](https://youtu.be/hmtXhZTfAes?list=PLB2BE3D6CA77BB8F7&t=2320) ###

The Dynamic Programming using Memoization, version of the shortest path is:-

````python
def dpShortestPath(graph, start, end, visited = [], memo = {}):
    # global numCalls
    # numCalls += 1
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    if start == end:
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited):
            visited = visited + [str(node)]
            try:
                newPath = memo[node, end]
            except:
                newPath = dpShortestPath(graph, node, end,
                                         visited, memo)
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
                memo[node, end] = newPath
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path
````

Lets examine the above code, each step at a time.

* Arguments:-
    - `graph ` :  reference of the graph which need to be traversed is passed.
    - `start ` : The starting node of the graph, from where the search has to start.
    - `end ` : The end node, where the search has to end.
    - `toPrint `:  Decide if the debugging statement needs to be printed or not.
    - `visited ` : A list which stores the node already traversed.
    - `memo ` : Is a Dictionary, which stores, the path already traversed.
* All the steps are similar to the normal Shortest path algorithms, except these.
* `newPath = memo[node, end]` : we try to find if we have already traversed the path, if not, it gives an exception which means we have not traversed a path, and then we run the algorithm recursively.


Since performance was a prime concern for us, lets see how the Dynamic programming solution prevails, if we check the no of calls which is made, as shown below.

````
Number of calls to shortest path = 398094
Number of calls to dp shortest path = 76
````

So we can see with Dynamic Programming, we have a huge reduction in the no of recursive calls being made.

Dynamic Programming, was conceptualized by Robert Bellman, The reason for naming it Dynamic Programming can be found [here](http://www.eng.tau.ac.il/~ami/cd/or50/1526-5463-2002-50-01-0048.pdf)

Dynamic programming is very important because it provide solution to Optimization techniques which on the surface looks intractable or exponential in nature.

So when can we use Dynamic programming, we cannot use it all the time, we can use it for problem which exhibits following 2 properties.

* The problem must have a optimal substructure.
    - We can find globally optimal solution, by combining locally optimal solution.
* It should have overlapping subproblems.
    - So we should have a provision that we can look-up already existing solutions.

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

