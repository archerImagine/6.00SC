# Lecture 04 | Machine Interpretation of a Program #

The actual lecture starts at [9:26](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=566).

We have seen the square root program which we have written previously, just for reference here it is again.

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

Now this calculates the square root, but if we have to calculate cube root, or any other higher order roots, we have to copy paste the same code multiple times to get the desired result.

This extra code will hamper in maintainability of the code, as a result it will become difficult to debug such code. The best thing a programmer can do is to write less code with the same functionality.

So write less code we need a new language construct called **FUNCTIONS.**

## [Module ](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=740)##

Before we give an introduction to functions, we should understand what functions will achieve for us. It will provide us with a mechanism for:-

* Decomposition
* Abstraction


### [Decomposition ](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=764)###

Decomposition allows us to create structure for our programs. It helps to break our program and create modules in the programs. There are two units of modules.

* Function.
* Class.

**Modules** are self-contained and reusable which can be used in multiple context.

### [Abstraction ](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=816) ###

Abstraction follows the wording by **Thomas Gray**.

> Ignorance is Bliss.

Basically abstraction suppresses details, it act like a black box of code, of which we should only understand the use of the code and can be ignorant of the internal implementation or details of its internals.

## [Function ](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=879)##

A function allows us to break code into reusable, coherent pieces. It allows use to extend an existing language with new primitives, and use these primitives just the way we use other language primitives like `float`, `string`.

An example of function is given below:-

````
def withinEpsilon(x, y, epsilon):
    """x,y,epsilon ints or floats.  epsilon > 0.0
       returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon

print withinEpsilon(2,3,1)
val = withinEpsilon(2,3,0.5)
print val
````

Lets dissect the above code. The first line of the code:-

````
def withinEpsilon(x, y, epsilon):
    """x,y,epsilon ints or floats.  epsilon > 0.0
       returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon
````

