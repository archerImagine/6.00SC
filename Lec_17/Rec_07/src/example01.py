import pylab
import random

def showDiscreteUniform(a,b,numPoints):
    points = []
    for m in range(numPoints):
        points.append(random.randint(a,b))
    pylab.figure()
    pylab.hist(points,100,normed=True)
    pylab.title('Discrete Uniform distribution with ' +str(numPoints) +" points")
    pylab.show()

showDiscreteUniform(1,100,100000)    
            