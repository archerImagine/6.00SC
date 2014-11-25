# Lecture 3 | Problem Solving

## [Decrementing Function.](https://www.youtube.com/watch?v=ggxY20cXql8&list=PLB2BE3D6CA77BB8F7#t=119)

Consider the following Cube Root code, which we have already seen.

````
x = int(raw_input('Enter an integer: '))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans + 1
    #print 'current guess =', ans
if ans*ans*ans != abs(x):
    print x, 'is not a perfect cube'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
````

In this code, what is the value of `x` is it a guarantee that it will stop.
* Is it all positive number
* Is it all negative number
* It is 0
* Or is it all integers

Basically it terminates for all integer value of `x`, this is because of the presence of a **Decrementing Function** in the code, which guarantees to stop a loop execution.

### Properties of Decrementing Function ###

1. It will map some set of program variables to an integer.
2. The value of the variable is non-negative when entering the loop for first time.
3. When the value of the integer is less than `0`, loop terminates.
4. The value is decreased each time in the loop.

These 4 property guarantees to terminate the loop, Also there is a possibility to count up to a value, but we can always use some logic to always decrement in place of increment.

So how do we find the **decrementing function** of the above code?

As per the first property we have to find a program variable which can store integers, and we have only 2 program variables in the code, `x` and `ans`.

The decrementing function will be,

````
abs(x) - ans**3
````

Considering `x=8` to start with the steps will be as shown below

| `x` | `ans` | `abs(x) - ans**3` |
| --- | ----- | ----------------- |
| `8` | `0`   |                 8 |
| `8` | `1`   |                 7 |
| `8` | `2`   |                 0 |

So when the `ans` becomes `2`, the loop exits.

Now a lot of you might be thinking where is this `abs(x) - ans**3` in the actual code mentioned above, it is explicitly not present, so if you look in the code, we are actually doing this step, in a multiple ways.

We are incrementing the `ans` variable each time in the `while` loop. And the `while` condition test the condition `ans*ans*ans < abs(x)` which can rather be modified to `abs(x) - ans**3` as both means the same.

## [Exhaustive Enumeration/Brute Force](https://www.youtube.com/watch?v=ggxY20cXql8&list=PLB2BE3D6CA77BB8F7#t=549)

The above code uses the method called **Guess and Check**, where we are basically Guessing a answer and then checking. This is also called **Exhaustive Enumeration.**

The reason it is called **Exhaustive Enumeration**, because we go through the complete answer set and then decide if we have achieved the answer. So by this we mean we are exhausting the answer space.

For awful set of problem a Exhaustive Enumeration technique will work, for the simple reason that today's computer are very fast.

The Exhaustive Enumeration Technique is also called **Brute Force** technique.

## [`for`  and `while` Loop](https://www.youtube.com/watch?v=ggxY20cXql8&list=PLB2BE3D6CA77BB8F7#t=789)

There is a variation in looping construct, what we saw in the last example was `while` loop, now we will see the same program with `for` loop.

````
x = int(raw_input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print x, 'is not a perfect cube'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)

````

The major difference is this line:-
````
for ans in range(0, abs(x)+1):
````

basically `range(from,to)` generate number starting from `from` and ending at `to - 1` numbers.


we also have another interesting code construct in the above code

````
if ans**3 == abs(x):
        break
````
What this break basically does is, it break from the loop, and executes the statement followed by it. This is similar to the condition check we had in `while` loop.

Since we can also nest `for` loop's, the break will break from inner for loop, if the code is like this.

````
for ans in range(1,10):
        for x in xrange(1,10):
            print "ans: ", ans, " x " , x
            if x == 3:
                break
````

`for` and `while` loops are interchangeable, there is nothing which we can do with one which cannot be done with other.

## [Approximation](https://www.youtube.com/watch?v=ggxY20cXql8&list=PLB2BE3D6CA77BB8F7#t=1109)

Now we have seen the logic to find the cube root of a number, let say we want to extend that logic to find the square root of a number.

To find the square root of `2`, is basically a very large decimal point number, not this provides us with a very nice programming construct called **Approximation.**

In **Approximation**, we basically find answers which are close enough to be called and answer but may not be exact ans.

So in **Approximation** we need to find answers within a **epsilon** value. So the Square root problem can be re-written as.

Find a `y` such that `y * y = x +- e` where `e` is epsilon value.

To solve the above problem, here is the code for the same

