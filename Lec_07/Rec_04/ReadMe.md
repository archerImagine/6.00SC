# MIT 6.00SC | Recitation 04 | Recursion, Pseudo code and Debugging #

## [Recursion ](https://www.youtube.com/watch?v=7BpomdjZ_Os&feature=player_detailpage&list=PLB2BE3D6CA77BB8F7#t=32) ##

We will start from the last recitation's topic, Recursion. So as a review, can we define **what is Recursion?**

**Recursion** is a divide and conquer techniques, in which we first identify the **base case**, where we can find the answer immediately, and then we break the big problem into problem of smaller size of the same type.

The biggest question with recursion is **when to use recursion and when to use iteration?**, the reason being, the same recursive algorithm can be implemented using a iterative approach also.

So we can check the difference by using the Multiplication example, from the last time.

````
def recursiveMultiplication(m,n):
    #Base Case
    if n == 0:
        return 0
    elif n >= 1 :
        return m + recursiveMultiplication(m,n-1)
    elif n <= -1 :
        return -m + recursiveMultiplication(m,n+1)
````

And this is the iterative version:-

````
def IterativeMultiplication(m,n):
    if n == 0 or m == 0:
        return 0

    # Initialize variable to hold result
    result = 0
    if n >= 1:
        while n > 0:
            #Add m to the result n times
            result += m
            n -= 1
    elif n <= -1 :
        # n is negative, we we would increment n
        while n < 0:
            # Add -m to the result n times.
            result += -m
            n += 1

    return result

````

Now if you see the two example, it feels (which is subjective) that the iterative implementation is much simpler that the recursive implementation. But both these are subjective understanding, for some the recursive approach is simpler to understand.

So we cannot define which approach is better, it just depends on what is the understanding level of an individual over these 2 techniques. But some problems like **Fibonacci**, **factorial** are better implemented in recursive algorithm because it matches the mathematical definition to the **T**.


So check both the approaches for Fibonacci series.

**Recursive Approach**

````
def recursiveFibonacci(n):
    """
        A recursive fibonacci to find the nth fibonacci were
        n is a int > 0
    """

    # Base Case: 0th fibonacci number is either 0 or 1
    if n == 0 or n == 1:
        return 1            #there is a bug in MIT OCW code, because it should return 1 in place of return n, as fib(0) = 1
    else:
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)
        

````

Now as you can see, the mathematical equation can be directly derived.


**Iterative Approach**

````
def iteratativeFibonacci(n):
    """ An Iteratative function to find the nth Fibonacci number,
        n is an int and >= 0
    """
    if n == 0 and n == 1 :
        return n
    else:
        # Hold the currect and the previous Fibonacci number
        previousFib = 0
        currentFib = 1
        for iteration in xrange(1,n + 1):   #MIT OCW, has a bug, it should not be xrange(1,n)
            # The next Fib number will be sum of currentFib and previousFib
            nextFib = previousFib + currentFib
            # print "nextFib: ", nextFib
            # Save these value
            previousFib = currentFib
            currentFib = nextFib
            # print "iteration: ", iteration, " currentFib : ", currentFib, " previousFib: ", previousFib, "\n"
    return currentFib
````

We have to do a little more housekeeping in this case.

### [Default Parameters](https://www.youtube.com/watch?v=7BpomdjZ_Os&list=PLB2BE3D6CA77BB8F7#t=647) ###

Consider the below example:-

````
def defaultParameter(n = 100):
    print "I was called with: ", n

defaultParameter(1)     #print 1
defaultParameter()      #print 100
````

When we define a function like this `def defaultParameter(n = 100)`, what it means is that the parameter `n` has a default value of `100`, so when we do call the function `defaultParameter()` without any parameter, which is the second case, it take the default value of `100`, but if we pass with a value it is called with the value passed that is `1` in the first call.

## [Floating Point ](https://www.youtube.com/watch?v=7BpomdjZ_Os&list=PLB2BE3D6CA77BB8F7#t=945) ##

Consider the below example:-

````
ten_hundredths = 10/100.0
one_hundredths = 1/100.0
nine_hundredths = 9/100.0

if ten_hundredths == (one_hundredths + nine_hundredths):
    print "Yes, (10/100.0) equals (1/100.0 + 9/100.0)"
else :
    print "No, (10/100.0) equals (1/100.0 + 9/100.0)"
    print "10/100.0 is : ", ten_hundredths, " ... which python represents as ", \
            repr(10/100.0)
    print "(1/100.0 + 9/100.0) is : ", (1/100.0 + 9/100.0), " ... which python represents as ", \
    repr((1/100.0 + 9/100.0))

````

As discussed previously, floating point is not exact, which means we should never compare for equality. That is the reason, the above check `ten_hundredths == (one_hundredths + nine_hundredths)` fails.

We should also check the binary representation, when we want to check value using `repr`, inplace of using `print`.

As a reason, we use to check it the values close enough, which is done like this method.

````
def compare(x,y,epsilon = 0.00001):
    """ 
        Takes two floating point numbers, x and y, and determines if
        they are within epsilon of one another.

        If no value of epsilon is supplied, the default value of 0.00001,
        is used.

        Returns true if they are else false.
    """

    return abs(x - y) < epsilon
````

To know more about floating point, you can visit the below link
* [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point)

Floating may be inexact but it is consistent. So the below code works:-

````
nine_hundredths_plus_one_hundredths = nine_hundredths + one_hundredths
nine_hundredths_plus_one_hundredths -= one_hundredths

print "9/100.0 + 1/100.0 - 1/100.0 == 9/100.0", nine_hundredths_plus_one_hundredths == nine_hundredths
````

The above will be True, when adding and subtracting `one_hundredths`, we are adding and subtraction use the same precision so this is consistent.

## [Pseudo Code](https://www.youtube.com/watch?v=7BpomdjZ_Os&list=PLB2BE3D6CA77BB8F7#t=1539) ##

**Pseudo Code**, is a way of representation of code into a language of human understanding. Pseudo code is that as human we do not think in computer language, so pseudo code helps in understanding and solving a problem.

## [Debugging ](https://www.youtube.com/watch?v=7BpomdjZ_Os&list=PLB2BE3D6CA77BB8F7#t=2585) ##

A major debugging technique is to write test case, and running them as an when we are making changes to the code.






