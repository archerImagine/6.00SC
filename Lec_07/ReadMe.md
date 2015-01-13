# Lecture 07 | Debugging #

## Introduction ##

In this lecture we will main cover these topics:- 

* **Floating Point Numbers**
* **Debugging**

## [Floating Point Numbers](https://www.youtube.com/watch?v=5gt2WDBl8-0&list=PLB2BE3D6CA77BB8F7#t=113) ##

To start understanding of Floating point numbers, we should all understand how a number is represented in computers, i.e. Binary Numbers.

The understanding of Binary numbers is crucial for Floating point numbers.

### Binary Numbers ###

We are all familiar with the decimal number system, as a number in decimal number system is represented by digits from 0,1,2,3,4,5,6,7,8,9. The numbers are formed by a combination of `10^x`, were `10` is the base for decimal number as we have `10` digits in it, and `x` is the location of the digit in the number.

So a number `302` can be represented in decimal using

````
302 = 3 * 10^2 + 0 * 10^1 + 2 * 10^0
````

For more information on decimal number system visit this wikipedia link.

* [Decimal Number System ](http://en.wikipedia.org/wiki/Decimal)


A Binary Number system is also similar, as it has only two digits to represent number `0` and `1`, and in the same manner as decimal a binary number is formed by a sequence of `0`s and `1`s.

So a number `101` can be represented in binary as:- 

````
101 = 1*2^2 + 0 * 2^1 + 1 * 2^0 
    = 4 + 0 + 1
    = 5
````

If we have `n` digit in a sequence we can form these many numbers with it.

Decimal  10 ^ n
Binary   2 ^ n


The reason for computers to use base 2 or binary representation is because we can make switches with two states on and off.

The representation of human is decimal, i.e. we think of numbers in base 10, but computers do it in base 2, this difference causes confusion mainly for fractional numbers.

Consider the below example:-

**Representation of 0.125 in decimal:-**
````
0.125 = 1 * 10^-1 + 2 * 10^-2 + 5 * 10^-3
````

**Representation of 0.125 in binary:-**
````
0.125 = 1/8
      = 1/2^3
      = 1/10^3
      = 0.001
````

**Representation of 0.1 in decimal:-**
````
0.1 = 1 * 10^-1
````

**Representation of 0.1 in binary:-**
````
0.1 = 1/10
    = very lomg infinite number
````

Since `0.1` is infinity, it cannot be represented in a computer, so what a computer does is truncates the number of digit for representation, so this representation is what creates most of the confusion.

So in python if we there is a caveat to the representation:-

````
print (0.1)     #prints 0.1
repr (0.1)      #prints '0.10000000000000001'
````

So it is always better to print with `repr` for decimal number to find the exact representation of a number.

Most of the time this difference in representation of fractional decimal number in binary does not create a problem, but consider the below example:-

````
x = 0.0
numIter = 100000

for i in range(numIter):
    x += 0.1

print "x: " , x                 #Prints 10000.0
print "repr(x): ", repr(x)      #prints 10000.000000018848
print 10.0 * x == numIter       #prints false
print "repr(10.0 * x): ", repr(10.0 * x)    

````

As you can see, this line `print 10.0 * x == numIter` prints `false`, because the binary representation is different, so checking for equality in a decimal fraction creates problem. A better way of checking will be like this.


````
x = 0.0

numIter = 100000

for i in range(numIter):
    x += 0.1

print "x: " , x
print "repr(x): ", repr(x)
print 10.0 * x == numIter
print "repr(10.0 * x): ", repr(10.0 * x)


# Do this to check equality of floating Point.
def close(x,y,epsilon=0.00001):
    return abs(x-y) < epsilon


if close(10.0 * x, numIter):
        print "Good Enough" 
````

We we check for `abs(x-y) < epsilon` some threshold value `epsilon`, then we can assume that my calculation is close enough.


## [Debugging ](https://www.youtube.com/watch?v=5gt2WDBl8-0&list=PLB2BE3D6CA77BB8F7#t=1437) ##

Some Myths about debugging:-

* Bugs crawl unbidden in our programs - Completely wrong
* Bugs do not bread in programs - Bug are there, we never found out.

So what is the Goal of debugging is:-

* Not to eliminate 1 bug quickly.
* It is to move towards bug free program.

We cannot debug instinctively. The skill involved in becoming better in debugging is:-

* Think systematically and efficiently.

There are tools like **debuggers** are present to help in this task, but tools are rarely import, it is the skills of the craftsmen that matters. The best debugging habit it `print` statement. So add effective print statement which can help.

In place of asking why the program is giving me a wrong answer, the correct
question should be How this program gave the output which it is giving.

For debugging :-

* Studying available data.

In a computer program available data are:-

* The program code.
* Test Results.
* Logs for the program.

After studying the available date.

* Form a hypothesis.

And then

* Design and run a repeatable experiment.

Why are we looking for **repeatable** experiment, the reason being a lot of bugs are because of randomness of a program.

So lets start with a program to learn all the above technique.

````
def isPal(x):
    """ requires x to be a list,
        return True if the list is a palindrome, False otherwise """
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """ requires: n is an int > 0
        Gets n input from user
        Prints Yes, if the input is a palindrome; No otherwise"""
    assert type(n) == int and n > 0
    for i in range(n):
        result = []
        elem = raw_input("Enter Something: ")
        result.append(elem)
    if isPal(result):
        print 'Is a palindrome'
    else:
        print "Is not a palindrome"


silly(5)        
````

The output of the above program is:-

````
Enter Something: 1
Enter Something: 1
Enter Something: 1
Enter Something: 1
Enter Something: 1
Is not a palindrome
````

As we can see, though `1111` is a palindrome, it is printing not a palindrome.


The **first thing** which should do is to find **smaller set of inputs which will reproduce the bug**, the reason for this is:-

* if it is small input, it means lesser execution time.
* with smaller input it will be easier to debug


So if we invoke the above program with `silly(2)`, we get the desired bug, so now we have to look into a lesser input.


Now  the **Second thing** which we should see is to check in the code, and with binary search decide a mid point of the code where the bug could be present.

Here is the modified code with those print.

````
def isPal(x):
    """ requires x to be a list,
        return True if the list is a palindrome, False otherwise """
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """ requires: n is an int > 0
        Gets n input from user
        Prints Yes, if the input is a palindrome; No otherwise"""
    assert type(n) == int and n > 0
    for i in range(n):
        result = []
        elem = raw_input("Enter Something: ")
        print "result: ", result        #Line Added
        result.append(elem)
    if isPal(result):
        print 'Is a palindrome'
    else:
        print "Is not a palindrome"


silly(2)        

````

The output in this case is:-

````
Enter Something: a
result:  []
Enter Something: b
result:  []
Is a palindrome
````

Now this is not what is expected out of the code, because `result` does not have `a` and `b` at the end of the execution. 

So if we look closely we find that the `result` variable is initialized inside the `for` loop, so it is always empty, there is no append happening to the list `result`.


So we modify the code according to the hypothesis formed.

````
def isPal(x):
    """ requires x to be a list,
        return True if the list is a palindrome, False otherwise """
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """ requires: n is an int > 0
        Gets n input from user
        Prints Yes, if the input is a palindrome; No otherwise"""
    assert type(n) == int and n > 0
    result = []
    for i in range(n):
        elem = raw_input("Enter Something: ")
        print "result: ", result
        result.append(elem)
    if isPal(result):
        print 'Is a palindrome'
    else:
        print "Is not a palindrome"


silly(2)        
````

This gives us the output:-

````
Enter Something: a
result:  []
Enter Something: b
result:  ['a']
Is a palindrome
````

So the result is expected, but still the final output is wrong.

The moral here is, that there is no such thing as **The Bug**. 

So now we know that `silly` is behaving as expected, so the problem is below our print, which a call to `isPal`, we will use the concept of `TestDriver` to verify the function `isPal`, and here is the code for that.

````
def isPal(x):
    """ requires x to be a list,
        return True if the list is a palindrome, False otherwise """
    assert type(x) == list
    temp = x
    temp.reverse
    print "temp: ", temp
    print "x: ", x
    if temp == x:
        return True
    else:
        return False

def isPalTest():
    L = ['a','b']
    result = isPal(L)

    print "Should print False, ", result

    L = ['a','b','a']
    result = isPal(L)
    print "Should print True, ", result


isPalTest() 
````


So the good thing about the above code is the method `isPalTest` method, which actually test the function `isPal`, this is a great thing to do, and most of the time our test code is more than the actual code written.

The output of the above program is 

````
temp:  ['a', 'b']
x:  ['a', 'b']
Should print False,  True
temp:  ['a', 'b', 'a']
x:  ['a', 'b', 'a']
Should print True,  True
````

So we can see that, it is working once but not working the other time, so there is some problem. Actually we see that `temp` and `x` are both same, there is no reverse happening. So if we check the `reverse` is not called i.e. `()` is missing in the function call.


So after modifying the code:-

````
def isPal(x):
    """ requires x to be a list,
        return True if the list is a palindrome, False otherwise """
    assert type(x) == list
    temp = x
    print "Before Reverse temp: ", temp
    print "Before Reverse x: ", x
    temp.reverse()
    print "After Reverse temp: ", temp
    print "After Reverse x: ", x
    if temp == x:
        return True
    else:
        return False

def isPalTest():
    L = ['a','b']
    result = isPal(L)

    print "Should print False, ", result

    L = ['a','b','a']
    result = isPal(L)
    print "Should print True, ", result


isPalTest() 

````
The output is:-

````
Before Reverse temp:  ['a', 'b']
Before Reverse x:  ['a', 'b']
After Reverse temp:  ['b', 'a']
After Reverse x:  ['b', 'a']
Should print False,  True
Before Reverse temp:  ['a', 'b', 'a']
Before Reverse x:  ['a', 'b', 'a']
After Reverse temp:  ['a', 'b', 'a']
After Reverse x:  ['a', 'b', 'a']
Should print True,  True
````
Now if we see, we find that after reverse both `temp` and `x` have changed, the reason for this is we are pointing to the same memory location, so the reverse is changing both. So we have to use a **Full Slice**.

The final code is:-

````
def isPal(x):
    """ requires x to be a list,
        return True if the list is a palindrome, False otherwise """
    assert type(x) == list
    temp = x[:]
    print "Before Reverse temp: ", temp
    print "Before Reverse x: ", x
    temp.reverse()
    print "After Reverse temp: ", temp
    print "After Reverse x: ", x
    if temp == x:
        return True
    else:
        return False

def isPalTest():
    L = ['a','b']
    result = isPal(L)

    print "Should print False, ", result

    L = ['a','b','a']
    result = isPal(L)
    print "Should print True, ", result


isPalTest() 

````

## References ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/MIT6_00SCS11_lec07.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/lec07.py)
4. [Lecture slides (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/MIT6_00SCS11_lec07_slides.pdf)


### Problem Sets ###

1. Problem Set 3: Wordgames (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/MIT6_00SCS11_ps3.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/ps3.zip)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/ps3_sol.zip)
2. Problem Set 4 (Assigned)
    1. [Problem Set 4 Due on Lecture 10](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes)

### Further Study ###

1. [8. Errors and Exceptions](http://docs.python.org/tutorial/errors.html)
2. [Appendix A: Debugging ](http://www.greenteapress.com/thinkpython/thinkCSpy/html/app01.html)

## Check Yourself ##

### Why do computers use binary representations? ###

Computers are made up of Switches, which have only two states `0` and `1`. 

### Why shouldn't we test for equality with floats? ###

The representation of floats in computer is not exact, because computers can only store binary numbers, and some of the approximation of floats are not accurate.

### When debugging, how can you ensure that the values in your program are the ones you think they are? ###
We can check by using `print` statements.








