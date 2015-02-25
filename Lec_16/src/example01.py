import pylab

def clear(n,clearProb,steps):
    numRemaning = [n]
    for t in range(steps):
        numRemaning.append(n * ((1 - clearProb) ** t))
    pylab.plot(numRemaning, label = 'Exponential Decay')

clear(1000,0.01,500)    
# pylab.semilogy()
pylab.show()