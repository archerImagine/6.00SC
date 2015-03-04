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
    extX = pylab.array(xVals + [1.5])
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    extX = extX*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)
    extY = a*pylab.array(extX) + b
    pylab.plot(extX, extY, label = 'Linear fit')
    a,b,c,d = pylab.polyfit(xVals, yVals, 3)
    extY = a*(extX**3) + b*extX**2 + c*extX + d
    pylab.plot(extX, extY, label = 'Cubic fit')
    pylab.legend(loc = 'best')

fitData('../data/springData.txt')
pylab.show()        