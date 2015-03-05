import pylab
import random
import math

def frange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def makeGaussianPlot(mu,sigma,numPoints,showIdel=True):
    points = []
    for m in range(numPoints):
        points.append(random.gauss(mu,sigma))
    idealPointsX = [frange(mu - (sigma * 3), mu + (sigma * 3), 0.0001)]
    idealPointsY = []
    for x in idealPointsX:
        y = 1.0/math.sqrt(2.0 * math.pi * sigma**2) * math.exp(-(x - mu) ** 2)
        idealPointsY.append(y)

    pylab.figure()
    pylab.hist(points,100,normed=True)

    if showIdel:
        pylab.plot(idealPointsX,idealPointsY,c="r",lw=5)
        pylab.legend(['Ideal Curve', 'Random Points'])
    else:
        pylab.legend(['Random Points'])
    
    pylab.title('Gaussian distribution with' +str(numPoints) +"Points")        

makeGaussianPlot(0,1,100000,False)    