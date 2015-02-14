# MIT 6.00SC | Lecture 15 | Statistical Thinking #

## [Introduction ](https://www.youtube.com/watch?v=VqZBqoZgL7k&list=PLB2BE3D6CA77BB8F7#t=85) ##

At the end of lecture 14, we were flipping coin, and trying to find number of sample which is enough to safely say that the probability of getting a head or tails after n trails is 0.5.

So to solve this, we can flip a coin just 2 times and get head and tails, now with this we will have the probability of 0.5 which is the correct answer, but the sample size is not good enough, because if we flipped it twice and got heads both the times, we cannot assume the probability is 1 for getting heads.

So the important question which we will answer in this lecture is **How many samples do we need to believe the answer?**

Fortunately there is a very solid set of mathematics which will help us get to this answer.

## [Variance ](https://www.youtube.com/watch?v=VqZBqoZgL7k&list=PLB2BE3D6CA77BB8F7#t=205) ##

Variance is at the root of the answer to the above question. So **variance** is a measure of how much spread there is in the possible outcomes.

So to use variance, we should have different outcomes, which is we want to run multiple trials, which is why we need to run multiple trials rather than 1 trails with multiple flips in case of coin.

The question which we should think of is, why we should do a million trails of coin flips rather than 1 trails with a million flips? The reason for doing a million trails is for each trails we will get a outcome which gives us a fair idea of the spread of outcome i.e. variance.


We can formalize the concept of Variance, which is called **Standard Deviation**.

## [Standard Deviation ](https://www.youtube.com/watch?v=VqZBqoZgL7k&list=PLB2BE3D6CA77BB8F7#t=329) ##

The fraction of values which are close to the mean.

As quoted in [wikipedia ](http://en.wikipedia.org/wiki/Standard_deviation).

>  A low standard deviation indicates that the data points tend to be very close to the mean (also called the expected value) of the set, while a high standard deviation indicates that the data points are spread out over a wider range of values.

If all values are the same, the standard deviation is `0`.

Here is the mathematical formula for standard deviation:-

![Standard Deviation ](http://geographyfieldwork.com/standa5.gif)

and the code to calculate standard deviation will be:- 

````
def stdDev(X):
    mean = sum(X)/float(len(X))
    total = 0.0
    for x in X:
        total += (x - mean)**2
    return (total/len(X)) ** 0.5
````

So see the steps to find standard deviation kindly see this link, [Standard Deviation Formulas](http://www.mathsisfun.com/data/standard-deviation-formulas.html)

We have now understood what a standard deviation is, now what is the use of it?

Standard deviation will be used to look at the relationship between the number of samples we have looked at and how much confidence we should have in the answer.

### Co-efficient of variation : 17:40 ###

![Co-efficient of variation](https://www.resna.org/sites/default/files/legacy/conference/proceedings/2010/Wheeled%20Mobility/Student%20Papers/ChaconA/Equation%205.png)

### Normal Distribution ###

### Standard Error : 41:19 ###

![Standard Error ](http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Confidence_Intervals/CI_prop_SE.png)

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-15-statistical-thinking/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-15-statistical-thinking/MIT6_00SCS11_lec15.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-15-statistical-thinking/lec15.py)



### Check Yourself ###
### What does the standard deviation tell us? ###
### What is variance? ###
### What is the coefficient of variation? ###


