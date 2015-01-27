# Lecture 11 | OOP and Inheritance #

## Introduction ##

Object oriented programming started with the development of these 2 programming language.

* [CLU](http://en.wikipedia.org/wiki/CLU_%28programming_language%29)
* [Smalltalk ](http://en.wikipedia.org/wiki/Smalltalk)

These languages were not able to propel the OOP concepts till the advent of [Java ](), followed by **C++** and **Python**.

## [Abstract Data Type ](https://www.youtube.com/watch?v=FBpe3xFvPrQ&list=PLB2BE3D6CA77BB8F7#t=123) ##

The core of all Object Oriented programming is **Abstract Data Type**. The fundamental use of Abstract data type is that we can add user defined data type which behave just like a Built in Data type.

The question arises that why do we call it **Abstract** Data Type? and not just data type.

The reason for this is, because we define

* **Interface**: Explains what the methods do. What they do at the level of the user and not how do they do it.
    * **Specification** : The idea of interface is dependent on Specification, Which is a set of rules which lets what a method does.

Let See an example for this:-

````
class intSet(object):
    """An intSet is a set of integer."""
    def __init__(self):
        """Create an empty set of integer"""
        self.numBuckets = 47
        self.vals = []
        for i in range(self.numBuckets):
            self.vals.append([])
    def hashE(self,e):
        #Private Function, should not be used outside the class.
        return abs(e)%len(self.vals)
    def insert(self,e):
        """Assumes e is an integer, and insert e into self"""
        for i in self.vals[self.hashE(e)]:
            if i == e:
                return
        self.vals[self.hashE(e)].append(e)
    def member(self,e):
        """Assumes e is an integer,
            Returns True, if e is in self, else False"""
        return e in self.vals[self.hashE(e)]
    def __str__(self):
        """Returns a string representation of self"""
        elem = []
        for buckets in self.vals:
            for e in buckets:
                elem.append(e)
        elem.sort()
        result = ''
        for e in elem:
            result = result + str(e) +','
        return '{' +result[:-1]+"}"
````

Lets dissect the code written above.

* `class intSet(object)`
    * The first thing which we find is, we are defining a new data type called `intSet`. Which is done by using the keyword `class`.
    * The parameter is a `object`. We will discuss this `object` when we discuss about inheritance.
* `def __init__(self):`
    * when we see, anything with `__` in the name like `__init__`, it has a special meaning, particularly this function `__init__` is called when a object of `intSet` is initialize, which initialize two variable/ attribute.
        * `self.numBuckets = 47`
        * `self.vals = []`
    + `self`: what does this means. To understand this, consider the below example:-
    ````
    s = intSet()
    print self.numBucket
    ````
    The above code gives error.
    ````
    NameError: name 'self' is not defined
    ````
    The reason being, `self` is not available in the global scope.This code will however work.
    ````
    print s.numBuckets
    ````
    To understand this, we can say `numBuckets` and `vals` are attributes of the object `s` which is instance of the class `intSet`. `self` is used to refer the object being created.
    We can also note that `__init__` takes a parameter `self`, but when we created `intSet()` we did not pass any object, the reason being, the `__init__` has a special magic, in which it take `self` as a parameter, even when it is not passed.
* `def hashE(self,e):` 
    - This is private function, as specified by the comment in the function, this function is not exposed as a interface. This is a convention and not enforced by the language, so this means that we can call this outside, just like any other interface, But good programmers always **Program to the specification and not implementation.**
* `def insert(self,e):`
    - This is a exposed method, if we see the formal parameters of these we have two arguments, `self` and `e`.
    - We call `insert` like this `s.insert(i)`, what this does is, `s` before the dot is passed to the `self` formal parameter and `i` is passed to `e`.
    - By convention, the first argument is always called `self` in python. It is not enforced, but it is a convention.
* `def __str__(self):`
    - This is again a special method, what is means is when we call `print "s: ", s`, it will invoke `__str__`.
* We should not reference the data element of the class like, `print "s.vals: ", s.vals`, because this is not part of the specification. So if we reference it, it might break in future. So the implementation of `vals` may not be present in the future, so the program should work. Always remember the golden words **Program to the specification and not implementation.** This concept is called **Data Hiding**.

### [Data Hiding ](https://www.youtube.com/watch?v=FBpe3xFvPrQ&list=PLB2BE3D6CA77BB8F7#t=1043) ###

This is the only fundamental which makes Abstract data type useful. Java provides a mechanism to enforce data hiding, but not in python. 

The things which we are hiding are:-

* **Instance variables**: Variables which are associated with each instance of the class. ex. `numBuckets` and `vals`.
    - We get a new copy of these variables when we create a new instance.
* **Class Variable**:  Variables which are associated with a class.
    - We only have one copy of the class variable, like we have just one `Class`


[20:22](https://www.youtube.com/watch?v=FBpe3xFvPrQ&list=PLB2BE3D6CA77BB8F7#t=1222)

## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-11-oop-and-inheritance/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-11-oop-and-inheritance/MIT6_00SCS11_lec11.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-11-oop-and-inheritance/lec11.py)

### Further Study ###

1. [StackOverFlow | Python - why use "self" in a class?](http://stackoverflow.com/questions/475871/python-why-use-self-in-a-class)


### Check Yourself ###
### What is an instance?###
### What is an abstract data type? ###
### What is encapsulation? ###
### What is data hiding? ###
### What functions can subclasses use? ###

### Question in mind ###

* Since python does not enforce data hiding, is there a naming convention to identify private members of a class.
* Why is Data hiding not enforced in Python like Java.
