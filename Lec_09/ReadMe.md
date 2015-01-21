# Lecture 09 | Memory and Search Methods #

## [Memory ](https://www.youtube.com/watch?v=6wTuOMgTrU4&list=PLB2BE3D6CA77BB8F7#t=22) ##

When we have an list of int's as shown below

````
L = [35, 4, 5, 29, 17, 58, 0]
````

The access to this list is always constant time, for a simple reason being the size of int is constant for a platform and a programming language. 

To see how this constant time access works, lets consider ints occupy 4 units of memory, this units can be 8 bits, 16 bits. So how to access the `i`th element of the list i.e. `L[i]`?

The answer to the above question is, if we know the starting address of the list which is generally the identifier `L`, it will be `L + (4 * i)`

So the above is how a traditional list which we call an array is implemented, it is based on the concept that, each element will have a definite size.

### [List in Python ](https://www.youtube.com/watch?v=6wTuOMgTrU4&list=PLB2BE3D6CA77BB8F7#t=195) ###

As we have seen, how list are, but the python list is different. It is different because, as list is not homogeneous, so it can contain int, float, strings, dicts etc.

So how would List be implemented in Python.

One of the very immediate and oldest way of doing its is a **Linked List**. In a linked list, every element have a data part and a pointer part which pointed to the next element. The end of the list is identified by a Null element. The cost of accessing `i`th element of the list is `i` step which is order `i`. So in this case, binary search will not be `nlogn` but it will be `n` as I have to traverse each element of the list.

