import pylab, random, string,copy

class Point(object):
    """docstring for Point"""
    def __init__(self, name,originalAttrs,normalizedAttrs=None):
        """normalizedAttrs and originalAttrs are both Arrays."""
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

    def distance(self,other):
        # Eculidean distance metrics.
        result = 0.0
        for i in range(self.dimensionality()):
            result += (self.attrs[i] - other.attrs[i]) ** 2
        return result ** 0.5

    def getName(self):
        return self.name

    def toStr(self):
        return self.name + str(self.attrs)

    def __str__(self):
        return self.name

class Cluster(object):
    def __init__(self, points,pointType):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()

    def singleLinkageDist(self,other):
        minDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) < minDist:
                    minDist = p1.distance(p2)
        return minDist

    def maxLinkageDist(self,other):
        maxDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) > maxDist:
                    maxDist = p1.distance(p2)
    
    def averageLinkageDist(self,other):
        totDist = 0.0
        for p1 in self.points:
            for p2 in other.points:
                totDist += p1.distance(p2)
        return totDist/(len(self.points) * len(other.points))

    def update(self,points):
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

    def isIn(self,name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False

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
        centroid = self.pointType('mean', totVals/len(self.points)), totVals/len(self.points)

        return centroid
            

                        