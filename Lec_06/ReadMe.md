# Lecture 06 |  Recursion #
---

## [Dictionaries ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=48) ##
As we have seen in the previous lecture notes about Dictionaries, It is a `<Key, Value>` pair. The interesting thing about this is, what things can become `keys` and which things can become `values`.

So some examples of such association for Keys.

* Keys with numbers
* Keys with Strings
* Keys with other objects including Dictionaries.

Along with the above property, you can also have great things take the form of keys.

* Keys can be just strings.
* Keys can be a Tuple
* Keys can be set of names.

So suppose we did not had Dictionaries, in that case we can surely have code which can do the same thing. Consider the below code.  

````
def keySearch(L,k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None

myList = [
            [1,"One"],
            [2,"Two"],
        ]
for e in myList:
    print "e = ", e

print "keySearch(myList,1): ", keySearch(myList,1)      #prints "One"
````

Now as we can see from the above code a list can be used to implement a Dictionaries, and a simple `for` loop for the searching logics in Dictionaries.

Now the pertinent question arise, if we can implement a Dictionaries in this manner then what is the need of the actual data structure Dictionaries.

To answer this question we have to see, how much time does searching takes in this new implementation.

So on an average if we use some good algorithms for searching, we will requires some time which is dependent on the size of the list, so the bigger the list the larger the time taken.

But to do the same search on the built-in Dictionaries, it takes constant time, that means it is independent from the size of the list.

There is also a discussion on [Reddit.com | What are some great blogs or article to read for understanding Dictionaries in Python better?](http://www.reddit.com/r/learnpython/comments/2r46ro/what_are_some_great_blogs_or_article_to_read_for/)

## [Modular Abstraction ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=245) ##

Now can we look into this example code:-

````
EtoF = {'bread': 'du pain', 'wine': 'du vin',\
        'eats': 'mange', 'drinks': 'bois',\
        'likes': 'aime', 1: 'un',\
        '6.00':'6.00'}

def translateWord(word,dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word

def translate(sentences):
    translation = ""
    word = ""
    for c in sentences:
        if c != ' ':
            word = word + c
        else:
            translation = translation + ' ' +translateWord(word, EtoF)
            word = ""
    return translation[1:] + " " +translateWord(word, EtoF)

print translate('John eats bread')
````

The above program/code is a very basic translation system. But it explains few basic programming construct.

For the above code we are making few assumptions for it to work, and those assumptions are:-  

* There is a single space between words which we are checking here.
    ````
    if c != ' ':
            word = word + c
    ````
* The is no space after the last word of the sentence.
    ````
    return translation[1:] + " " +translateWord(word, EtoF)
    ````

So the first programming construct that we learn from this code is to make you assumptions clear.

The next thing which we learn can be found if we know the answer to this question:-

We have these function in the above code:-

* `translateWord(word,dictionary)`
* `translate(sentences)`

Why to divide this into these 2 functions in place of writing everything in one function. 

The answer to the above question is:-

* The first thing which we get is small function or piece of code, which we can test individually and check for its correctness, in place of a big chunk of code.
* The second thing which we achieve is the next programming construct i.e. **Modular Abstraction**.

So with **Modular Abstraction** we get a perfect division of code which helps in segregating piece of code which are not interdependent so that we can change the internal structure of the code any time if we have this abstraction.

## [Divide and Conquer ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=728)##

The Modular Abstraction is a specific implementation of a more generic term called **Divide and Conquer**.

**Divide and Conquer** is the idea of taking a big/large problem and breaking them into some simpler problems. These simple problems have 2 properties.

1. Small problems are easier to solve than the big problem.
2. Solutions to small problems can **easily** be combined to solve the big problems.

## [Recursion ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=866) ##

**Recursion** is a technique for Divide and Conquer. Recursion is used in two ways in computer science.

1. Way of describing or defining problems.
2. Way of designing solutions.

A recursive definition of a problem have 2 parts:-

1. The first part is very simple. This is called ***BASE CASE***
2. The second part which is called **recursive or inductive case**, its job is to reduce the bigger problem to a much simpler problem of the same type in addition we might have to do some simple operations.

So now let us see some example of **Recursions**, 

### [Exponentiation ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=1111) ###

Lets see how we can use recursion to solve integer Exponentiation. As we all know the definition of Exponentiation is,

````
(b)^ n = b * b * b * .......b (n times)
````

So if we have to solve the above equation using recursion we have to think, how to reduce this big problem into small problem and the way to do this is.

````
(b)^ n = b * (b * b * .......b) (n - 1 times)
````
Now this might not look a great thing to do, but notice what we did, we effectively telling ourself that the big problem (n) times has reduced to (n - 1) times and it will continue till n > 0.

And when n = 0, we can say (b)n = 1

So combining these two we can understand the power of recursion. So the code for this would be.

````
def simpleExponentiation(b,n):
    if n == 0 :
        return 1
    else:
        return b * simpleExponentiation(b,n-1)


print "simpleExponentiation(5,3): ", simpleExponentiation(5,3)
````

### [Tower of Hanoi ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=1310) ###

One more use case for using recursion is the famous [Tower of Hanoi ](http://en.wikipedia.org/wiki/Tower_of_Hanoi), which helps us to understand a difficult problem in simple steps. So we can solve it by using:-

> A key to solving this puzzle is to recognize that it can be solved by breaking the problem down into a collection of smaller problems and further breaking those problems down into even smaller problems until a solution is reached
> * label the pegs A, B, C — these labels may move at different steps
> * let n be the total number of discs
> * number the discs from 1 (smallest, topmost) to n (largest, bottommost)
> To move n discs from peg A to peg C: 
> * move n−1 discs from A to B. This leaves disc n alone on peg A
> * move disc n from A to C
> * move n−1 discs from B to C so they sit on disc n

So the sample code for the above recursion will be:-

````
def hanoi(n,f,t,s):
    if n == 1:
        print 'move from ' +f +' = ' +t
    else:
        hanoi(n-1,f,s,t)
        hanoi(1,f,t,s)
        hanoi(n - 1,s,t,f)


hanoi(5,'f','t','s')
````


### [Palindrome ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=1614) ###

One more use case to use recursion is [Palindrome ](http://en.wikipedia.org/wiki/Palindrome).

The base for a string to be palindrome is that it is of length `1` or `0`. So now we have the base case, how to break it into problems of smaller size of the same type.

Compare the first and last character are same take them out and continue if not equal, exit there as it is not a palindrome, so we will have smaller version of the same problem.

So the same can be written in code as:-

````
def toChars(s):
    import string
    s = string.lower(s)
    ans = ''
    for c in s:
        if c in string.lowercase:
            ans = ans + c
    return ans

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toChars(s))


print isPalindrome('Guttug')
````
### [Fibonacci sequence ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=WbWb0u8bJrU#t=2408) ###

One of the classic example of recursion is [Fibonacci Sequence ](http://en.wikipedia.org/wiki/Fibonacci_number)

TO solve the problem here is the code for the same:-

````
def fibonacci(x):
    """assumes x an int >= 0
        Returns Fibonacci of x"""
    assert type(x) == int and x >=  0
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)



def testFib(n):
    for i in range(n+1):
        print ('fib of', i, '=', fibonacci(i))

testFib(5)
````

---
## References ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/MIT6_00SCS11_lec06.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/lec06.py)

### Problem Sets ###
1. Problem Set 2: Successive Approximation and a Wordgame (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/MIT6_00SCS11_ps2.pdf) 
2. Problem Set 3 (Assigned)
    1. [Problem Set 3 Due on Lecture 7](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging)  

### Further Study ###

1. [4.9 Recursion ](http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap04.html)
2. [Recursion ](http://beastie.cs.ua.edu/cs150/book/index_16.html)
3. [Comparing Recursion and Looping ](http://beastie.cs.ua.edu/cs150/book/index_17.html)
4. [Related Lecture | Dynamic programming I: memoization, Fibonacci, Crazy Eights, guessing ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008)


## Check Yourself ##
### What is recursion? ###

Recursion is a 'Divide and Conquer' technique, in which we have a base case which provides us with a answer immediately, and then we break the function to call itself with reduced input size or smaller size, so that it approaches the base case. 

### What is a recursive case? ###
The part of a function which call's itself with a smaller input is called the recursive case.

### What is a base case? ###
Base case, is the condition in a recursive call, which gives us a answer immediately. Base Case is the end point of recursion.




