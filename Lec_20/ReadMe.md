# MIT 6.00SC | Lecture 20 | More Clustering #

## [Feature Vector ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=93) ##

In the last lecture, we saw example and the notion of clustering, In clustering we used linkage criteria to get the clusters. Now if we use a wrong linkage criteria, we might not get an optimal answer.

One more concept we studies or rather brushed through is **Feature Vector**. So we start with the concept that in place of generalizing just based on one feature, to being able to generalize based on a Feature Vector.

If all the feature in a feature vector are represented by the same physical units, we might find that easier ways of identifying the generalization.

In case a feature vector contains feature which cannot be represented in the same physical units ex. a feature vector containing, distance between cities and their temperature, then we have an issue of generalizing the feature vector.

So if we are using different physical unit for feature representation in a feature vector, we might have to think about **how to scale the elements of the vector.**

### [Scaling ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=259) ###

Scaling is not only required when we have different physical unit of representation of feature in a feature vector, It is even important when we have the same physical unit.

Consider the image in lecture slide [page 2](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_lec20_slides.pdf), in which both height and width, are presented in inches. So if we scale based on height the clusters will be more skewed, because the variation in width is much smaller than in height for a person.

So the understanding we have to take is we have to think hard on how to scale a feature, because a wrong scale can have adverse effect on the cluster.

To identify the scale factor and to identify the clusters, we have to have the **Domain Knowledge.**

### [Domain Knowledge ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=422) ###

When we are involved in any type of learning be it supervised or unsupervised, the feature selection and scaling is critical, and to help in this regard we might need Domain Knowledge.

### [Minkowski metric ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=493) ###

