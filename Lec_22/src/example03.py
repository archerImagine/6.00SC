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

def shortestPath(graph,start,end,toPrint=False,visited = []):
    global numCalls
    numCalls += 1
    if toPrint: #for debugging
        print "", start, end
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

def dpShortestPath(graph, start, end, visited = [], memo = {}):
    global numCalls
    numCalls += 1
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

def test3(kind):
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
    shortest = shortestPath(g, nodes[0], nodes[4])
    print 'The shortest path:'
    print shortest
    shortest = dpShortestPath(g, nodes[0], nodes[4])
    print 'The shortest path: DP'
    print shortest

# test3(Digraph)    

def bigTest2(kind, numNodes = 25, numEdges = 200):
    global numCalls
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
    numCalls = 0
    print shortestPath(g, nodes[0], nodes[4])
    print 'Number of calls to shortest path =', numCalls
    numCalls = 0
    print dpShortestPath(g, nodes[0], nodes[4])
    print 'Number of calls to dp shortest path =', numCalls

bigTest2(Digraph)
