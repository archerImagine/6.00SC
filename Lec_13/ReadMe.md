# MIT 6.00SC | Lecture 13 | Some Basic Probability and Plotting Data #

## [Introduction ](https://www.youtube.com/watch?v=hGQw3KJ7i6Q&list=PLB2BE3D6CA77BB8F7#t=22) ##

In the last lecture, we had a error in our code, because the Random walk code, did not output correct value of small samples as we had manually checked.

The problem was in the `simWalks()` method, which used wrong arguments, we had used this:-

````
distances.append(walk(f, homer, numTrials))
````

But we should have used:-

````
distances.append(walk(f, homer, numSteps))
````

So the complete corrected code is:-

````
import random

class Location(object):
    def __init__(self, x,y):
        """x and y are float"""
        self.x = x
        self.y = y
    def move(self,deltaX,deltaY):
        """deltaX and deltaY are float"""
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self,other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2) ** 0.5
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
        def __init__(self):
            self.drunks = {}
        def addDrunk(self,drunk,loc):
            if drunk in self.drunks:
                raise ValueError('Duplicate Drunk')
            else:
                self.drunks[drunk] = loc
        def moveDrunk(self,drunk):
            if not drunk in self.drunks:
                raise ValueError('Drunk not in field')
            xDist,yDist = drunk.takeStep()
            self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
        def getLoc(self, drunk):
            if not drunk in self.drunks:
                raise ValueError('Drunk not in field')
            return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
    def __str__(self):
        return 'This drunk is named ' + self.name

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))
def simWalks(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances
def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 10000, 100000]:
    # for numSteps in [0,1]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print '  Mean =', sum(distances)/len(distances)
        print '  Max =', max(distances), 'Min =', min(distances)
                
homer = Drunk("homer")
origin = Location(0,0)
field = Field()
field.addDrunk(homer,origin)
print "walk(field,homer,10): ", walk(field,homer,10)

drunkTest(10)
````

The above problem of random walk will give different output every time you run it, also we cannot infer much from it. So these type of problem are called stochastic problems.

## [Role of RandomNess in computation ](https://www.youtube.com/watch?v=hGQw3KJ7i6Q&list=PLB2BE3D6CA77BB8F7#t=515) ##

If we consider Newtonian physics, it is very comforting. To ever cause there is a reaction. Everything is deterministic.

Then came [Copenhagen Doctrines](http://en.wikipedia.org/wiki/Copenhagen_interpretation), associated with quantum physics changed this deterministic view of the world. It argued that, 

> natural change is necessarily by way of indeterministic physically discontinuous transitions between discrete stationary states

One can make probabilistic statements of the form **"X is highly likely to happen"**, but not statement of the form **"X is certain to happen."** What they meant was, The world is Stochastic.

But Einstein and Schrodinger disagreed the [Copenhagen Doctrines](http://en.wikipedia.org/wiki/Copenhagen_interpretation).

These two have practically divided the physics world, and at the heart of it was **Causal Non Determinism**.

### Causal Non Determinism ###

Causal Non Determinism believed that not every event is based on the cause of a previous event. Which was disagree by Einstein and Schrodinger. Famously said by Einstein "God Does not play Dice."

### Predictive Non Determinism ###

Our inability to make measurement of the physical world makes it impossible to make prediction of the future. So basically this means, things are not unpredictable, it just looks unpredictable because we do not have enough information.

## [Stochastic Process ](https://www.youtube.com/watch?list=PLB2BE3D6CA77BB8F7&feature=player_detailpage&v=hGQw3KJ7i6Q#t=895) ##

A process is **Stochastic**, if its next step depends on both, i.e. the previous state and some random elements.

The random elements in python are introduced by the help of `random.random()`, which generates a random value between `0.0` and `1.0`.

Consider the example of rolling a dice, suppose we roll a dice, which one of the following sequence is more likely to be possible, if the dice is rolled 10 times.:-

````
1111111111
5442462412
````
The answer is both the answer are equally likely, as each roll of dice is independent of the previous rolls.

In a Stochastic process, two events are independent, if the outcome of one event has no influence on the outcome of the other.

Consider one more example, which we do with a Coin. So on a coin flip, what are the maximum number of output we can get. It is `2`, heads or tails. So If we flip the coin for 10 times, the total different sequence of `1` and `0` it will create is `2^10`.

So in the flipping of coin for 10 times, both 10 times `0` and `1` is equally likely to happen.

What is the probability of getting all `1`, is `1/2^10`. 

Probability = what fraction of the possible results have the property we are testing for.

Probability lies between `0` to `1`. `0` meaning will never happen, `1` means most certain to happen.

Another interesting question will be, what is the probability of getting anything other than all `1`.

````
1 - 1/2^10
````

## [Data Visualization ](https://www.youtube.com/watch?list=PLB2BE3D6CA77BB8F7&feature=player_detailpage&v=hGQw3KJ7i6Q#t=1528) ##

Data Visualization is very important, because a visual data representation is always good enough, that simple print or log statements. We know this, but very rarely we draw/plot graphs in programming language as it is very difficult to plot.

In python, it is very easy, because of [PyLab](matplotlib.sourceforge.net), which gives most of the functionality from Matlab.

Consider this example:-

````
import pylab

pylab.plot([1,2,3,4], [1,2,3,4])
pylab.plot([1,4,2,3], [5,6,7,8])
pylab.show()
````
In the above code, the `show()` method will finally display the result as a plot. Mostly we write intermediate steps into a file, and then finally writing it. Also `show()` method should be used only once in a program and it is mostly at the end of the text. 

Consider the below example:-

````
import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,2,3,4])
pylab.figure(2)
pylab.plot([1,4,2,3], [5,6,7,8])
pylab.savefig('firstSaved')
pylab.figure(1)
pylab.plot([5,6,7,10])
pylab.savefig('secondSaved')

pylab.show()
````

We can also, label x and y axis, which a graph title:--

````
pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')
````

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-13-some-basic-probability-and-plotting-data/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-13-some-basic-probability-and-plotting-data/MIT6_00SCS11_lec13.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-13-some-basic-probability-and-plotting-data/lec13.py)
4. [Install PyLab](../misc/ReadMe.md)

### Check Yourself ###
### What is a stochastic process? ###
### What makes two events independent? ###
