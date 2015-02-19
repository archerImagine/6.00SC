import pylab,random

def stdDev(X):
    mean = sum(X)/float(len(X))
    total = 0.0
    for x in X:
        total += (x - mean)**2
    return (total/len(X)) ** 0.5

def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1.0
    return heads/numFlips

def flipSim(numFlipsPerTrails,numTrails):
    fracHeads = []    
    for i in range(numTrails):
        fracHeads.append(flip(numFlipsPerTrails))
    return fracHeads

def labelPlot(nf,nt,mean,sd):
    pylab.title(str(nt) + ' trials of '+ str(nf) + ' flips each')    
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 6))
               + '\nSD = ' + str(round(sd, 6)))
def makePlots(nf1, nf2, nt):
    """nt = number of trials per experiment
       nf1 = number of flips 1st experiment
       nf2 = number of flips 2nd experiment"""
    fracHeads1 = flipSim(nf1, nt)
    mean1 = sum(fracHeads1)/float(len(fracHeads1))
    sd1 = stdDev(fracHeads1)
    pylab.hist(fracHeads1, bins = 20)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    labelPlot(nf1, nt, mean1, sd1)
    pylab.figure()
    fracHeads2 = flipSim(nf2, nt)
    mean2 = sum(fracHeads2)/float(len(fracHeads2))
    sd2 = stdDev(fracHeads2)
    pylab.hist(fracHeads2, bins = 20)
    pylab.hist(fracHeads2, bins = 20)
    pylab.xlim(xmin, xmax)
    ymin, ymax = pylab.ylim()
    labelPlot(nf2, nt, mean2, sd2)    

makePlots(100, 1000, 100000)
pylab.show()    