````
x = int(raw_input("Enter a Number to Find its Square Root: "))
epsilon = 0.01
numOfGuesses = 0
ans = 0

while abs(ans**2 - x) > epsilon and ans <= x:
    ans += 0.00001
    numOfGuesses += 1
print "Number of Guess: ", numOfGuesses
if abs(ans ** 2 - x) >= epsilon:
    print "Failed to find Square Root"
else:
    print ans, " is close to square root of ", x
````

When we run, we get the following output

````
Enter a Number to Find its Square Root: 25
Number of Guess:  499900
4.99899999998  is close to square root of  25
````

Now there are few things to note in the above code and the answer which we got.

The first thing to note is what is the **Decrementing Function** for the above code, the easiest thing to understand about the **Decrementing Function** is that it should be part of the condition check of the loop.

Now in this regard we would have 2 decrementing function
1. `abs(ans**2 - x) > epsilon` or
2. `ans <= x`

Now we might be thinking that the `1`st one is the decrementing function, but it is actually the `2`nd one which guarantees the exit of loop, the `1`st condition is just an optimization to reach the exit of the loop faster.

Now the Second thing to note about the output is, if we gave input as `25`, we did not get `5` as the square root, but we got `4.99899999998` instead, this is because we did not ask for **closest square root of a number**, but we asked for **Find a `y` such that `y * y = x +- e` where `e` is epsilon value.**

Now this is called *Specification of a Problem*

Another thing which is noticeable in the output of the program is

````
Number of Guess:  499900
````
We got the answer, in roughly .5 million number of guesses, this again proves that **exhaustive enumeration** is most of the time good enough.

So one question arises, **Can we see the code and find out the number of guesses it will make to find the answer?**

We can find that, basically by figuring out the distance from the starting point of guess to the actual answer, it also depends on the value of epsilon, and the number of increment which it takes.

These are the lines of code, which help in finding out the running time as discussed in the previous paragraph.

* Distance from the starting point of the guess
    - `ans = 0`
* value of epsilon
    - `epsilon = 0.01`
* number of increment
    - `ans += 0.00001`

Now we can increase the increment, but it will sometimes jump over the real answer. So basically we need a better algorithm to find an answer.

## [Specification of a Problem ](https://www.youtube.com/watch?v=ggxY20cXql8&list=PLB2BE3D6CA77BB8F7#t=1576)

## [Bisection search ](https://www.youtube.com/watch?v=ggxY20cXql8&list=PLB2BE3D6CA77BB8F7#t=1931)

Now as we saw in the last section, the Exhaustive Enumeration is very slow in some of the case, though it gives a correct ans. So if we have to better the algorithm we have to go for **Bisection Search**.

In Bisection Search we have a technique which is called **Cut Search Space in Half** as described below.

### Cut search space in half
In this what we do, is we try to reduce the search space into half in each iteration. In the previous examples we did tiny increment in a liner fashion.

So what we do is, we start with the Guess somewhere in the midpoint of the Search space, and the check if the answer is too big or too small, depending on the answer we can figure out if we have to see which section for the answer, and then we repeat these till we get a answer.

Here is the Square root code, using the bisection search.

````
x = int(raw_input("Enter a Number to find the square root: "))
epsilon = 0.01
numOfGuesses = 0
low = 0
high = x
ans = (low + high)/2.0

while abs(ans**2 - x) > epsilon and ans <= x:
    print "LOW: ", low, " HIGH: ", high, " ANS: ", ans
    numOfGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0

print 'numOfGuesses =', numOfGuesses
print ans, 'is close to square root of', x
````

TODO: Not able understand the number of search space?
TODO: What is the positive integer for with the bisection search does not work?
[Square Roots of Numbers between 0 and 1](http://mathforum.org/library/drmath/view/58270.html)
## References ##
### Links ###
1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-3-problem-solving/)
2. [Lecture code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-3-problem-solving/MIT6_00SCS11_lec03.pdf)
3. [Lecture code (PY)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-3-problem-solving/lec03.py)


## Check Yourself ##
### What does it mean for a program to terminate? ###
When a program either runs to its completion or terminates with a exception, this is said to be program have to terminate, but if it enters a infinite loop it will never exit.

### What is a for loop? ###
This is the construct of a `for` loop

````
for ans in range(0, abs(x)+1):
````
where `ans` get the value from `0` till `abs(x) + 1 -1` in the increment of `1`
