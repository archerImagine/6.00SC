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
    def __init__(self, src,dest,weight=0):
        self.src = src
        self.dest = dest
        self.weight = weight
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
    def hasNode(self,node):
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


def test3(kind, toPrint=False):
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
    print g, "\n"
    shortest = shortestPathBFS(g, [([nodes[0]],1)], nodes[4],toPrint)
    print 'The shortest path:'
    print shortest

test3(Digraph)      