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


The Video Lecture starts [here](https://youtu.be/_QnAUd-em3E?list=PLB2BE3D6CA77BB8F7&t=1512) to discuss Breadth First Search.

In Breadth first search, we get all the path called partial paths from source to destination and then decide which one is the shortest.

Here is the code to find Shortest Path using Breath First Search.

````python
def shortestPathBFS(graph,paths,goal,toPrint = False):
    """
        paths is a list of partial path tuples, in the form of 
        ([path node], pathLength)
        where [path nodes] is a sequential list of Nodes in the path
        and pathLength is an integer denoting the number of Nodes
    """        
    (NODELIST, LENGTH) = (0,1)
    paths = sorted(paths,key=lambda path: path[LENGTH])
    if toPrint:
        print "Path List so far"
        for path in paths:
            nodeNames = [node.getName() for node in path[NODELIST] ]
            print (nodeNames,path[LENGTH])
    newPaths = []
    examiningPath = paths.pop(0)
    for node in graph.childrenOf(examiningPath[NODELIST][-1]):
        if node == goal:
            shortest = examiningPath[NODELIST] + [node]
            return [node.getName() for node in shortest]
        if node not in examiningPath[NODELIST]:
            newPaths.append((examiningPath[NODELIST] + [node], examiningPath[LENGTH] + 1))
    paths.extend(newPaths)
    return shortestPathBFS(graph,paths,goal,toPrint)
````

Lets understand the code mentioned above:-

* Arguments:-
    - `graph `: We pass the complete graph to the code.
    - `paths ` : Contains the list of the partial paths, in the form of list of tuples, like `([path node], pathLength)`, so `path node` is a list of `nodes` in the partial path, and `pathLength` is the length of that list.
    - `goal `: The Node to search.
* ` paths = sorted(paths,key=lambda path: path[LENGTH])` : This first thing which we do is sort the path based on its length, so the shortest path will always be the 0th index.
    - The `lambda ` is the code fragment which we should consider.
    - The `sorted ` function takes a parameter `key ` which takes a function, which returns the sorting parameter.
    - The `lambda ` is a anonymous function
* `examiningPath = paths.pop(0)` : This takes the shortest path list, from the `sorted ` function.
* `examiningPath ` is a list, so we take the last element in this list and find the children of the node, and check if this is same as the `goal ` nodes
    - If it is not, we add this node to the list of `newPath`, which gets appended to the `paths.` and then we call recursively `shortestPathBFS` with this partial path.
    - If this is the `goal ` node, we have found the `shortest ` paths, which we then return.

### Lambda Function ###

Lambda Function is a anonymous function, to do very simple yet complicated things.

Consider this example:-

````python
g = lambda x: x**2

def h(x):
    return x ** 2

print "g(10): ", g(10) #prints 100
print "h(10): ", h(10) #prints 100
````




