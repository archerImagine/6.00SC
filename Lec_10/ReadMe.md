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

All immutable objects can be hashed, that is the reason, the `keys` in the Dictionary are immutable. We need a immutable object for hashing because, we need to get the same value whenever we pass it to hash, but if it mutates it will give me a different value than when we stored.

## [Exceptions ](https://www.youtube.com/watch?v=pjLbxB9TXJs&list=PLB2BE3D6CA77BB8F7#t=1253) ##

## [Class ](https://www.youtube.com/watch?v=pjLbxB9TXJs&list=PLB2BE3D6CA77BB8F7#t=2118) ##


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
### What is a bucket? ###
### What are try blocks for? ###
### What does polymorphic mean? ###
### What is a module? ###
### What is an object? ###


