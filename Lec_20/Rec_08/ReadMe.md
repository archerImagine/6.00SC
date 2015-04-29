# MIT 6.00SC | Recitation 08 | Hierarchical and k-means Clustering #

## Clustering ##

Two types of Clustering are discussed till now.

1. Hierarchical Clustering
2. K-Means Clustering

### [Hierarchical Clustering ](https://youtu.be/UHRhUufAlE4?list=PLB2BE3D6CA77BB8F7&t=103) ###

As already discussed in Lecture 19:-

Here are the steps to follow for Hierarchical cluster:-

* Assign each item to its own cluster. If we have `n` items we will have `n` cluster.
* Find most similar pair of clusters and merge them.
* Continue the process, till all item in same cluster. 

Most of the Recitation is spend in understanding the Code which we saw for Hierarchical clustering in Lecture 20.

The only important concept discussed here is

### [Yield](https://youtu.be/UHRhUufAlE4?list=PLB2BE3D6CA77BB8F7&t=608) ###

We have already seen what an `yield ` is in [lecture 12](../../Lec_12/ReadMe.md). So as a recap let us review again.

To understand better we should understand the difference between `range` and `xrange`.

Lets see this example:-

````
num = range(1,10)
print "type(num): ", type(num)
print "num: ", num

xnum = xrange(1,10)
print "type(xnum): ", type(xnum)
print "xnum: ", xnum

def myXrange(maxValue):
    i = 0
    while i < maxValue:
        yield i
        print "Inside Function: ", i
        i += 1

myNum = myXrange(10)
print "type(myNum): ", type(myNum)
print "myNum: ", myNum

for x in myXrange(10):
    print "OutSide Function: ", x

````

The output of this code is:-

````
type(num):  <type 'list'>
num:  [1, 2, 3, 4, 5, 6, 7, 8, 9]
type(xnum):  <type 'xrange'>
xnum:  xrange(1, 10)
type(myNum):  <type 'generator'>
myNum:  <generator object myXrange at 0x018340D0>
OutSide Function:  0
Inside Function:  0
OutSide Function:  1
Inside Function:  1
OutSide Function:  2
Inside Function:  2
OutSide Function:  3
Inside Function:  3
OutSide Function:  4
Inside Function:  4
OutSide Function:  5
Inside Function:  5
OutSide Function:  6
Inside Function:  6
OutSide Function:  7
Inside Function:  7
OutSide Function:  8
Inside Function:  8
OutSide Function:  9
Inside Function:  9
````

Lets dissect the above code, the first this which strike is.

* `type(num)`: is ` <type 'list'>`, so it returns a list of numbers, so that means all the numbers are pre-computed and then returned.
* `type(xNum)` is `<type 'xrange'>`, which is nothing but a type of `generator `. Which becomes much clear when we see the next method which is `myXrange()`
* `type(myNum)` is `<type 'generator'>`, so as we can see, it is not returning the complete list of values, but it remembers the last point of execution and then computes again when next value is to be returned. This saves a lot of memory.

Hierarchical clustering got it name because with each merge we are creating a Tree like structure, which can represent a Hierarchy.

### [K-Means Clustering](https://youtu.be/UHRhUufAlE4?list=PLB2BE3D6CA77BB8F7&t=1289) ###

We have already discussed it in the [Lecture 20](../ReadMe.md)

The benefit of K-Means is that it is faster and will end faster for large data points, but not the case of Hierarchical Clustering.

But the draw back is K-Means is based on the physiology of Random points, so it means it is not deterministic, i.e. for multiple iteration it will not give me same results but for Hierarchical clustering is deterministic.

Since we have a non-deterministic we do the following steps to avoid the error, or getting a wrong clusters.

* Run the test multiple times.
* Run the K-means Cluster algorithm on some sample data, and then calculate the **R-Squared** error of the same, the iteration which gives the least **R-Squared** error will the be the the near correct no of clusters.
