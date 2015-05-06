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

## [Revision Machine Learning ](https://youtu.be/UiZlaJX3IRk?list=PLB2BE3D6CA77BB8F7&t=1499) ##

## [Graph Theoretic ](https://youtu.be/UiZlaJX3IRk?list=PLB2BE3D6CA77BB8F7&t=1843)  ##

### Digraph ###

### Weighted Directed Graph ###

### [Adjacency Matrix](https://youtu.be/UiZlaJX3IRk?list=PLB2BE3D6CA77BB8F7&t=2729) ###


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

