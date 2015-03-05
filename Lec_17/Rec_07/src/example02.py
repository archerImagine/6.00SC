import pylab
import random

def showCountinowsUniform(a,b,numPoints):
    points = []
    for m in range(numPoints):
        points.append(random.uniform(a,b))
    pylab.figure()
    pylab.hist(points,100)
    pylab.title('Continous Uniform distribution with ' +str(numPoints) +" points")
    pylab.show()

showCountinowsUniform(0,1.0,100000)    
            