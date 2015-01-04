# Lecture 05 | Objects in Python #
----

## [Introduction ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=B8is52oxHBw#t=75) ##

Most of the time we need Data Structures to store information, Information which can be stored in a ordered or un-ordered fashion.

There are **3** Data Structures in Python which are used to store information.

1. Tuples
2. Lists
3. Dictionary

**Tuples** and **Lists** are used to store **ordered** information. Which means, the order in which we put elements is the same order we will get it back.  

**Dictionary** are used to store **Un-ordered** information.


## [Tuples ](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=B8is52oxHBw#t=150) ##

Here is a most simple code for Tuples.

````
Test = (1,2,3,4,5)
````

A tuple is identified by `()` parentheses, but there is a catch which we will see later.

### Operations on Tuples ###

These are the operation which you can perform on tuples.

**Index any particular element of the tuple.**

````
print "Test[0]: ", Test[0]      #prints 1
print "Test[1]: ", Test[1]      #prints 2
````
We can use the normal array indexing to index elements of a tuples, and it is zero indexed, so the first element starts at `0`.

**Get the last element of the tuple.**

````
print "Test[-1]: ", Test[-1]        #Prints the last element, i.e 5
````

**Print the length of the Tuple.**

````
print "len(Test): ", len(Test)      #Prints the Length of the tuple.
````

We can also use this Len to get the last element of the Tuple.

````
print "Test[len(Test) - 1]: ", Test[len(Test) - 1]      #Prints the last element, i.e 5
````

**How to initialize a tuple with length 1**
Since the representation of Tuple is `()`, how do Python understand when to parenthesis i.e. group element and when to make it a tuple, let see a example.

````
x = 100
divisors = ()

for i in range(1,x):
    if x % i == 0:
        divisors = divisors + (i,)

print "divisors: ", divisors
````

This syntax `(i,)` actually initializes a Tuple with length 1.

**Slice of Tuple**
We can take a portion or subsequence of a Tuple. For the above example we can generate a sub sequence by this.

````
print "divisors[1:3]: ", divisors[1:3] #prints the 1th index and 2nd index, excluding 3rd.
````

## [Lists](https://www.youtube.com/watch?feature=player_detailpage&list=PLB2BE3D6CA77BB8F7&v=B8is52oxHBw#t=491) ##

Lists are much more complex than tuples for a simple reason that tuples are **immutable**, whereas lists are **mutable**. 

Tuples are immutable means that once you have created a tuple, you cannot change its value. You can create a new tuple with modification to old value, but you cannot modify existing tuple.

Lists on the other hand can be modified as an when required.

We might argue that we have used assignment operator `=` in the past to modify a tuple, but what actually did was changed the object bound to a identifier.

Consider the below example for list.

````
Techs = ['MIT','Cal Tech']          #creates a List of strings
Ivys = ['Harvard','Yale','Brown']   #creates a List of strings

Univs = []                          #empty list.
Univs.append(Techs)                 #Modifes the original List(Univs)

print "Univs: ", Univs              #prints Univs:  [['MIT', 'Cal Tech']]
print "len(Univs): ", len(Univs)    #prints len(Univs):  1
````

List is not bound to contain only homogeneous item, like the list of strings which we created in the above example.

The code to notice in the above example is:-

````
Univs.append(Techs)
````

`append()` : is a method of a class, we can think of method of an alternate to writing a function. This is not same as assignment, this `append` is actually having a side-effect, i.e. modifies the list `Univs`.

Now consider this example which is an extension to the previous example:-

````
Techs = ['MIT','Cal Tech']
Ivys = ['Harvard','Yale','Brown']

Univs = []
Univs.append(Techs)             #Modifes the original List

print "Univs: ", Univs
print "len(Univs): ", len(Univs)

Univs.append(Ivys)              #Modifes the original List
print "Univs: ", Univs
print "len(Univs): ", len(Univs)
for e in Univs:
    print "e: ", e              #pints e:  ['MIT', 'Cal Tech']
                                #      e:  ['Harvard', 'Yale', 'Brown']
````

So the important code to see in the above example is:-

````
for e in Univs:
    print "e: ", e
````
We can use a `for` loop to iterate over a List, just like we used to iterate over any enumerable type. So List can also be enumerated.

We can also use `+` to concatenate a list as shown below:-

