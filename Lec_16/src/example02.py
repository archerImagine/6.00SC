import pylab,random

def clear(n,clearProb,steps):
    numRemaning = [n]
    for t in range(steps):
        numRemaning.append(n * ((1 - clearProb) ** t))
    pylab.plot(numRemaning, label = 'Exponential Decay')



def clearSim(n,clearProb,steps):
    numRemaning = [n]
    for t in range(steps):
        numLeft = numRemaning[-1]
        for m in range(numRemaning[-1]):
            if random.random() <= clearProb:
                numLeft -= 1
        numRemaning.append(numLeft)
    pylab.plot(numRemaning,"r",label = "simulation")

clear(1000,0.01,500)    
clearSim(1000,0.01,500)
pylab.show()