
# Lecture 1: Introduction to 6.00 

**Programming: The most fun you can have with your clothes on.**

There is essentially two kinds of knowledge. [TimeStamped YouTube Links](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=528) 

* **Declarative.**  
* **Imperative.**

## Declarative Knowledge 

* [TimeStamped YouTube Links](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=560)

Declarative knowledge is composed of statement of facts.

example:-  

* y is the square root of x if and only if y * y = x.  

The above point is a fact, declarative knowledge does not tell you how to find the **SQUARE ROOT**, interestingly it tells you how to test the square root.

## Imperative Knowledge.

* [TimeStamped YouTube Link](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=656)

Imperative knowledge is about how to accomplish something. Declarative knowledge is about testing the validity of the knowledge and Imperative about finding how to generate the knowledge.

Consider the steps to find a square root of a number, The Declarative knowledge tells us.  

* y is the square root of x if and only if y * y = x.

Imperative knowledge tells us how to find the square root, consider the below steps:- 

1. Start with a guess g.
2. if `g * g` is close enough to `x`, then `g` is a good approximation of the square root of `x`.
3. Otherwise, create a new guess by averaging `g` and `x/g`, i.e `g(new) = (g(old) + x/g(old))/2`
4. Using this new guess, go back to Step 2.  

**Example:- **
If we have to find square root of 25, which is 5,

Iteration 1:  

1. Start with  `g = 3`.
2. `3 * 3 = 9`, which is not close to `25`.
3. Calculate new guess, `g(new) = (3 + 25/3)/2 = 5.666666666666667`.
4. Restart at Step 2.  

Iteration 2:  

1. Start with `g = 5.666666666666667`
2. `5.666666666666667 * 5.666666666666667 = 32.11111111111111`, which is not close to `25.`
3. Calculate new guess, `g(new) = (5.666666666666667 + 25/5.666666666666667)/2 = 5.03921568627451`.
4. Restart at step 2. 

Iteration 3:

1. Start with `g = 5.03921568627451`
2. `5.03921568627451 * 5.03921568627451 = 25.39369473279508`, which is close to `25`, so stop.

So from the above steps we can deduce that.  


### Algorithm: 
An algorithm is a description on how to perform a computation. We say that the algorithm have **CONVERGED**, which is fancy way to saying that it has halted.  

* [TimeStamped YouTube Link](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=918)

An algorithm consists of these terms:-   

* **Instructions**:- Set of step to perform the computation, so in the above algorithm we have 4 sets of instructions
* **Flow of control**:- How the instruction are supposed to execute i.e. the sequence of execution, which in the above algorithms is Step 1,2,3,4 and then repeat from step 2
* **Termination condition**:- The particular condition on which the execution of instruction will be halted/ converged, in the above algorithm it is if `g * g` is close enough to `x`. In the absence of a termination condition the algorithm will repeat till infinity. 

## How do we capture this idea of a recipe or algorithm in a mechanical process?
* [TimeStamped YouTube Link](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=1064)

We have defined the algorithm to find the square root, now this is a theoretical set of instruction, which needs to be converted to a mechanical process for it to be possible to do automatic computation using computers.

One way will be to design a machine which specifically computes square roots, meaning to design a circuit to implement this algorithm. This is used to be the way all computers worked and they were called:- 

* **Fixed Program Computers**:- They were designed to do very specific things, ex, The very first computer designed was supposed to compute the trajectory of artillery, and then Alan Turing designed a computer to break the enigma code, and thats all these computers were capable of nothing else.

Thee type of computer are not very efficient and cost effective, so then came **Stored Program Computers**.

* **Stored Program Computers**:- The basic notion of these computers are that there is no difference between the program that implement the algorithm and the data on which it operates on.  
    - Once this was clear, we can visualize computers as program itself, and in particular a type of program called **interpreter.**
    - An **interpreter** is a program which can execute any legal set of instructions. 
    - So this diagram below shows how a **Stored Program Computer** looks like.

## Stored Program Computer  

* [TimeStamped YouTube Link](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=1335) 

A stored program computer looks like this. It has the following main components.  

* Memory
* Control Unit: A control unit basically tells Memory what to do, like fetch some data, put some data,
* Arithmetic Logic Unit: This is the brains of the computer,
    - Accumulator: Its stores the result.
* Input
* Output

Typically a computers have a very minimal instruction sets, based on which we can create great programs based on the different combination of these instructions.  
Alan Turing in fact said that a primitive computer does not need more than 6 Instructions.  

## Programming Language

* [TimeStamped YouTube Link](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=1505)

A programming language provide as discussed in the section Algorithms.

* the set of primitive instruction to work on a computers. 
* a set of primitive control structures.

One programming language differ from another in these two points along with how the instructions are clubbed together to perform complex actions.

### What Defines a Programming Language?

* [TimeStamped YouTube Link](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=1677)

These together defines a programming language.  

* **Syntax**: Tells us which sequence of character and symbols constitute a well formed string, but it may not have a meaning
    - ex: x = 3 + 4, is syntacticly correct
    - but, x = 3 4 is not
* **Static Semantic**: Tells us which well formed strings have meaning.
    - ex: 3/"abc", is syntacticly correct, but does not have a meaning
* **Semantics** : Looks only at those strings which are syntacticly correct, and static semantically correct and assigns a real meaning to it. So like in natural language can have ambiguity, a programming language cannot have any ambiguity.

There are times programs does not give output which we desired, in place of that it might give these:-  

* Program can **Crash**
    - In a properly designed computing system, the **crash**, should be local, that means it should not destroy the whole system.
* Program can go never stop, i.e. **Infinite Loop**.
* Program which runs to completion but produces **wrong output**.

The problems mentioned above is in ascending order of erroneousness, i.e., crash is much more acceptable than an infinite loop which is acceptable than a wrong output, because a wrong output can result in very life threatening results, and you may not be aware of any errors in the program, but the other two are errors in the programs.

## Compiled Vs Interpreted Language.

* [TimeStamped YouTube Link](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7#t=2230)

In terms of error handling, Python is somewhere in the middle, it is not as robust as Java, but better than C at weeding out meaning less things.

A programming language should have a strong **Static Semantics**, so that it behaves as expected.

### Benefits of Python 

* It is easy to learn.
* It is widely used in life sciences.
* It is easier to debug, because it is in an interpreted language, because it outputs error in the programming language itself and not in object code like compiled languages.



## References. 
* [Lecture Slide](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-1-introduction-to-6.00/MIT6_00SCS11_lec01_slides.pdf)
* [OCW HomePage Lecture 01](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-1-introduction-to-6.00/)