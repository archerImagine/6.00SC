# MIT 6.00SC | Lecture 18 | Optimization Problems and Algorithms #

## [Co-efficient of determination ](https://www.youtube.com/watch?v=BRjwkgQct28&list=PLB2BE3D6CA77BB8F7&t=34) ##

**Co-efficient of determination** is used to find out the goodness of a fit, i.e. How nicely a data fits to a statistical model, usually it is called **RSquared**.

The formula for Co-efficient of determination is represented by:-

![](http://upload.wikimedia.org/math/4/2/5/4253e227d95c290764b310c57ff34625.png)

Where:-

* ![](http://upload.wikimedia.org/math/6/7/9/67976e7df3f8a29ef9867a4a35e5c4db.png)
* ![](http://upload.wikimedia.org/math/d/6/b/d6b7e64a7c677ae32bc62d675107dac8.png)
* A data set has n values marked `y1...yn` (collectively known as `yi`), each associated with a predicted (or modeled) value `f1...fn` (known as `fi`, or sometimes `yi`).

As we can derive from the formula above:-

* **RSquared** always lies between `0` and `1`.
* If **RSquared** equals `1`, that means the model can successfully predict change in possible data.
* If **RSquared** equals `0`, that means the model can never predict all possible data. i.e. The model is not able to predict any data.

Here is the code, to find the **RSquared**:-

````
import pylab

def rSquare(measured,estimated):
    """
        measured: one dimensional array of measured values
        estimated: one dimensional array of predicted values
    """
    EE = ((estimated - measured) ** 2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured) ** 2).sum()
    return 1 - EE/MV

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

def tryFits(fName):
    distances,heights = getTrajectoryData(fName)
    distances = pylab.array(distances)*36
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    meanHeights = totHeights/float(len(heights))
    pylab.plot(distances, meanHeights, 'bo')
    a,b = pylab.polyfit(distances, meanHeights, 1)
    altitudes = a*distances + b
    pylab.plot(distances, altitudes, 'r',
               label = 'Linear Fit' + ', R2 = '
               + str(round(rSquare(meanHeights, altitudes), 4)))
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) + b*distances + c
    pylab.plot(distances, altitudes, 'g',
               label = 'Quadratic Fit' + ', R2 = '
               + str(round(rSquare(meanHeights, altitudes), 4)))
    pylab.legend()

tryFits('../data/lec18_launcher.txt')
pylab.show()    
````

The output graph look like this:-

![](images/rSquare_01.png)

If we analyze the graph closely we find that:-

1. The linear fit represented the line fitting the data, has an rSquared value of `0.0177`, practically meaning, it does not explain any data in the model.
2. Where as in the Quadratic fit, we have an rSuared value of `0.9858`, determining that all the changes in the `y` value is modeled by the model.

Now since we have successfully modeled the data, what is the purpose of making this model.

An important reason for creating a model is to answer question of actual physical situation. So in the above question on important real world question which we should be able to answer is **How fast is the arrow traveling? **

To find the answer to the above question we have to understand the interplay between models, computation and theory.

## Optimization : 17:13 ##
### Problem Reduction : 20:59 ###

## KnapSack Problem: 22:35 ##




## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/MIT6_00SCS11_lec18.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/lec18.py)
4. [Lecture slides (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/MIT6_00SCS11_lec18_slides.pdf)
5. [Launcher data file (TXT)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/lec18_launcher.txt)

### Problem Sets ###

1. Problem Set 8: Simulating The Spread of Disease and Virus Population (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/MIT6_00SCS11_ps8.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/ps8.zip)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms/ps8_sol.zip)
2. Problem Set 9 (Assigned)
    1. [Problem Set 9 Due on Lecture 20](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-20-more-clustering)


### Check Yourself ###
### What does an optimization problem consist of? ###
### What is problem reduction? ###
