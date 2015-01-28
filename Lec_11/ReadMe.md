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

## [Inheritance ](https://www.youtube.com/watch?v=FBpe3xFvPrQ&list=PLB2BE3D6CA77BB8F7#t=1338) ##

When we design program using OOP, we are not looking at the implementation details, we should be able to think in terms of abstraction. Inheritance is a important feature in this regards.

Inheritance is used to setup hierarchy of Abstraction. The idea is to identify the similarity between most of the object and make a class which will have this common functionality. We should be able to identify if there is a shared attributes between different class.

So to design a MIT Database the base class will look like this:-

````
import datetime

class Person(object):
    def __init__(self, name):
        #Create a person with name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            # print "__init__: firstBlank: ", firstBlank
            self.lastName = name[firstBlank+1:]
        except :
            self.lastName = name
        self.birthDay = None
    def getLastName(self):
        #returns self's last name
        return self.lastName
    def setBirthday(self,birthDate):
        #assumes that self's birthday is of type datetime.date
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthDay = birthDate
    def getAge(self):
        #assumes that self's birthday is set
        #returns self's age in days
        assert self.birthDay != None
        return (datetime.date.today() - self.birthDay).days
    def __lt__(self,other):
        #returns True if self name is lexicographically greater
        #than other's name, and False Otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        return self.name
````

Now lets dissect this code:-

* `def __init__(self, name):` is the same as before, nothing new, it will be called when the object is created, with the parameter `name`.
* `def getLastName(self):` is a method which will return me the value of the attribute `lastName`, the reason this method is present is because we do not want user of this abstraction to have access to the data attribute `lastName` directly, so that we can put some checks in place.
    - Mostly we will have method which will fetch `get` something, which will return the information about the instance of the class.
* `def setBirthday(self,birthDate):` this is a set method, the reason for its existence is similar to get method.
* `def __lt__(self,other):` this is another of those magic method, this will be used to compare two object of `Person` type. The reason we are using `__lt__` and not any function name as `less` etc, is because `__lt__` is predefined in Python, just like `__str__` which will be called automatically when we will do comparison `<` on Person object. So this Person class will behave exactly like any inbuilt data type, but if we have a special function name like `less` though it will get the job done, but it will not be same as inbuilt data type.

Lets consider this class:-

````
class MITPerson(Person):
    nextIDNum = 0
    def __init__(self, name):
        #super(MITPerson, self).__init__()
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIDNum
        MITPerson.nextIDNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return type(self)==UG or type(self)==G
````

* The class `MITPerson` is a subclass of `Person`, because we are passing `Person` as a argument in place of `Object` which we were passing till now, in this line, `class MITPerson(Person):`, so what this means is I want all the attributes of class `Person`, but `MITPerson` will have some additional attributes and functionality.
* `nextIDNum = 0` is a **class variable**, that means this is common to the class and not to just one object of the class. So this is shared across object of this class type.
* `def __lt__(self, other):` The base class, `Person ` also had `__lt__` method, which I am **overriding** here. Overriding helps in modifying the base class methods to suits the sub class attributes. Because in the case of `MITPerson` we want to check the comparison based on `nextIDNum` and not the `firstName` or `lastName` basis as done in the `Person ` class.
    - Consider that some time we need to use the functionality provided in the super class and not the overridden functionality in the subclass, we can use it by calling `Person.__lt__(p1, p2)`
* `p4 < p3` : when we do comparision like this, what it will do is take `p4`, checking is `__lt__` method and pass `p3` as a argument.

Now consider this new class:-

````
class UG(MITPerson):
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None
    def setYear(self, year):
        if year > 5:
            raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year
````

Lets dissect this code:-

* `class UG(MITPerson):` `UG` is a subclass of `MITPerson.`
* `MITPerson.__init__(self, name)`: What is piece of code is doing is that it will call `MITPerson`s `__init__` and then continue to initialize itself.
* What happens when we call this `ug2 < ug1`?
    - The reason for this question is because we do not have `__lt__` function in `UG` class, so since it is inheriting from `MITPerson`, it will invoke the `__lt__` of `MITPerson`, if it was not present in `MITPerson`, then it will go further up in the hierarchy till it reaches `object `.

Now consider this class:-

````
class G(MITPerson):
    pass

g1 = G('Mitch Peabody')
````

* Now as you can see the class `G` is not doing anything just saying `pass`, this means, `G` is a `MITPerson` with no special property.
* The reason for doing this is we can check for `type`. As this will be `type(g1)` will be `G`

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

The answers to the above question can be found [here](http://www.reddit.com/r/learnpython/comments/2tukft/mit_ocw_few_question_about_oop_in_python_based_on/).