Minkowski metric helps in doing the scaling, as per [wiki](http://en.wikipedia.org/wiki/Minkowski_distance)

> The Minkowski distance is a metric in a normed vector space which can be considered as a generalization of both the Euclidean distance and the Manhattan distance.

**Definition : ** 

The Minkowski distance of order p between two points

![](http://upload.wikimedia.org/math/1/1/e/11ed0dab51d86c81395e1def760c91c5.png)

is defined as

![](http://upload.wikimedia.org/math/a/a/0/aa0c62083c12390cb15ac3217de88e66.png)

For ![](http://upload.wikimedia.org/math/a/a/4/aa47fa19b67316cd180a645dec5bf0b7.png)  the Minkowski distance is a metric as a result of the Minkowski inequality.

Minkowski distance is typically used with p being 1 or 2. The latter is the Euclidean distance, while the former is sometimes known as the Manhattan distance.


As per wiki Manhattan distance is defined as:-

> The distance between two points in a grid based on a strictly horizontal and/or vertical path (that is, along the grid lines), as opposed to the diagonal or "as the crow flies" distance. The Manhattan distance is the simple sum of the horizontal and vertical components, whereas the diagonal distance might be computed by applying the Pythagorean theorem.

Till now we were dealing with feature vector which were comparable, i.e. they were mainly numbers, but a lot of time we have to deal with **Nominal category** of data, where we cannot use numbers to represent data.

In case of Nominal category of data, we convert these data to numbers with the help of Domain knowledge.

Once we have number representation of a **Nominal data**, we will use scaling or normalization, to generalize every feature between `0` and `1`. This is required because everything is normalized to the same dynamic range, and then we can compare them.


## [Clustering Example ](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=866) ##

Lets see an example of Clustering, using Hierarchical Clustering.

Here is an example:-

````
#Code shared across examples
import pylab, random, string, copy

class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None):
        """normalizedAttrs and originalAttrs are both arrays"""
        self.name = name
        self.unNormalized = originalAttrs
        if normalizedAttrs == None:
            self.attrs = originalAttrs
        else:
            self.attrs = normalizedAttrs
    def dimensionality(self):
        return len(self.attrs)
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized
    def distance(self, other):
        #Euclidean distance metric
        result = 0.0
        for i in range(self.dimensionality()):
            result += (self.attrs[i] - other.attrs[i])**2
        return result**0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name + str(self.attrs)
    def __str__(self):
        return self.name        
    
class Cluster(object):
    def __init__(self, points, pointType):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()
    def singleLinkageDist(self, other):
        minDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) < minDist:
                    minDist = p1.distance(p2)
        return minDist
    def maxLinkageDist(self, other):
        maxDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) > maxDist:
                    maxDist = p1.distance(p2)
        return maxDist
    def averageLinkageDist(self, other):
        totDist = 0.0
        for p1 in self.points:
            for p2 in other.points:
                totDist += p1.distance(p2)
        return totDist/(len(self.points)*len(other.points))
    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        if len(points) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
    def members(self):
        for p in self.points:
            yield p
    def isIn(self, name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def __str__(self):
        names = []
        for p in self.points:
            names.append(p.getName())
        names.sort()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]
    def getCentroid(self):
        return self.centroid
    def computeCentroid(self):
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        centroid = self.pointType('mean',
                                   totVals/float(len(self.points)),
                                   totVals/float(len(self.points)))
        return centroid

class ClusterSet(object):
    def __init__(self, pointType):
        self.members = []
    def add(self, c):
        if c in self.members:
            raise ValueError
        self.members.append(c)
    def getClusters(self):
        return self.members[:]
    def mergeClusters(self, c1, c2):
        points = []
        for p in c1.members():
            points.append(p)
        for p in c2.members():
            points.append(p)
        newC = Cluster(points, type(p))
        self.members.remove(c1)
        self.members.remove(c2)
        self.add(newC)
        return c1, c2
    def findClosest(self, metric):
        minDistance = metric(self.members[0], self.members[1])
        toMerge = (self.members[0], self.members[1])
        for c1 in self.members:
            for c2 in self.members:
                if c1 == c2:
                    continue
                if metric(c1, c2) < minDistance:
                    minDistance = metric(c1, c2)
                    toMerge = (c1, c2)
        return toMerge    
    def mergeOne(self, metric, toPrint = False):
        if len(self.members) == 1:
            return None
        if len(self.members) == 2:
            return self.mergeClusters(self.members[0],
                                      self.members[1])
        toMerge = self.findClosest(metric)
        if toPrint:
            print 'Merged'
            print '  ' + str(toMerge[0])
            print 'with'
            print '  ' + str(toMerge[1])
        self.mergeClusters(toMerge[0], toMerge[1])
        return toMerge
    def mergeN(self, metric, numClusters = 1, history = [],
               toPrint = False):
        assert numClusters >= 1
        while len(self.members) > numClusters:
            merged = self.mergeOne(metric, toPrint)
            history.append(merged)
        return history
    def numClusters(self):
        return len(self.members) + 1
    def __str__(self):
        result = ''
        for c in self.members:
            result = result + str(c) + '\n'
        return result

#Mammal's teeth example
class Mammal(Point):
    def __init__(self, name, originalAttrs, scaledAttrs = None):
        Point.__init__(self, name, originalAttrs, originalAttrs)
    def scaleFeatures(self, key): 
        scaleDict = {'identity': [1,1,1,1,1,1,1,1],
                     '1/max': [1/3.0,1/4.0,1.0,1.0,1/4.0,1/4.0,1/6.0,1/6.0]}
        scaledFeatures = []
        features = self.getOriginalAttrs()
        for i in range(len(features)):
            scaledFeatures.append(features[i]*scaleDict[key][i])
        self.attrs = scaledFeatures
        
def readMammalData(fName):
    dataFile = open(fName, 'r')
    teethList = []
    nameList = []
    for line in dataFile:
        if len(line) == 0 or line[0] == '#':
            continue
        dataLine = string.split(line)
        teeth = dataLine.pop(-1)
        features = []
        for t in teeth:
            features.append(float(t))
        name = ''
        for w in dataLine:
            name = name + w + ' '
        name = name[:-1]
        teethList.append(features)
        nameList.append(name)
    return nameList, teethList
    
def buildMammalPoints(fName, scaling):
    nameList, featureList = readMammalData(fName)
    points = []
    for i in range(len(nameList)):
        point = Mammal(nameList[i], pylab.array(featureList[i]))
        point.scaleFeatures(scaling)
        points.append(point)
    return points

#Use hierarchical clustering for mammals teeth
def test0(numClusters = 2, scaling = 'identity', printSteps = False,
          printHistory = True):
    points = buildMammalPoints('../data/mammalTeeth.txt', scaling)
    cS = ClusterSet(Mammal)
    for p in points:
        cS.add(Cluster([p], Mammal))
    history = cS.mergeN(Cluster.maxLinkageDist, numClusters,
                        toPrint = printSteps)
    if printHistory:
        print ''
        for i in range(len(history)):
            names1 = []
            for p in history[i][0].members():
                names1.append(p.getName())
            names2 = []
            for p in history[i][1].members():
                names2.append(p.getName())
            print 'Step', i, 'Merged', names1, 'with', names2
            print ''
    clusters = cS.getClusters()
    print 'Final set of clusters:'
    index = 0
    for c in clusters:
        print '  C' + str(index) + ':', c
        index += 1

test0()                
````

[Start Here](https://youtu.be/Iu4xTLKcbPo?list=PLB2BE3D6CA77BB8F7&t=1137)

## K-Means Clustering : 41:25 ##





## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_lec20.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/lec20.py)
4. [Lecture slides (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_lec20_slides.pdf)
5. [Lecture data files (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/lec20_data.zip)

### Problem Sets ###

1. Problem Set 9: Schedule Optimization (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/MIT6_00SCS11_ps9.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/ps9.zip)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering/ps9_sol.zip)
2. Problem Set 10 (Assigned)
    1. [Problem Set 10 Due on Lecture 22](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2)

### Check Yourself ###
### How do we use nominal (non-numeric or noncontinuous) categories as features? ###
### Why do we need to use scaling (normalization)? ###
### How does k-means clustering work? ###