````
Flat = Techs + Ivys
print "Flat: ", Flat                #prints Flat:  ['MIT', 'Cal Tech', 'Harvard', 'Yale', 'Brown']
print "len(Flat): ", len(Flat)      #prints len(Flat):  5
````

Consider the below example:-

````
Flat = Techs + Ivys
print "Flat: ", Flat
print "len(Flat): ", len(Flat)

artSchools = ['RISD', 'Harvard']

for u2 in artSchools:
    if u2 in Flat:
        Flat.remove(u2)
````

The code of importance is:-

````
Flat.remove(u2)
````

This will `remove` the element `u2` from the list.

We can also **sort** a list as shown below:-

````
Flat.sort()     
```` 

We can also change the value of individual items of a list like this.

````
Flat[1] = 'UMass'
````

Now the thing to note here is `Flat[1]` is not a identifier.

Now consider this examples:- 

````
L1 = [2]
L2 = [L1,L1]        #The list L2 contains reference to L1
print "L2: ", L2    #prints L2:  [[2], [2]]

L1[0] = 3           #changes the value of L1's element.
print "L2: ", L2    #Prints L2:  [[3], [3]], as L2 points to L1

L2[0] = 'a'         #this removes one of the L1 binding in L2
print "L2: ", L2    #Prints, L2:  ['a', [3]]
````

Now consider this piece of code, in continuation to above.

````
L1 = [2]
print "L2: ", L2    #Prints L2:  ['a', [3]]
````

The line `L1 = [2]` change to link of `L1`, but `L2` stills points to the old value of `L1` so the output will be `L2:  ['a', [3]]` and not `L2:  ['a', [2]]`
An explanation of this can be found here.

* [MIT OCW 6.00SC Code doubt: Kindly see the text for code.](http://www.reddit.com/r/learnpython/comments/2qt2p4/mit_ocw_600sc_code_doubt_kindly_see_the_text_for/)

## [Dictionaries ](https://www.youtube.com/watch?list=PLB2BE3D6CA77BB8F7&feature=player_detailpage&v=B8is52oxHBw#t=2281) ##


A Dictionary differers from a List/Tuples in two ways.

1. First a dictionary is not ordered like list/tuples.
2. The index of dictionary is not integers, which are called `keys`, any immutable type.


Consider the below code:-

````
D = {1:'one','deux':'two','pi':3.14}    #create a dictionary object.

D1 =D

print D1

D[1] = 'uno'
print D1

for k in D1.keys():
    print k, '=', D1[k]
````

We can index through items in a dictionary with the help of keys, as shown below.

````
print D[1]      #prints `one`
print D['deux']      #prints `two`
````

We can iterate over the dictionary by using the keys as shown here:-

````
for k in D1.keys():
    print k, '=', D1[k]
````

So `dict` is a set of `<key, value>` pair. The way the value of Dictionary is printed in not decided, it is random.

To delete an item from the dictionary/list/Tuple we can do it like this:-

````
del d[1]
````

---

## References ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-5-objects-in-python/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-5-objects-in-python/MIT6_00SCS11_lec05.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-5-objects-in-python/lec05.py)

### Further Study ###

1. [Lists](http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap08.html)
2. [Tuples](http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap09.html)
3. [Dictionaries ](http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap10.html)
4. [Tuples as Sequences](http://docs.python.org/tutorial/datastructures.html#tut-tuples)
5. [Dictionaries ](http://docs.python.org/tutorial/datastructures.html#dictionaries)

## Food For thought ##

As mentioned in the Lecture notes, we can have immutable type as a key to dictionary, So the idea to think is can we have tuple as a key to dictionary, because tuple is a immutable data type.

* [Python: Tuples/ dictionaries as keys, select, sort ](http://stackoverflow.com/questions/4878881/python-tuples-dictionaries-as-keys-select-sort)
* [What are some example of tuple as a key of dictionary?](http://www.reddit.com/r/learnpython/comments/2qzoiy/what_are_some_example_of_tuple_as_a_key_of/)

## Check Yourself ##
### What is mutability? ###

A Mutable object can change is value, by the use of APIs like `append()`


### What is the important difference between a list and a tuple? ###

A list is mutable but a tuple is immutable.

### What is cloning? ###

Cloning is the copy of a Mutable object, so that we can work on the Object without actually modifying the actual object.

### What are the important aspects of a dictionary? ###
The important aspect of dictionary are:-

1. There are set in place of a sequence i.e are un-ordered.
2. The index of dictionary are not restricted to int, it can be any immutable type.




