import pylab
import random
import math

def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L

#http://code.activestate.com/recipes/66472-frange-a-range-function-with-float-increments/

def makeGaussianPlot(mu,sigma,numPoints,showIdel=True):
    points = []
    for m in range(numPoints):
        points.append(random.gauss(mu,sigma))
    idealPointsX = frange(mu - (sigma * 3), mu + (sigma * 3), 0.0001)
    print type(idealPointsX)
    idealPointsY = []
    for x in idealPointsX:
        y = 1.0/math.sqrt(2.0 * math.pi * sigma**2) * math.exp(-((x - mu) ** 2/ (2 * sigma **2)))
        idealPointsY.append(y)

    pylab.figure()
    pylab.hist(points,100,normed=True)

    if showIdel:
        pylab.plot(idealPointsX,idealPointsY,c="r",lw=5)
        pylab.legend(['Ideal Curve', 'Random Points'])
    else:
        pylab.legend(['Random Points'])
    
    pylab.title('Gaussian distribution with' +str(numPoints) +"Points")    
    pylab.show()    

makeGaussianPlot(0,1,100000,True)    