import pylab

def getXSpeed(a, b, c, minX, maxX):
    """minX and maxX are distances in inches"""
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*12 #accel. of gravity in inches/sec/sec
    t = (2.0*yPeak/g)**0.5
    return xMid/(t*12.0)
    #print 'speed = ' + str(int(xMid/(t*12))) + ' feet/sec'

def getTrajectoryData(fileName):
    dataFile = open(fileName,'r')    
    distances = []
    heights1,heights2,heights3,heights4=[],[],[],[]
    discardHeader = dataFile.readline()
    print "discardHeader: ", discardHeader
    for line in dataFile:
        d,h1,h2,h3,h4 = line.split()
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
    dataFile.close()
    return distances,[heights1,heights2,heights3,heights4]

def rSquare(measured,estimated):
    """
        measured: one dimensional array of measured values
        estimated: one dimensional array of predicted values
    """
    EE = ((estimated - measured) ** 2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured) ** 2).sum()
    return 1 - EE/MV


def processTrajectories(fName):
    distances, heights = getTrajectoryData(fName)
    distances = pylab.array(distances)*36
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    meanHeights = totHeights/len(heights)
    pylab.plot(distances, meanHeights, 'bo')
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) +  b*distances + c
    speed = getXSpeed(a, b, c, distances[-1], distances[0])
    pylab.plot(distances, altitudes, 'g',
               label = 'Quad. Fit' + ', R2 = '
               + str(round(rSquare(meanHeights, altitudes), 2))
               + ', Speed = ' + str(round(speed, 2)) + 'feet/sec')
    pylab.legend()

processTrajectories('../data/lec18_launcher.txt')
pylab.show()