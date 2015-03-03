# MIT 6.00SC | Lecture 17 | Curve Fitting #

## [Introduction](https://www.youtube.com/watch?feature=player_detailpage&v=TIQTYgmavC4&list=PLB2BE3D6CA77BB8F7#t=25) ##

In the last lecture, when we were finding the value of Pi, we started with an assumption that if we drop large enough pins and if we repeat this experiment multiple times, if we get a very small standard deviation we will have a correct value of PI.

But this assumption is not correct. This was because we were believing that a statistically sound argument is equivalent to truth.

The use of every statistical test is based on some ground rules:-

* **Independence:** The events are independent to each other or not.
* **Model of reality: ** Simulation are a model of reality.

So in the last lecture when we calculated PI, we based our calculation on [Buffon Laplace Math](http://en.wikipedia.org/wiki/Buffon's_needle), then we did some algebraic calculation and then based on this algebraic calculation derived our code for estimating PI, we got our estimation of PI based on small standard deviation which was as shown below:-

````
import random

def stdDev(X):
    mean = sum(X)/float(len(X))
    total = 0.0
    for x in X:
        total += (x - mean) ** 2
    return (total/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    for needle in xrange(1,numNeedles+1,1):
        x = random.random()
        y = random.random()
        if (x * x + y * y) **0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(needle))

def estPi(precision = 0.01, numTrials = 20):
    numNeedles = 1000
    numTrials = 20
    sDev = precision
    while sDev >= (precision/4.0):
        estimates = []
        for t in range(numTrials):
            piGuess = throwNeedles(numNeedles)
            estimates.append(piGuess)
        sDev = stdDev(estimates)
        curEst = sum(estimates)/len(estimates) 
        curEst = sum(estimates)/len(estimates)
        print 'Est. = ' + str(curEst) +\
              ', Std. dev. = ' + str(sDev)\
              + ', Needles = ' + str(numNeedles)
        numNeedles *= 2
    return curEst
estPi()        
````

But suppose we did a mistake in our code where in place of in the `throwNeedles()` method, we modified this line `return 4*(inCircle/float(needle))` to `return 2*(inCircle/float(needle))`, we will get out estimation of PI as `1.56969296875`, which will be wrong.

So as per the above code, we have nothing wrong with the statistics, but still it is nowhere close to the real value of PI.

The moral of the story is:-

* Before we believe the output of the model, we should have confidence that our conceptual model is correct.
* We have correctly implemented that conceptual model in code.

How can we achieve this:-

* Test our result against reality

To test our result, we can calculate the circumference of circle based on the estimation of PI which we get, so immediately we could have identified that the value of PI is nowhere close to the actual value.

A real scientist when they derives a simulation model, that run some experiments to verify that there model is giving results which is near reality or at least plausible. Statistic identifies that we have got the minute details right but we should also do a sanity check.

## [InterPlay of Physical Reality, Theoretical and Computational ](https://www.youtube.com/watch?list=PLB2BE3D6CA77BB8F7&v=TIQTYgmavC4&feature=player_detailpage#t=277) ##

In real engineering we have to find a cohesive existence of these 3.

* **Physical System : **  A real world problem, which can be stock market or something which exist in real world.
* **Theoretical System : ** Some theory which gives some insight into the Physical system.
* **Computational System : ** When the Theoretical system becomes to complicated we use computation to solve the real world problems.

We can understand these concept we can relive our high school days, when in time for a practical exam for Physics, Chemistry or Biology. In the exam, we have studied the theory and when after doing experiments we get results which are no where close to the theory which we studied, so we know something is wrong, We have three possibility.

* Turn in the same reading which we get and stand a chance of being ridiculed about our sloppiness.
* Turn in the perfect result from the theory and chance of being caught increases.
* Do the smart thing, and make the reading close enough to the theory but have error also there.

The smart solution is the best thing to do, but to model this case, we also have to model for experimental errors.

## [Error Modeling ](https://www.youtube.com/watch?list=PLB2BE3D6CA77BB8F7&v=TIQTYgmavC4&feature=player_detailpage#t=427) ##

We can model the error which are introduced in experiments, this can be done when we know how best to model reality in addition to model error.

The best way to model experimental error, we have to assume there is some sort of perturbation, i.e. deviation from standard flow of the actual data. As per Gauss's analysis, errors are also distributed **normally**.

## [Hook's Law](https://www.youtube.com/watch?list=PLB2BE3D6CA77BB8F7&v=TIQTYgmavC4&feature=player_detailpage#t=470) ##

We can see how to model error, with the help of [Hook's Law](http://en.wikipedia.org/wiki/Hooke%27s_law)

Hook's Law states that

> Hooke's law is a principle of physics that states that the force ![](http://upload.wikimedia.org/math/8/0/0/800618943025315f869e4e1f09471012.png) needed to extend or compress a spring by some distance ![](http://upload.wikimedia.org/math/0/2/1/02129bb861061d1a052c592e2dc6b383.png) is proportional to that distance

![](http://upload.wikimedia.org/math/1/c/7/1c749d4ed8bae462c7e39d39bbecb23d.png)

![](http://upload.wikimedia.org/math/8/c/e/8ce4b16b22b58894aa86c421e8759df3.png ) is a constant factor characteristic of the spring, its stiffness. It is also called Spring Constant.

Hook's law hold for a wide variety of materials, but it does not hold for arbitrary large force. All materials have a elastic limits, and if we stretch beyond this limit, the law fails.

Spring constant tells us how stiff a materials is, like the suspension of an automobile, the spring constant value is very high.

The negative sign in the Hook's law equation means that the Force exerted is in the reverse direction of the displacement.

We can calculate the spring constant using this experiments.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Hookes-law-springs.png/220px-Hookes-law-springs.png)

So we know can do some algebra:-

````
F = -Kx ---- (1)
F = ma  ---- (2)    #mass * acceleration 

from (1) and (2)

k = (m * g)/x       # a is changed to g, which is acceleration due to gravity

````

So if we know `m` that is the mass suspended on the spring, and the `x` which is the displacement caused but the mass, we can calculate `k` because `g` is `9.81` mts per sec.

This is a straight forward calculation and we have can get the result fairly easily but the problem is we have experimental error, which is due to environments, so what we do is we put different weight and we calculated different displacement. So we will have series of weight to k points. Since the errors are evenly distributed, so if we do good enough no of experiments we can get a nice estimation of spring constant.

Calculation of spring constant 
* we have the experimental data shared at [Spring Constant ](data/springData.txt). 
* We have a algebraic equation, as show above.
* We will make a computational model based on above data.

Here is the code for computational model:-

````
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

def plotData(fileName):
    xVals,yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  #acc. due to gravity
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

plotData('../data/springData.txt')
pylab.show()    
````
Lets dissect the code mentioned above:-

* `getData()` : This is the method which reads from a file which is `../data/springData.txt` and returns the masses and distances list.
    - This methods have few interesting steps, `dataFile = open(fileName,'r')` this opens the file in a read only mode.
    - `discardHeader = dataFile.readline()` just removes the header or the first line from the text file.
    - `line.split()` splits each line with space as the separator, which gives us `d` distance and `m` mass for each iteration of experiments, which is stored in a list `distances` & `masses` that is returned as a tuple.
    - We close the file, `dataFile.close()`
* `plotData()`: uses the information from the files and plot some interesting statistics as shown below:-
    - The tuple of `distances` & `masses` is saved into `xVals` and `yVals`
    - Then this `xVals` and `yVals` is converted to a `pylab.array()` which helps us to do a lot of manipulation on each element of the array. This `pylab.array()` is built on top of `numpy.array.`
        + This array is type of list which a sequence of things.
        + This does not have apis like `append` but have some other valuable methods.
        + We can do point wise operation on an array. which we are doing when we do `xVals = xVals*9.81`
        + When multiply one array with another, we get a cross product.
        + In python, we start with a list to build up the list, because we have `append()` methods etc, and once we have the list we convert them to an `array()` so we can do maths on them.
        + These array are very different that the one's in `C` or `java`
    - Once it is converted, we do `xVals = xVals*9.81` which will multiply each item in `xVals` with `9.81` because we changed it to a `pylab.array()`
    - Then we make a plot of `xVals` and `yVals`

The plot will look like this:-

![Spring Constant ](images/springConstant_01.png)

So the big question here is **how to calculate the spring constant?**

To find the spring constant, we have to plot a line based on the above points which we get and the slope of that line will be `k`

Now you might be thinking what the hell just happened we have a simple formula why not use it, or what is this slope and how it is related.

To explain the above phenomenon, let do a little bit of maths.

We know that from the equation of Hook's law.

````
F = -kx
````

We have plotted the graph for `F` and `x`. 

Now if we see the Plot shown above and remember the Equation of straight line will be:-

````
y = mx + b

b = Y intercept, if b = 0

y = mx
````

Since from the plot we have seen that there is no Y intercept so based on the equation `y = mx` we can derive that `m =  k` , so if we can find the slope of the line we will get `k`

Now we have to get that [line](https://www.youtube.com/watch?list=PLB2BE3D6CA77BB8F7&v=TIQTYgmavC4&feature=player_detailpage#t=1209).

## Pylab.array : 16:00 ##
## Objective Function : 21:00 ##
### Least square fit: 22:41 ###
### Polyfit ###
### Liner Regression : 28:40 ###

## Co-efficient of Determination : 47:40 ##






## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-17-curve-fitting/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-17-curve-fitting/MIT6_00SCS11_lec17.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-17-curve-fitting/lec17.py)
4. [Lecture slides (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-17-curve-fitting/MIT6_00SCS11_lec17_slides.pdf)
5. [Lecture data files (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-17-curve-fitting/lec17_data.zip)


### Check Yourself ###
### What is an objective function? ###
### What method of curve fitting is used by polyfit? ###
### What does curve fitting do? ###
### What is the coefficient of determination? ###


