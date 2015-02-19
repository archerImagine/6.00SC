import pylab,random

def stdDev(X):
    mean = sum(X)/float(len(X))
    total = 0.0
    for x in X:
        total += (x - mean)**2
    return (total/len(X)) ** 0.5

def poll(n,p):
    votes = 0.0
    for i in range(n):
        if random.random() < p/100.0:
            votes += 1
    return votes

def testErr(n = 1000, p = 46.0, numTrials = 1000):
    results = []
    for t in range(numTrials):
        results.append(poll(n, p))
    print 'std = ' + str((stdDev(results)/n)*100) + '%'
    results = pylab.array(results)/n
    pylab.hist(results)
    pylab.xlabel('Fraction of Votes')
    pylab.ylabel('Number of Polls')


testErr()
pylab.show()    
