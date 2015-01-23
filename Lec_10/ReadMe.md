# Lecture 10 | Hashing and Classes #


## [Hashing ](https://www.youtube.com/watch?v=pjLbxB9TXJs&list=PLB2BE3D6CA77BB8F7#t=39) ##

Hashing is the concepts used in Dictionary are implemented in Python. This provides us with a very efficient search mechanism, but at the cost of space(Memory).

For understanding the concepts of hashing we will consider that we will use hashing on a set of integers.

Let consider a integer `i`, which we pass it to a `hash()` function, it generates another integer in some range.

````
hash(i) ----> 0 ... K, for some constant K.
````

We will use this new integer to index into a list of lists. Each of these list of list is called a **Bucket**, So a Bucket will itself be a list. We already know that we can find `i`th element of a list in constant time.

So when we get an integer after hashing, it will be an index in the list of list, and once we identify the list, we can search in that list using efficient techniques.

So lets understand this using some code:-

````
numBuckets = 47     #This is ugly, we will better it soon.

def create():
    global numBuckets
    hSet = []
    for i in range(numBuckets):
        hSet.append([])
    # print "[XYZ]: create() hSet: ", hSet, " type(hSet): ",type(hSet)
    return hSet

def hashElem(e):
        global numBuckets
        return e % numBuckets

def insert(hSet,i):
    hSet[hashElem(i)].append(i)
    # print "[XYZ]: insert() hSet: ", hSet, " type(hSet): ",type(hSet)

def remove(hSet,i):
    newBucket = []  
    for j in hSet[hashElem(i)]:
        if j != i:
            newBucket.append(j)
    hSet[hashElem(i)] = newBucket
    print "[XYZ]: remove() i: ", i," hashElem[i]: ", hashElem(i), " hSet[hashElem(i): ", hSet[hashElem(i)]

def member(hSet,i):
        return i in hSet[hashElem(i)]

def testOne():
    s = create()        
    for i in range(40):
        insert(s,i)
    print "[XYZ]: S: ", s
    insert(s,325)
    insert(s,325)
    insert(s,9898900067)
    print "[XYZ]: S: ", s
    print "[XYZ]: ,member(s,325): ",member(s,325)
    remove(s,325)
    print "[XYZ]: After Remove, member(s,325): ",member(s,325)
    print "[XYZ]: member(s,9898900067)",member(s,9898900067)

testOne()   
````

Now lets discuss the functions one at a time:-

````
def create():
    global numBuckets
    hSet = []
    for i in range(numBuckets):
        hSet.append([])
    # print "[XYZ]: create() hSet: ", hSet, " type(hSet): ",type(hSet)
    return hSet

````

Now this `create()` function, will have a list `hSet` which will be initialized to contain empty list.

````
def hashElem(e):
    global numBuckets
    return e % numBuckets
````

This is the actual function which is performing hashing, what it is doing, we will pass any element, and it will return a integer which is the remainder, so we can give any range of value, and it will return in the range of `0` to `9`.

````
def insert(hSet,i):
    hSet[hashElem(i)].append(i)
````

This `insert()` function, will take `hSet` and `i` as parameter and insert `i` at the list position identified by `hashElem()`.


````
def remove(hSet,i):
    newBucket = []  
    for j in hSet[hashElem(i)]:
        if j != i:
            newBucket.append(j)
    hSet[hashElem(i)] = newBucket
    print "[XYZ]: remove() i: ", i," hashElem[i]: ", hashElem(i), " hSet[hashElem(i): ", hSet[hashElem(i)]
````

Now the `remove()`, is little complex, what it is doing is, it identifies the list of list by passing `i` to the `hashElem()` which returns the index of the list, and then iterate over this list to identify the element, along with duplicity and remove them.


````
def member(hSet,i):
    return i in hSet[hashElem(i)]
````

The `member()` function, just identifies, the list of list by passing it to `hashElem()` and then checks if `i` is present in this list.


Now the question arises why we need the remainder functionality in the `hashElem()` method, why not have just `boolean` values. The reason being, the basic concept of hashing is **"Many To One"**, because we have infinite number of positive integers, which will hash to only `47` elements, so there has to be multiple values mapping to a single index.

When more than 2 elements hash to one index, we have something called **Collision**, then there are multiple ways of solving Collision, we have used **Linear Rehashing** to avoid collision in the above case. Which is the List of List.

The complexity of the `member()` will depends on the length of a bucket, and what will define the length of a bucket? It will depend of number of total buckets which is `47` in the above case.

So the chances of collision is less, when we have a million bucket, but more when we have only `2` bucket.

A very good Hash function is identified by how distributed it expands its values.

In python, Dictionary use this concepts, so it looks into the `keys` and creates a large enough bucket to evenly distribute values, if we are left out of even distribution, it rehashes everything with a large bucket.