* `def` : means define.
* `withinEpsilon` : is the function name. The function name should be mnemonic.
* `x, y, epsilon` : formal parameters.
* followed by a function body.
````
"""x,y,epsilon ints or floats.  epsilon > 0.0
       returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon
````

* `return` : special command, which returns the value to the one who have called.
* Specification: Tells what a function does, which is in the comment

````
"""x,y,epsilon ints or floats.  epsilon > 0.0
       returns True if x is within epsilon of y"""
````


Now we have get the `withinEpsilon` function to be invoked, which can be done in these 2 ways:-

````
print withinEpsilon(2,3,1)      #Type 01
val = withinEpsilon(2,3,0.5)    #Type 02
print val
````

Since `withinEpsilon` returns a value we can use this function as a part of an expression.

Now if we modify the `withinEpsilon` code such that we remove the return statement.

````
def withinEpsilon(x, y, epsilon):
    """x,y,epsilon ints or floats.  epsilon > 0.0
       returns True if x is within epsilon of y"""
    #return abs(x - y) <= epsilon
````

So when we invoke the function like this.

````
print withinEpsilon(2,3,1)      #Type 01
val = withinEpsilon(2,3,0.5)    #Type 02
print val
````

we will get the output as:-

````
None
None
````

Because the function will return by default `None`, if there is no return statement in the function.

There is a big **advantage** of a function, as I can invoke `withinEpsilon` wherever I want and can avoid duplicate the code.

### [Parameter and Arguments](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=1385) ###

Now to understand parameter of function, we should look at the below code.

````
def f(x):
   x = x + 1
   print 'x =', x     #First Print, which prints x = 4
   return x

x = 3
z = f(x)
print 'z =', z        #Second Print, since we are assigning the return value of function f()
print 'x =', x        #Thrid Print, since the original value of x = 3 and the function does not modify the original value.
````

The output of the above code is:-

````
x = 4
z = 4
x = 3
````

Why we got this output, lets understand this.

The first 2 outputs are expected, because we are printing the value of `x` in function `f()` and returning the value `4` from function `f()`.

But the question is why does the 3 print gives `x = 3`, the reason being the variable `x` within the function `f()` if different that outside it, when we invoke `f(x)` the value of `x` if copied, and not the actual `x` is passed so that when we modify `x` inside `f()` it has no impact on value of `x` outside.

The confusion is because the formal parameter of `f()` as `x`, we could have used some other variable and it will still work.

Important question to understand is, **What happens when we call a Function ?**

1. The formal parameter, `x` in this case is bound to the value of the actual parameter, `x`.
2. Upon entry to a function, a new scope is created. A scope is a mapping from names to objects.


## [Assert ](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=1707) ##

Assert is a command, were the keyword `assert` is followed by a expression, if the expression evaluates to `True` it does nothing else, if it evaluates to `False` the program stops.

Consider the below code.

````
def f1(x):
   def g():
       x = 'abc'
       assert False
   x = x + 1
   print 'x =', x
   g()
   return x

x = 3
z = f1(x)
````

Now when we execute the above code we get the output as:-

````
x = 4
Traceback (most recent call last):
  File "assert.py", line 12, in <module>
    z = f1(x)
  File "assert.py", line 7, in f1
    g()
  File "assert.py", line 4, in g
    assert False
AssertionError
````

We get a `AssertionError` because we have a `assert false` in `g()`. Now with the help with `assert` we will try to understand scope.

## Scope ##

As discussed in the above code, when the interpreter executes the above code line by line we get the following.

### Main Scope ###

Interpreter first creates a `main` scope, which start at the first line which is a `def` of we have a scope with the name `f1()` in the scope.

Then it jumps to the line `x = 3`, creates a variable `x` in the same `main` scope.

Then it executes the line `z = f1(x)`, creates a variable `z`, but to get the value of `z` we have to invoke `f1()`, so with this we have a `f1` scope.

### f1 Scope ###

Now the interpreter will execute the function `f1` line by line, so in the `f1` scope we create a `def g()` which creates a object of name `g`.

Then it jumps to the line `x = x + 1`, since `x` was a formal parameter it was already in the `f1` scope.

Then it executes `print 'x =', x`, which prints the value of x.

Then we invoke `g()`, which creates the `g` scope.

### g Scope ###

Now the interpreter is executing `g()`, which use the new `x` different from `f1` scope. And in the next line it assert, so we get the output from `g()` ---> `f1()` ---> `main` which is a stack.

### Stack frame ###
Scope are created as a Stack. So for the above code the stack will look like.

|        |
| ------ |
| `g()`    |
| `f1() `  |
| `main()` |

Now if the assert was not there, and `g()` executed the stack would look like.

|        |
| ------ |
| `f1()`   |
| `main()` |


## [Strings ](https://www.youtube.com/watch?v=Mx0uXIBD-yA&list=PLB2BE3D6CA77BB8F7#t=2718) ##

Strings are non scalar value, i.e. values which can be decomposed. Consider the below example.

````
sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print sumDigits

````

Consider this line `for c in str(1952):` till now we have used `for in` on integer values, but we can use it on any value on which we can enumerate each and every values.

We can also do certain operation like **Slice** on string, consider the below code.

````
s = "abc"
c = s[0:1]
print 'c = ', c
````
The output will be `a` because as in `range` we go till `n-1` term the same is done here, so slice creates a new string.

We can also used `find`, which will return the index of the character found.

---


## References ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/)
2. [Lecture code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/MIT6_00SCS11_lec04.pdf)
3. [Lecture code (PY)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/lec04.py)

### Problem Sets ###
1. Problem Set 1: Paying Off Credit Card Debt (Due)
    1.  [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/MIT6_00SCS11_ps1.pdf)
2. Problem Set 2 (Assigned)
    1. [Problem Set 2 Due on Lecture 6](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/)

## Check Yourself ##
### What is decomposition? ###
Decomposition is the process to break larger problems into more manageable smaller problem.

### What is abstraction? ###
Abstraction is the process by which we hide the inner details of implementation so that the user is not bothered with the internal details. It is just like a black box, where only the specification are exposed.

### What is the difference between formal and actual parameters? ###
Formal parameters are the variables which are used inside a function, and actual parameter are the variables with which the function is invoked.

ex:- Consider the below code.

````
def sum(a,b):
  return a + b

x = 8
y = 9
print "sum of 8 and 9 is = ", sum(x,y)
````
In the above code, formal parameters are `a` and `b`, and the actual parameters are `x` and `y`.











