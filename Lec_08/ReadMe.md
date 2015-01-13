# Lecture 08 | Efficiency and Order of Growth #

## Efficiency ##

Efficiency is about algorithms and not about coding details.

Problem Reducing, where we reduce a new problem to previously solved problem.


2 Dimensions:-

* Space.
* Time.

Computing Complexity.

Influenced by 
* speed of machine
* Cleverness of the python implementation.
* Depends on the input.

Counting the number of basic steps.

T:N -> N

First N: Size of input
Second N: No of steps.


Step is a operation which takes constant time.

## Random Access Machine (RAM) ##

They are sequential. We can access any part of memory at random in constant time.

## Representation of Algorithms ##

### Best Case ###

### Worst Case ###

Provides a upper bound. So we do not have surprises. Worst case happen often.

### Average Case ###


## Order of growth ##

Growth with respect to size of input.

Asymptotic growth. Big O notation. **O**(n), liner of n. We call it Big **O**, because of omicron. Gives a upper bound for the Asymptotic growth of function.

f(x) e **O**(n2)

Function F grows, no faster than the quadratic polynomial x2.

* Order 1 : Constant.
* Order log(n) : Lograthimic
* Order (n) : liner
* Order nlog(n): log liner
* order (nC) : polynomial
* order (Cn) : exponential


## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/MIT6_00SCS11_lec08.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/lec08.py)
4. [showGrowth code (PY)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/showGrowth.py)


### Check Yourself ###
### Why is efficiency important? ###
### What notation do we use to state complexity? ###





