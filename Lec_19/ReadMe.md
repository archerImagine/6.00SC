# MIT 6.00SC | Lecture 19 | More Optimization and Clustering #

## [Introduction ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=21) ##

In the last lecture we discussed about Knapsack problems, the two division of Knapsack problem.

* 0/1 Knapsack problem
* Continuous Knapsack problem.

We also saw that we can solve Continuous Knapsack problem using a Greedy Algorithm optimally.

Greedy also solves the 0/1 Knapsack problem quickly, but we should be careful with the use of solve, because it may not be an optimal solution.

So lets see an example of a Brute Force Greedy algorithm which will solve the Continuous Knapsack problems.

````
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def dToB(n,numDigits):
    """
        requires : n is a natural number less than 2 ** numDigits 
        return : a binary string of length numDigits representing the
                decial number n 
    """
    assert type(n) == int and type(numDigits) == int and \
    n >= 0 and n < 2 ** numDigits
    bStr = ""
    while n > 0:
        bStr = (str(n%2)) + bStr
        n = n/2
    while numDigits - len(bStr) > 0:
        bStr = '0'+bStr
    return bStr

def getPset(Items):
    """ Generate a list of list representing the power set of Items """    
    numSubSet = 2 ** len(Items)
    templates = []
    for i in range(numSubSet):
        templates.append(dToB(i,len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset

def chooseBet(pset,constarints,getVal,getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)    
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constarints and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet,bestVal)

def testBet():
    Items = buildItems()
    pset = getPset(Items)
    taken,val = chooseBet(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item


testBet()

````

The output of the program is:-

````
Total value of items taken = 275.0
   <clock, 175.0, 10.0>
   <painting, 90.0, 9.0>
   <book, 10.0, 1.0>
````

So we have found a better solution than the 0/1 knapsack problem.

Lets dissect the above code for trivial understanding.

* `dToB() :` Converts a decimal number `n` to a binary number with length `numDigits`. The need of `numDigits` is to identify which position item is taken and which is not, if we do not pass this, it will just inform us which item is taken but will give no information for the item not taken.
* `getPset() :` Generates a Power Set of the items,  A power set is the set of of all subset of a given set. kindly check the [wiki for details.](http://en.wikipedia.org/wiki/Power_set) The total items in a power set will be `2^n`. This function will make a super set of all the item one can take without the constraint of whether it meets the constraints or not.
* `chooseBet() :` It takes the previous power set, the constraints, and two function, one `getVal`, and `getWeight` as input. With this these as the inputs, we iterate over the power set and choose the set with optimal answer.

This brute force algorithm finds a better answer than the Greedy algorithms because this algorithm is focused on the globally optimized solution than the locally optimized solution.

Now the one question which should answer is **The brute force algorithm is not good to solve because we used a very stupid algorithm?**

The answer to this question is that, It is a stupid algorithm but it also falls under the group of algorithm which we call **Inherently Exponential.** What this means is, what ever means we use, we can never find an algorithm which can solve this in sub-exponential time.

There are technique which can provide fast result for a **Inherently Exponential.** problem which will be discussed later.

## [Machine Learning ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=624)##

**Definition : ** 

* Superficially Machine learning deals with question of **how to build programs which learns?**
    - Every program tends to learn something.
* [Wikipedia ](http://en.wikipedia.org/wiki/Machine_learning) define it as

> Machine learning is a scientific discipline that explores the construction and study of algorithms that can learn from data.

In layman's term Machine learning means to identify patterns in a set of data, and based on these patterns make informed decision. 

This whole process is called [Inductive Inference. ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=780)

### Inductive Inference : 12:45 ###

The basic idea is that the program observes examples that represent incomplete statistics phenomenon and tries to generate a model that summarizes sum statistical property of the data and can be used to predict the future.

This process is shown below:-

![](http://www2.cs.uregina.ca/~dbd/cs831/notes/ml/overview.gif)

There are 2 distinctive approaches to machine learning:-

1. **Supervised Learning**
2. **Unsupervised Learning**

### [Supervised Learning ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=859)###

In Supervised learning, we associate a label with each example in a training set. 

If the label is discrete we call it a **classification problem.**

If the labels are real valued it is a **Regression problem**.

To understand supervised learning, kindly see the image in the lecture [pdf](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/MIT6_00SCS11_lec19_slides.pdf)

In the first page we have a image with X, and Y values, and few dots which are labeled with blue or red color. So we want to learn, given X and Y values, what makes a circle red or blue.

To make this classification I need to answer few questions about it:-

* **Are the labels accurate**: In real world we will never get a data where the labels are always accurate.
* **Is the past the representation of the future?** : Mostly it is not,
* **Do you have enough data to generalize?** : If we have less data, then we should have very minimal confidence in our learning.
* **Feature Abstraction?** : The learning we want to devise should be directly correlation to the feature available in the training set.
* **How tight should the fit be?**

Lets see the page 2 of the lecture  [pdf](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/MIT6_00SCS11_lec19_slides.pdf)

There are 2 different ways we can generalize from the data. When we are looking into classification problem in supervised learning, we are looking as ways to divide our training data.

If we look into the 2nd page of the lecture slide we will see that the triangle is a very good classification, as there we always want to **minimize the training error.**

If we use the liner vertical separator we have some training error. So does this means that the triangle is better than the liner separator. Not necessarily because the goal is to predict future label. So the liner separator might be a better classification provided the singular red circle may be a outliers.

This is analogous to the over fitting of training data which may not yield correct prediction.

### [Unsupervised Learning ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=1375) ###

In Unsupervised learning, we have training data, but we do not have labels. So in the first page of the lecture pdf we only have point, not label of blue and red.

In unsupervised learning, we learn about **regularities of data**.

The dominant way of learning in unsupervised learning is **Clustering**.

## [Clustering ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=1494) ##

Since we do not have label in the data, we want to find grouping in the data, which we can call Clustering.

This can be seen in the 3rd page of the lecture [pdf](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/MIT6_00SCS11_lec19_slides.pdf)

Clustering is the process of organizing objects into groups whose member are similar in some way. The problem we face is what is the metrics to be used for identify something as similar.

So in the 3rd page of lecture [pdf](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/MIT6_00SCS11_lec19_slides.pdf) we can group people in these manner.

* if we say that if heights are same then the people are similar, then we will have 2 groups, one of shorter people and another of taller people.
* If we want to group w.r.t. weight, we will say we want thinner people and fatter people, so the divisor will be parallel to Y-Axis.
* if we want some combination of height and weight, we might get 4 clusters.

Clustering is a great optimization problem, so we can ask, **What property does a good clustering have?**

* It should have low intra cluster dissimilarity. All of the points in the same cluster should be similar.
* It should have high inter cluster dissimilarity. All of the points outside the cluster should be dissimilar.

We will use Variance for finding dissimilarity.


### [Variance](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=1825) ###

As describe in [Wiki](http://en.wikipedia.org/wiki/Variance)

> In probability theory and statistics, variance measures how far a set of numbers is spread out. A variance of zero indicates that all the values are identical. Variance is always non-negative: a small variance indicates that the data points tend to be very close to the mean (expected value) and hence to each other, while a high variance indicates that the data points are very spread out around the mean and from each other.

Based on above description can we say, IF the variance is low in a cluster, and the intra/inter cluster dissimilarity is minimal we have a good cluster.

We cannot say this, because we can have a cluster with just one element, where the above point will suffice. So the objective function is great, but we are missing the set of constraints.

Some constraints might be:-

* Maximum number of clusters.
* Maximum distance between clusters.

So solving the Clustering optimization is very difficult to solve so we use Greedy Algorithms to solve them. Two most common greedy algorithms are:-

* K-Mean Clustering 
* Hierarchical Clustering


### [Hierarchical Clustering ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=2130) ###

Consider this problem we have `N` items, with corresponding `N * N` distance matrix.

We have to find a Hierarchical cluster for the same, the distance metrics is given in lecture [pdf](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/MIT6_00SCS11_lec19_slides.pdf) page 4.

Here are the steps to follow for Hierarchical cluster:-

* Assign each item to its own cluster. If we have `n` items we will have `n` cluster.
* Find most similar pair of clusters and merge them.
* Continue the process, till all item in same cluster.

This type of cluster is called **Agglomerative**, This is a "bottom up" approach: each observation starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.

There is just one problem, which is the complication on step 2, Which to find a mean to find similar cluster.

We can use different metrics to get different properties.

These are typically called **Linkage Criteria.**

## [Linkage Criteria ](https://youtu.be/miw2CiKp1r0?list=PLB2BE3D6CA77BB8F7&t=2404) ##

Few of the linkage Criteria are:-

* single-linkage clustering : Shortest distance between any pair.
* complete linkage clustering : Furthest distance between any pair.
* average linkage clustering : 

The problem with this Clustering is it is `n^2` complexity and it does not scale nicely and there is a possibility that it will not find optimal clusters.

We might need a Feature vector, to find similarity between clusters.

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/MIT6_00SCS11_lec19.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-19-more-optimization-and-clustering/lec19.py)


### Check Yourself ###
### What is machine learning? ###
### What is inductive inference? ###
### What is supervised learning? ###
### What is unsupervised learning used for? ###
### What is clustering? ###
### What is agglomerative clustering? ###


