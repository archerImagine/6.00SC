# MIT 6.00SC | Lecture 21 | Using Graphs to Model Problems, Part 1 #

## [K-Means Algorithm Explanation ](https://youtu.be/UiZlaJX3IRk?list=PLB2BE3D6CA77BB8F7&t=77) ##

Here is the K-Means code which we will discuss:-

````python
def kmeans(points, k, cutoff, pointType, maxIters = 100,
           toPrint = False):
    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(points, k)
    clusters = []
    #Create a singleton cluster for each centroid
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    #Iterate until change is smaller than cutoff
    while biggestChange >= cutoff and numIters < maxIters:
        #Create a list containing k empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
        for p in points:
            #Find the centroid closest to p
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            for i in range(k):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add p to the list of points for the appropriate cluster
            newClusters[index].append(p)
        #Upate each cluster and record how much the centroid has changed
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = clusters[i].update(newClusters[i])
            biggestChange = max(biggestChange, change)
        numIters += 1
    #Calculate the coherence of the least coherent cluster
    maxDist = 0.0
    for c in clusters:
        for p in c.members():
            if p.distance(c.getCentroid()) > maxDist:
                maxDist = p.distance(c.getCentroid())
    if toPrint:
        print 'Number of iterations =', numIters, 'Max Diameter =', maxDist
    return clusters, maxDist
````

Lets dissect the above code.

* Arguments : The above K-Means function takes 6 arguments.
    - `points` : The points to be clustered.
    - `k` 
        + The number of clusters, unlike hierarchical clustering, in K-Means we have to start with providing the number of clusters which we need.
    - `cutoff `
        + In K-Means algorithm, we continue doing clustering till a point all the clusters are close enough, or what we can say that the difference is not big, This difference is specified by `cutoff `
    - `pointType` : Type of points to be clustered.
    - `maxIters` 
        + Since K-Means is a iterative algorithm, the condition to check for exiting the loop is only `cutOff`, but it is possible that the algorithm do not converge quickly toward `cutOff`, so we use `maxIters` so that we will exit the loop when these many iterations are over.
    - `toPrint`
        + For debugging, to print logs or not.
* So lets start forward, we start with Choose, K initial centroids at random. Checking that we have atleast K points to make K clusters.
    - We can choose the initial centroids based on some algorithms, but most of the time it is chosen at random.
    - Since we are choosing points at random, we might get different result each time we run this K-Mean algorithm. Due to this reason we have to run it multiple times and choose the best clustering.
    - Best clustering is choose with a Min-Max Metrics.
* Initial `clusters` are empty.
* Create a singleton cluster, one for each centroid.
* Till this point all are initializations.
* Now we will iterate till the change is smaller than the `cutoff ` or it has reached `maxIters`
    - Create a list containing `k` empty list.
    - Iterate over each points.
        + Find the centroid in the existing clusters.
    - Add point to the correct clusters.
* Compare the `newClusters` to the existing `clusters`, and get the biggest change.
* Then repeat.
* For the counties example, we are creating pre-configured filters, which gives weight age to corresponding fields.
* In addition to the filters, we also have normalization, to even out disparity in the quantum of weight of each field.

## [Revision Machine Learning ](https://youtu.be/UiZlaJX3IRk?list=PLB2BE3D6CA77BB8F7&t=1483) ##

We have learned about two types of learning.

* Supervised Learning.
    - We started with a training set with labels.
    - We tried to understand the relationship between the features of the points and the labels associated with it.
* Unsupervised Learning.
    - Training set was unlabeled data
    - Try to find relationship among points(features).
* Both Supervised and Unsupervised learning is similar to regression, where we tried to fit curve to data.
* We should be careful about Over fitting especially if the training data is small.
* Feature matters, which feature matters depends on if it is normalized or weighted.
* Features should be relevant to the information we want to learn. This is domain knowledge.

## [Graph Theoretic ](https://youtu.be/UiZlaJX3IRk?list=PLB2BE3D6CA77BB8F7&t=1843)  ##

The most popular way to build a model is Graph Theoretic. Till now, be it curve fitting or machine learning, we are targeting creation of model which we want to create and then learn from them.

There is a rich set of resources like Graph and Graph Theory to understand these models.

Consider this problem:-

Suppose we have a situation which tells us about flight from each city in America to every other city such that the cost involved from a city A to C is came as going from A to B and then B to C.

Based on the above information, what type of models we would like to have.

* Shortest no of hops between two cities.
* Least expensive way involving no more than 2 stops to go from one city to another.

These set of problems are nicely formulated a graph. As shown in [wiki](http://en.wikipedia.org/wiki/Graph_theory)

>  A "graph" in this context is made up of "vertices" or "nodes" and lines called edges that connect them. A graph may be undirected, meaning that there is no distinction between the two vertices associated with each edge, or its edges may be directed from one vertex to another;

Graphs is generally used when there is interesting relationship between the parts.

This domain of study was formulated because of [Seven Bridges of Konigsberg](http://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg), which was solved by Leonhard Euler

### Digraph ###

When the edges between vertices has a direction it is called Digraph or Directed Graph.

### Weighted Directed Graph ###

A graph which have weights associated with edges is called Weighted Directed graph. The WWW, is models as a Graph.

### [Adjacency Matrix](https://youtu.be/UiZlaJX3IRk?list=PLB2BE3D6CA77BB8F7&t=2729) ###

The most important question which hover over Graphs, is which data structure to use to represent Graphs. There are two option

* Adjacency Matrix
    - We have a N * N matrix, which gives the weight connecting the points.
    - The disadvantage is that, it cannot represent multiple edges between nodes.
    - This is a great choice when the connection are dense.
* Adjacency List
    - For every node, we have have list all the edges starting from that node.
The use of one of these two, depends on the application.

The code to Implement graph is shown in Lecture 22.

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-21-using-graphs-to-model-problems-part-1/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-21-using-graphs-to-model-problems-part-1/MIT6_00SCS11_lec21.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-21-using-graphs-to-model-problems-part-1/lec21.py)
4. [Lecture slides (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-21-using-graphs-to-model-problems-part-1/MIT6_00SCS11_lec21_slides.pdf)



### Check Yourself ###
### What are filters used for? ###
### What is a graph? ###
### What is a digraph? ###
### What is a weighted graph? ###
### Based on the code in the handout, why is Graph a subclass of Digraph, rather than the other way around? ###

