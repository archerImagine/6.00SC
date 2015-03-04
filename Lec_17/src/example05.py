import pylab

def getData(fileName):
    dataFile = open(fileName,'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    print discardHeader
    for line in dataFile:
        d,m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses,distances)

def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*pylab.array(xVals) + b
    pylab.plot(xVals, estYVals, label = 'Linear fit')
    a,b,c,d = pylab.polyfit(xVals, yVals, 3)
    estYVals = a*(xVals**3) + b*xVals**2 + c*xVals + d
    k = 1/a
    print "k: ", k
    pylab.plot(xVals, estYVals, label = 'Cubic fit')
    pylab.legend(loc = 'best')

fitData('../data/springData.txt')
pylab.show()        