Any type of immutable objects can be hashed, that is the reason, that `keys` in the Dictionary are immutable. We need a immutable object for hashing because, we need to get the same value whenever we pass it to hash, but if it mutates it will give me a different value than when we stored.

We can also hash a string and not only integers, but a string has to be converted to a integer with some logic, kindly see below the code for doing it with strings:-

````
def hashElem(e):
        global numBuckets
        if type(e) == int:
            val = e
        if type(e) == str:
            val = 0
            shift = 0
            for c in e:
                val = val + shift * ord(c)
                shift += 1
        return val % numBuckets
````

The following function `ord(c)` gives a ASCII code of the character.

## [Exceptions ](https://www.youtube.com/watch?v=pjLbxB9TXJs&list=PLB2BE3D6CA77BB8F7#t=1253) ##

Exceptions are everywhere in python, The below code will raise a exception.

````
test = [1,2,3]
test[12]
````

This will give the below error.

````
Traceback (most recent call last):
  File "<string>", line 1, in <module>
IndexError: list index out of range
````

Anything ending with `Error` is a exception, like `IndexError` is a exception.

The above exception is **Unhandled Exception**, because it crashes once exception happens.

The Unhandled exception can be handled, so this is a perfect flow of control option in python.

The general syntax of handling exception is given below.

````
try:
    #some Code
except:
    #Some exception code.
````

Starts with instruction in `try` block, and nothing wrong happens it will jump to instruction after the `except` block, but if a exception is raised it will stop execution of `try` block and execute `except` block. `try` can be nested.

Consider the below example:-

````
def readVal(valType,requestMsg,errorMsg):
    numTries = 0
    print numTries
    while numTries < 4:
        val = raw_input(requestMsg)
        try:
            val = valType(val)
            return val
        except ValueError:
            print errorMsg
            numTries += 1       
    raise TypeError('Num tries excedded.')
````

So the above code does a very simple thing, it takes 3 inputs 

* valType : which is a type, since everything is a object in python, we can pass a type to function
* requestMsg : This is a string
* errorMsg : This is also a string

Now if we pass `int` as a first argument, and input string to it, it will print the error msg and then try again.

Since the method `readVal` raises an exception, we can also handle it in main code like this:-

````
try:
    a = readVal(int,"Enter int: ","Not a Int")
    print "a: ", a
except TypeError, s:
    print "s: ", s
````

If we do not give the `except` some name like I have given here `except TypeError, s:`, it will go in that block for all exception. So it will catch any exception, and usually we do not follow this practice to leave the `except` name empty, because it basically means I have not anticipated the error.

## [Class ](https://www.youtube.com/watch?v=pjLbxB9TXJs&list=PLB2BE3D6CA77BB8F7#t=2118) ##

We have already seen the concept of **Modules**, which is a collection of related function.

Example:-

````
import math

math.log()
````

The module helps in importing a lot of related information at once, and then use the `.` notation to access the related function like `Math.log`. The `.` notation helps in identifying the context.

Like we can have one method `member()` in two modules `set` and `table`, so when we call with `set.member()` we know which one to invoke. `.` notations avoids conflicts.

Class is like a module, it is collection of Data and Functions. Function which operates on the data, they are bound together, so we can invoke with proper context. This is the key to **Object Oriented Programming**. 

When we did it `L.append()`. Where `L` provides the context.

The data of a class are called **attributes**.

**Message Passing Metaphor** : When we write `L.append(e)`, I am passing a message `append(e)` to the object `L`.Then the message is identified by object `L` and then executes the corresponding method.

**Method is a function associated with a Object.**

Class is a collection of objects with identical characteristics that form a type. So class introduces new type into the language. `Dict` and `List` are built in classes.

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes/MIT6_00SCS11_lec10.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes/lec10.py)

### Problem Sets ###

1. Problem Set 4: The Caesar Cipher (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes/MIT6_00SCS11_ps4.pdf)
    2. [Pseudocode (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes/MIT6_00SCS11_ps4-pseudo.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes/ps4.zip)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-10-hashing-and-classes/ps4_sol.zip)
2. Problem Set 5 (Assigned)
    1. [Problem Set 5 Due on Lecture 12](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-12-introduction-to-simulation-and-random-walks)


### Further Study ###

1. **Readings**
    1. [12. Classes and objects](http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap12.html)
2. **Related Lectures**
    1. [6.006 Introduction to Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008)


### Check Yourself ###

### What does hashing do? ###
It converts an large range of value/objects into a small fixed range values.

### What is a bucket? ###
A list of item which have the same hash value.

### What are try blocks for? ###
try block are piece of code where we do error prone things because the program's input may not be within the control of the program.

### What does polymorphic mean? ###
Taking multiple forms, like `def readVal(valType,requestMsg,errorMsg)`, so we can pass in any `valType`

### What is a module? ###
Module is a collection of related function.


### What is an object? ###
A collection of data and functions which operates on that data.

