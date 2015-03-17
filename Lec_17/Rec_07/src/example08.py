import math
import random
import numpy
import pylab

# float range
def frange(start,stop,step):
    l = []
    for i in range(int((stop - start)/step)):
        l.append(start + step*i)
    return l

#
# rSquared
#

def mse(measured,predicted):
    """Compute Sum of Residual Square"""
    sum_sq = 0
    for i in xrange(len(measured)):
        sum_sq = (measured[i] - predicted[i]) ** 2
    return float(sum_sq)
def sstot(measured):
    """Compute total of sum square"""
    nMean = sum(measured) /float(len(measured))
    ntot = 0
    for m in measured:
        ntot += (m - nMean) ** 2
    return ntot
def rSquared(measured,predicted):
    """
        measured: list of measured values
        predicted: list of predicted values
    """
    SSerr = mse(measured, predicted)
    SStot = sstot(measured)

    return 1.0 - SSerr/SStot

def makeCurve(f,xs):
    ys = []    
    for x in xs:
        ys.append(f(x))
    return ys

def addNoise(ys, stddev = 1):
    ysp = []
    for y in ys:
        ysp.append(random.gauss(y,stddev))
    return ysp

def makeObservations(xs,f,noise):
    # Make a theoritical curve
    ys = makeCurve(f,xs)    

    # Add some noise to the simulate environment
    nys = addNoise(ys)

    return nys

def showExamplePolyFit(xs,ys,fitDegree1 = 1,fitDegree2 = 2):
    pylab.figure()    
    pylab.plot(xs,ys,'r.',ms=2.0,label = "measured")

    # poly fit to noise
    coeeff = numpy.polyfit(xs, ys, fitDegree1)

    # Predict the curve
    pys = numpy.polyval(numpy.poly1d(coeeff), xs)

    se = mse(ys, pys)
    r2 = rSquared(ys, pys)

    pylab.plot(xs,pys, 'g--', lw=5,label="%d degree fit, SE = %0.10f, R2 = %0.10f" %(fitDegree1,se,r2))

    # Poly fit to noise
    coeeffs = numpy.polyfit(xs, ys, fitDegree2)

    # Predict the curve
    pys = numpy.polyval(numpy.poly1d(coeeffs), xs)

    se = mse(ys, pys)
    r2 = rSquared(ys, pys)

    pylab.plot(xs,pys, 'b--', lw=5,label="%d degree fit, SE = %0.10f, R2 = %0.10f" %(fitDegree2,se,r2))

    pylab.legend()

def f(x):
    return x**3 + 5*x

xs = frange(-5,5,0.001)        
ys = makeObservations(xs, f, 3)

showExamplePolyFit(xs, ys, 1,2)
showExamplePolyFit(xs, ys, 2,3)
showExamplePolyFit(xs, ys, 3,4)
showExamplePolyFit(xs, ys, 4,5)
pylab.show()