Instead python uses a array of pointers, as explained here, [Python list implementation ](http://www.laurentluce.com/posts/python-list-implementation/). This concept is called **Indirection**. So we are same as the initial array of ints concepts because each element of list is a pointer, so I can now access each element in constant time.

**Indirection** is a very powerful programming concepts. All problem of computer sc. can be solved by adding a level of indirection. Indirection is bad if we have two many indirection as is the value stored using indirection is very far apart the memory cache may not function as we expect.

So with help of indirection we can achieve binary search of the order of `nlogn`. But there is a catch, the catch is we assume that for binary search the list is already sorted.

### [Amortized Complexity ](https://www.youtube.com/watch?v=6wTuOMgTrU4&list=PLB2BE3D6CA77BB8F7#t=660) ###

So who is sorting the list for using with binary search. So if The question is to search an element, does it make sense to follow this algorithm

1. Sort L
2. Use Binary Search

The thing on which this depends if the efficiency of these steps. 

We know that Step 2 is `O(log(Len(L)))`, and say step 1 takes `O(?)`, so every thing depends on how much time does Sort take.

We also know that if we use just Linear search it is of efficiency `O(n)`.

The decision to use the sort + Binary search combination or Linear search depends on how much time `O(?)` takes.

So every thing depends on this equation.

````
O(?) + O(log(Len(L))) < O(n)
````

So for the combination of Sort + binary search to work as shown in above equation, sort that is `O(?)` should be sub linear time. But there is no algo which can sort a list in sub liner time. Because we cannot get a list sorted in ascending or descending without looking as each element of the list.

The question arise that if we cannot do sort in sub linear time, then why not use Linear search for all our search operation.

The reason being, most of the time we are interested in Amortized Complexity. The idea behind amortization is that if we can sort the list once and end up searching many times, the cost of sort can be allocated to each of the different search which we are going to do. If we do enough searches, it does not matter how much time sort takes.

I we plan on performing `K` searches. So as per the below equation,

````
O(?) + k*O(log(len(L))) < K * O(Len(L))
````

everything depends on `O(?)` and the value of `k`.

## [Sorting ](https://www.youtube.com/watch?v=6wTuOMgTrU4&list=PLB2BE3D6CA77BB8F7#t=1072) ##

Here is a video telling how not to do Sorting, [Barack Obama - Computer Science Question ](https://www.youtube.com/watch?v=k4RRi_ntQc8)

### [Selection Sort ](https://www.youtube.com/watch?v=6wTuOMgTrU4&list=PLB2BE3D6CA77BB8F7#t=1244) ###

Here is the code for selection sort:-

````
def selectionSort(L):
    """
        Assumes that L is a list of elements which can be compared using >
        Sorts L in asscending order
    """
    print "len(L): ", len(L)
    for i in range(len(L) - 1):
        print "::::::::::::::::i: ", i
        #Invariant: the list L[:i] is sorted.
        minIndex = i
        minValue = L[i]
        j = i + 1
        while j < len(L):
            print "j: ", j
            if minValue > L[j]:
                minIndex = j
                minValue = L[j]
            j += 1
            temp = L[i]
            L[i] = L[minIndex]
            L[minIndex] = temp 
            print "L: ", L
L = [35, 4, 5, 29, 17, 58, 0]       
print L
selectionSort(L)    
print L
````

Selection sort is based on the concept to maintain an **Invariant.** Invariant is some thing which is invariantly true. 

The invariant in the selection sort is that, we will have a pointer into the list, which will divide the list in **prefix** and **suffix**. The Invariant which we are going to maintain is **The prefix is always sorted.**

In selection sort, the prefix is empty to begin with, and the suffix is the len of list, and with each iteration, the prefix will increase in size and suffix will decrease in size. We will complete when prefix is len of list and suffix as 0.

What is the complexity of selection sort?

There are practically 2 things happening:-

1. Comparison
2. Swaps

Since we do both swaps and comparison together, we can just check the number of comparison which we will do.

So we have to do `n` comparison for the first time, then `n-1` and so on, so this will be the complexity:-

````
n + (n-1) + (n-2).......+3+2+1 = O(n^2)
````

So Can we do better.

### [Merge Sort ](https://www.youtube.com/watch?v=6wTuOMgTrU4&list=PLB2BE3D6CA77BB8F7#t=1771) ###

We can use Divide and Conquer to sort, The main concept behind this.

1. Chose a threshold input size n(0), smallest problem.
2. How many instances at each division.
3. Combine the sub solutions.

So we will focus on the Step 3: which says, if we have two sorted list, we can combine them easily.

Consider the below example, which has two list.

````
L1 = [1,5,12,18,19,20]
L2 = [2,3,4,17]
````

So the steps of merge is:-

1. Compare the first element of L1 with first element L2
2. Choose the element which is smaller, and this is the smallest element of the merged list. in the above example it will be `1`
3. Now compare the next element of L1 with first element of L2
4. Choose, in this case it will be `5` and `2`, we will put `2` in the merged list.

Finally we will have a sorted list:-

````
L = [1,2,3,4,5,17,18,19,20]
````

The efficiency will be dependent on

1. No of copies O(Len(L1) + len(L2))
2. No of comparison O(Len(L))

So it will be linear.

Now we will consider Step 1 and Step 2, we will divide the list till it has only one element, and then start merging till the size if of Len(L)/2, so the complexity will be O(log n) for merge.

So total complexity will be; `O(nLogn)`.

Here is the code of Sort:-

````
def mergeSort(left,right,lt):
    """
        Assumes left and right are sorted list.
        lt defines the ordering on the elements of the list.
        Returns a new sorted(by lt) list containing the same elements as 
        left + right would contain.
    """
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if lt(left[i],right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def sort(L,lt = lambda x,y: x < y):
        """
            Returns a new sorted list containing the same elements as L
        """ 
        if len(L) < 2:
            return L[:]
        else:
            middle = int(len(L)/2)
            
            left = sort(L[:middle],lt)
            right = sort(L[middle:],lt)
            print "left: ", left, "right: ", right
            return mergeSort(left,right,lt)

L = [35, 4, 5, 29, 17, 58, 0]
newL = sort(L)
print 'Sorted list =', newL         
````

One Important piece of code is:-

````
def sort(L,lt = lambda x,y: x < y):
````

The 2nd argument of sort is a function itself, which will do a comparison. With the use of `lambda`. Which helps in building a function on the fly.

````
lambda x,y : x < y
````

Means the function takes two argument `x` and `y`, and returns `x < y`.
## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-9-memory-and-search-methods/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-9-memory-and-search-methods/MIT6_00SCS11_lec09.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-9-memory-and-search-methods/lec09.py)

### Further Study ###

1. **Readings**
    1. [8.7. Sets Unordered collections of unique elements](http://docs.python.org/library/sets.html)
2. **Related Lectures**
    1. [6.01SC Introduction to Electrical Engineering and Computer Science I.](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/index.htm)
        1. [Search Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-4-probability-and-planning/search-algorithms)
        2. [Optimizing a search ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-4-probability-and-planning/optimizing-a-search)
    2. [6.006 Introduction to Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008)
3. [What's the difference between list and tuples?](http://stackoverflow.com/questions/626759/whats-the-difference-between-list-and-tuples)


### Check Yourself ###
### What is indirection (in computing)? ###
### We know that a linear search works on all lists and is O(len(L)). Can we sort a list in sub-linear time? ###
### Can we even do it in linear time? ###
