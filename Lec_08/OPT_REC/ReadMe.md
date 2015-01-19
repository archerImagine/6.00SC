# MIT 6.00SC | Optional Recitation | Algorithm Complexity and Class Review #

TO get a clear picture of this Recitation, kindly read the [Recitation handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/MIT6_00SCS11_rec04.pdf).

The first question to ask ourself is **What is Big-O notation?**

Big-O notation gives us a upper bound on how long somethings will execute. The important thing to remember is that this is not time bound. So Big-O does not take how long a program will execute, it tells **how many steps** it will take to execute a program.

Big-O notation cannot predict accurately for small inputs, but for a very large input how the algorithm performs is what we are interested in.

Consider this scenario. We have 2 Algorithms and their Big-Oh representation.

````
A1 : O(n)
A2 : O(n^2)

A2/A1 : O(n^2)/O(n)
        : O(n^2)

````

So as we can see in the above case, irrespective of which computer you are running these algorithms, `A2` will always be slower that `A1` by `n^2` times.

## Some Common Big-O Notations ##

* O(1) : **Constant Time**,  What this means is, it does not depends on the size of the input, so O(1) = O(100) = O(2^100). The reason being, it will not change based on the input.
* O(log n): **Logarithmic Time**, Any base log is same Big-O because the variation is minimal. This is the fastest time bound for Search.
* O(n) : **Linear Time**, This means we have to look at each input at least once.
* O(n log n) : This is the fastest time bound for Sorting.
* O(n^2) :  **Quadratic Time**, This is the complexity when we consider inner loops.
* O (2^n) : **Exponential Time**, This is really big.

Always remember:-

````
O(n^k) < O(k^n)
Polynomial Time < Exponential Time
````

### Some Questions ###

1. Does O(100 n^2) = O(n^2)
2. Does O(1/4 n^3) = O(n^3)
3. Does O(n) + O(n) = O(n) 

All the above are *True*, because Big -O is bothered with the higher power.

12:00


## References ##
### Links ###

1. [Recitation handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/MIT6_00SCS11_rec04.pdf)
2. [Python | Time Complexity ](http://wiki.python.org/moin/TimeComplexity)
3. [Wiki | Big O Notation ](http://en.wikipedia.org/wiki/Big_O_notation)