# MIT 6.00SC | Optional Recitation | Algorithm Complexity and Class Review #

To get a clear picture of this Recitation, kindly read the [Recitation handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/MIT6_00SCS11_rec04.pdf).

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

## [Constant Time Examples](https://www.youtube.com/watch?v=8I0BmT1ccuw&list=PLB2BE3D6CA77BB8F7#t=748) ##

Consider the below example:-


````
def inc(x):
    return x+1
````

even this is constant time:-

````
    def bar(x, y):
        z = x + y
        w = x * y
        q = (w**z) % 870
        return 9*q
````

## [Linear Time ](https://www.youtube.com/watch?v=8I0BmT1ccuw&list=PLB2BE3D6CA77BB8F7#t=784) ##

Here is an example of linear time code:-

````
    def mul2(x, y):
    result = 0
        for i in range(y):
        result += x
    return result
````

The `for` loop in the above code is an indication that it will be atleast `O(n)`

Not always, the operation inside a `for` loop is constant time, consider this example:-

````
    def count_same_ltrs(a_str, b_str):
    count = 0
        for char in a_str:
            if char in b_str:
            count += 1
    return count
````

The above is not linear, because the `if` condition also have to traverse the `b_str`, so this is `O(n^2)`


## [Recursion ](https://www.youtube.com/watch?v=8I0BmT1ccuw&list=PLB2BE3D6CA77BB8F7#t=1555) ##

Consider the below example for recursion in factorial program.

````
    def r_factorial(n):
        if n <= 0:
            return 1
        else:
            return n*r_factorial(n-1)
````

To find the complexity of a recursive function you have to find out the number of recursive call it will make. So for the above example it will make `n` calls. So this will be Linear.

Now consider this example:-

````
    def foo(n):
        if n <= 1:
            return 1
        return foo(n/2) + 1
````

So solve this we need to find this

````
n/2^n = 1
n = 2^k
k = log n
````

So this is `O(Log N)`

## [Factorial ](https://www.youtube.com/watch?v=8I0BmT1ccuw&list=PLB2BE3D6CA77BB8F7#t=1816) ##

For a factorial, we might consider that it is linear because of this equation:-

````
fib(n) = fib(n - 1) + fib(n -2)
````

But it is not, if we draw the call structure, we will see a tree. As shown below:-

![Fibonacci ](http://www.math.ucla.edu/~wittman/10a.1.10w/ccc/ch14/images/fib_tree.png)

So as you can see, the depth of the tree is n, and at each level we have a branching factor of 2, so a loose calculation will give a complexity of `O(n^2)`

## References ##
### Links ###

1. [Recitation handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/MIT6_00SCS11_rec04.pdf)
2. [Python | Time Complexity ](http://wiki.python.org/moin/TimeComplexity)
3. [Wiki | Big O Notation ](http://en.wikipedia.org/wiki/Big_O_notation)