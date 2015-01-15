# Lecture 08 | Efficiency and Order of Growth #

## [Efficiency ](https://www.youtube.com/watch?v=GmkRmETGghw&list=PLB2BE3D6CA77BB8F7#t=23) ##

We should start this lecture with a very intrinsic question, **Why is efficiency important?**

With the advancement in the computing power we can solve most of computational problem using brute force, but as we all know some of the computational problem are not large, they are enormous, and it takes approximately around time at the order of days to solve them. So efficiency is the difference in say ending a computation in 2 weeks and not 2 years.

We should always remember few things about efficiency:-

* Efficiency is about **algorithms** and not about coding details.

Now we do not invent algorithm for most of our problem, there is very rarely any invention in the algorithm space.

So the second most important thing to note about efficiency:- 

* **Problem Reducing**, where we reduce a new problem to previously solved problem.


Efficiency is thought mostly in these 2 dimensions:- 

* **Space**. 
* **Time**.

Most of the time we have to make a trade off between one of these. Of the above 2 dimensions, **Time** is what people worry about the most.

Another question to answer about efficiency is, **How do we measure the time taken by an algorithm to run?**

The above question is actually called **Computing Complexity**. And we do not just run a algorithm on a machine and manually time it and say this is better than that other algorithm because it is 

**Influenced by** 
* speed of machine
* Cleverness of the implementation.
* Depends on the input.

So due to these reason we should be able to talk about algorithm efficiency in a more abstract manner.

We do this by counting the number of basic steps.

````
T:N -> N
````

* First N: Size of input  
* Second N: No of steps.
* Step is a operation which takes constant time.

### [Random Access Machine (RAM)](https://www.youtube.com/watch?v=GmkRmETGghw&list=PLB2BE3D6CA77BB8F7#t=557) ###

To measure the steps, we will use a mathematical model of a machine called **Random Access Machine (RAM)**

In a RAM, instruction are executed one after another in a **sequential** manner, and **Constant** time to access memory.

As we can see, the **Constant** time to access memory is not accurate, because in older computers it used a Tape, and it is faster to access the Tape at the beginning of it than at the end of it, also in modern computers we have L1 or L2 cache, along with memory hierarchy, so here also it is not a constant time.

So we do not go into that much details of a machine, and safely use the RAM model.

## [Order of Growth ](https://www.youtube.com/watch?v=GmkRmETGghw&list=PLB2BE3D6CA77BB8F7#t=698) ##

We can think of how long a algorithm can run in 3 ways:-

* **Best Case**
* **Worst Case**
* **Average Case**

So to understand the above 3, let us consider Liner search as an example:-

In liner search we have a array of integers, and we have to find a element in
that array of integers, and we traverse the array one element at a time, check
if the element is the same and return true or false.

The **Best Case** will be the first element itself is the element I am searching. It is the minimum running time of all the case.

The **Worst Case** will that the element I am searching is not present, The worst case will be maximum running time of all the case.

The **Average Case** will be the case, where most of the time we will find the element, it looks like average case is the case we should be bothered about the most, but the truth is in algorithm analysis we never care about average case because of it is too hard.

So we always focus on the **Worst Case**, It gives a upper bound, how bad things can happen, which means there are no surprises and worst case happen often.

Let consider this with an example:-

````
def f(n):
    assert n >= 0
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

print "f(5)", f(5)  
````

So the number of steps will be:-

* `assert n >= 0` and `answer = 1` corresponds to 2 steps.
* Then the loop, of n times. where it does these steps, `n > 1`, `answer *= n` and `n -= 1`, i.e 3n steps.
* and finally `return answer` which is 1 steps.

So totally it executes `2 + 3n + 1` steps.

Now consider `n = 3000`, so total steps will be `9003` steps. so we do not care if it is `9000` or `9003`. 

In case of algorithmic complexity we tend to ignore additive constants, like `2` and `1` in the above case. The reason of ignoring is that we are interested in the growth, i.e. how the running time increases as the no of input increases.

Now do we care for the `3` in `3n` i.e. do we care if the programs completes in 1 day or 3 days, we might care, but we might not care if it is 1 year or 3 years, we will just say it takes years to complete the program.

So with the above argument we ignore the multiplicative constants.

We use a model of Asymptotic growth, and we do it using **O**(n), i.e. it is linear in growth.

**O**(n), or Big Oh notation gives us a upper bound for the Asymptotic growth of a function.

````
F(x) e O(n)
````

The function F grows no faster than the liner polynomial `n`.

![Order of growth ](http://www.cs.odu.edu/~toida/nerzic/content/function/growth_files/summary.gif)

Some of the popular order which we will see is:- 

* Order 1 : Constant.
* Order log(n) : Lograthimic
* Order (n) : liner
* Order nlog(n): log liner, occurs very often
* order (n ^ C) : polynomial
* order (C ^ n) : exponential

When we saw the definition of Asymptotic function, we said ** The function F grows no faster than the liner polynomial `n`. **, but this is very generic statement, what we want is a tight bound, i.e. it grows no slower than something.

This is the big theta notation.


Consider another example:-

````
def factorial(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)

print factorial(5)
````

The above is a factorial in recursion. So what is the complexity of this. So as we had discussed we will drop the additive constants, so what we care about in the above code is how many times the recursive function `factorial()` is called. That is `n` times, which is same as the iterative version, there might be few overheads in terms of recursive function call, but we do not consider them.

Consider another example:-

````
def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x
print g(5)  
````

So to find the complexity of the above example, we start with the inner loop, which runs `n` times, and this inner loop runs `n` times for each `n` times of outer loop, so the complexity will be `n^2`.

So as a rule of thumb, we start with the inner loop and move to way outside.

Now consider another example:-

````
def h(x):
    assert type(x) == int and x >= 0
    answer = 0
    s = str(x)
    for c in s:
        answer += int(c)
    return answer
print h(556)            
````

So what will be the algorithmic complexity of the method `h()`, at a first instance we will say, `n` liner, because the loop if running for `n` times which is the no of digits, but `s` is a local variable, we always calculate the complexity in terms of the input to the function, in this case it is `x`, which will be `log x`

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/MIT6_00SCS11_lec08.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/lec08.py)
4. [showGrowth code (PY)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-8-efficiency-and-order-of-growth/showGrowth.py)


### Check Yourself ###
### Why is efficiency important? ###
### What notation do we use to state complexity? ###





