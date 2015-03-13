import math
import random
import pylab


# float range
def frange(start,stop,step):
    l = []
    for i in range(int((stop - start)/step)):
        l.append(start + step*i)
    return l

# def frange(start, end=None, inc=None):
#     "A range function, that does accept float increments..."

#     if end == None:
#         end = start + 0.0
#         start = 0.0

#     if inc == None:
#         inc = 1.0

#     L = []
#     while 1:
#         next = start + len(L) * inc
#         if inc > 0 and next >= end:
#             break
#         elif inc < 0 and next <= end:
#             break
#         L.append(next)
        
#     return L

def find_function_ymin_ymax(f,xmin,xmax,xstep = 0.001):
    ymin = None
    ymax = None

    for x in frange(xmin,xmax,xstep):
        f_y = f(x)    
        if ymin is None or f_y < ymin:
            ymin = f_y
        if ymax is None or f_y > ymax:
            ymax = f_y
    return (ymin,ymax)

# generate random points between xmin <= x <= xmax
# and ymin <= y <= ymax    

def randomPoints(xmin,xmax,ymin,ymax):
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymin, ymax)

    return(x,y)

def makePoints(xmin,xmax,ymin,ymax,numPoints):
    points = []    
    for n in range(numPoints):
        points.append(randomPoints(xmin,xmax,ymin,ymax))
    return points

def betweenCurve(f,points):
    return math.fabs(points[1]) <= math.fabs(points[0])

def estimateArea(f,xmin,xmax,numPoints,points = None):
    ymin,ymax = find_function_ymin_ymax(f, xmin, xmax)
    if points is None:
        points = makePoints(xmin, xmax, ymin, ymax, numPoints)

    pointCounter = 0
    for point in points:
        x = point[0]
        y = point[1]

        # is the point between the function and the X-axis?
        if betweenCurve(f,point):
            if y > 0 :
                pointCounter += 1 # above x-axis add to area
            if y < 0 :
                pointCounter -= 1 # below x-axix substract from area.
    rectArea = (xmax - xmin) * (ymax - ymin)
    fnArea = rectArea*pointCounter/float(numPoints)
    return fnArea

def f(x):
    return (x ** 2)

def plotFnScatter(f,xmin,xmax,numPoints):
    ymin,ymax = find_function_ymin_ymax(f,xmin,xmax)
    points = makePoints(xmin, xmax, ymin, ymax, numPoints)

    fnPointsX = []
    fnPointsY = []
    sqPointsX = []
    sqPointsY = []

    for point in points:
        if betweenCurve(f,point):
            fnPointsX.append(point[0])
            fnPointsY.append(point[1])
        else:
            sqPointsX.append(point[0])
            sqPointsY.append(point[1])
    pylab.figure()
    pylab.clf()
    pylab.scatter(sqPointsX, sqPointsY,c = "r")
    pylab.scatter(fnPointsX, fnPointsY,c = "b")
    pylab.title("With " +str(numPoints) +" points")
    pylab.axis([xmin,xmax,ymin,ymax])
    pylab.show()

numPointsList = [10,100,1000,10000,100000]    
for numPoints in numPointsList:
    print str(numPoints) + ' Points gives an area estimate of ' +str(estimateArea(f,-5,5,numPoints))
    plotFnScatter(f, -5, 5, numPoints)

