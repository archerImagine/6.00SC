# MIT 6.00SC | Lecture 16 | Using Randomness to Solve Non-random Problems  #

## Computational Models ##

We have seen some models of real world in past lecture, Gaussian or Normal Distribution is a great way to represent real world models with the help of Mean and Standard deviation.

A Normal Distribution can be fully characterized by its **mean** and **standard deviation.** This concept of characterization of a curve based on some parameters help in fully modeling real world system.

Most of time we would like to make a computational models based on normal distribution, because of how nicely it can be characterized and how it informs how closely it lies to the mean.

We have to take care if some thing is not normally distributed and we try to model it that way, we can get misleading results. Not all distribution are normal.

Ex:-

Consider rolling a single dice, each of the six outcome is equally probable, which means we cannot represent it as a normal distribution.

Similarly any fair lottery where the probability of each number coming is equally probable.

So for both of the above case we will have a flat line representing the distribution.

These distribution are called **Uniform Distribution**.

## [Uniform Distribution](https://www.youtube.com/watch?v=Q148jV9ljPM&list=PLB2BE3D6CA77BB8F7#t=164) ##

In a uniform distribution, each result is equally probable. It can be fully characterized by a single parameter its **range**.

Uniform distribution mostly occur in games devised by humans but never in nature, and it is not useful to model complex systems.

## [Exponential Distribution ](https://www.youtube.com/watch?v=Q148jV9ljPM&list=PLB2BE3D6CA77BB8F7#t=243) ##

Other distribution which occur very frequently in nature is **Exponential Distribution**.

The key thing about them is that these are memory less and there are the only continuous distribution which are memory less.

Consider the example, where we check the concentration of a drug in human body.

Assume at time `t` a molecule has a probability `p` of been cleared of drug in human body. The system is memory less which means the probability of a molecule been cleared at any step is irrelevant to what happened before that step.

So at time `t = 1` what is the probability of a molecule been still there in the body is: `1 - p`.

What is the probability of the molecule still there at time `t = 2`: `(1-p)^2` because these are independent events.

Generally, the molecule is still there at time `t = t` is `(1-p)^t`

Consider a problem where at time `t=0` there are `n` molecule so how many molecule will be present at time `t = t`?

See the below code to look into this:-

```
import pylab

def clear(n,clearProb,steps):
    numRemaning = [n]
    for t in range(steps):
        numRemaning.append(n * ((1 - clearProb) ** t))
    pylab.plot(numRemaning, label = 'Exponential Decay')

clear(1000,0.01,500)    
pylab.semilogy()
pylab.show()
```

The above code will give us a figure like this:-

![clear semi log y](images/clearSemilogY.png)

So we get a straight line in the graph, the reason being we are using a `semilogy` as the Y axis.

If we remove the `semilogy` we will get a curve as shown below.

![Clear Linear](images/clearLinear.png)

So if we see the graph, it looks like a exponential decay, which drop sharply and then asymptotes towards 0 but it never quite gets there in a continuous model, In a discrete model we might reach 0 because the last molecule will get cleared or not.

So if we plot a exponential curve on a log axis we will get a straight line.

## Monty Hall 22:00 ##

## Pi Estimation 34:00 ##


## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-16-using-randomness-to-solve-non-random-problems/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-16-using-randomness-to-solve-non-random-problems/MIT6_00SCS11_lec16.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-16-using-randomness-to-solve-non-random-problems/lec16.py)

### Problem Sets ###

1. Problem Set 7: Simulating The Spread of Disease and Virus Population (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-16-using-randomness-to-solve-non-random-problems/MIT6_00SCS11_ps7.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-16-using-randomness-to-solve-non-random-problems/ps7.py)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-16-using-randomness-to-solve-non-random-problems/ps7_sol.zip)
2. Problem Set 8 (Assigned)
    1. [Problem Set 5 Due on Lecture 18](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-18-optimization-problems-and-algorithms)


### Further Study ###

1. **Readings**
    1. [Monte Carlo method ](http://en.wikipedia.org/wiki/Monte_Carlo_method)
    2. [Matplotlib ](http://matplotlib.sourceforge.net/)


### Check Yourself ###
### What is a Gaussian distribution? ###
### What is a uniform distribution? ###
### What is important about an exponential distribution? ###


