# MIT 6.00SC | Recitation 05 | Quiz 1 Answers and Object-Oriented Programming #

The first 25 min of the Recitation is about Quiz 1 which we will not listen to now. 

## [Object Oriented Programming ](https://www.youtube.com/watch?v=ZFc_utdoexI&list=PLB2BE3D6CA77BB8F7#t=1559) ##

Classes allow to define a custom type. It allows to group data (attributes) and methods together, which is called **encapsulation**. We were already using inbuilt classes like `int`, `float`, `dict` etc.

Classes also allows for Inheritance and Polymorphism. Polymorphism allows to expect the same functionality as the base class.

We can implement class with a dictionary but will it provide all the functionality of a class. Consider the below class implemented as a dict.

````
def makePerson(name,age,height,weight):
    person = {}
    person['name'] = name
    person['age'] = age
    person['height'] = height
    person['weight'] = weight
    return person

def getName(person):
    return person['name']

def setName(person,name):
        person['name'] = name

def getAge(person):
    return person['age']    

def setAge(person,age):
    person['age'] = age     

def getHeight(person):
    return person['height'] 

def setHeight(person,height):
    person['height'] = height

def getWeight(person):
    return person['weight'] 

def setWeight(person,weight):
        person['weight'] = weight   
def printPerson(person):
    print 'Name: ', getName(person)," Age: ", getAge(person)," height: ", getHeight(person), " weight: ", getWeight(person)

def equalPerson(person1,person2):
    return getName(person1) == getName(person2)    
````

Few things to remember in the above class implemented in dict are, these methods `getName()`, `getAge()`,`getHeight()`, `getWeight()` are called **getter** methods.

These methods `setName()`, `setAge()`,`setHeight()`, `setWeight()` are called **setter** methods.

Together these are called accessors and mutator. For accessing values and mutating values.

We can do most of the things which a class can do, using the above implementation, but in a few places it fails.

Like:-
````
print "type(mitch): ", type(mitch)
````
will return
````
<type 'dict'>
````

So a lot of things which we can do using class can also be done using a dict, but it is not intuitive i.e. it does not work like built-in data type.

So lets see how a class implementation will look like.

````
class Person(object):
    def __init__(self, name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # This type of method is called accessor (or getter)
    def getName(self):
        return self.name

    # This type of method is called mutator (or setter) 
    def setName(self,name):
        self.name = name

    # This type of method is called accessor (or getter)
    def getAge(self):
        return self.name

    # This type of method is called mutator (or setter) 
    def setAge(self,age):
        self.age = age

    # This type of method is called accessor (or getter)
    def getHeight(self):
        return self.height

    # This type of method is called mutator (or setter) 
    def setHeight(self,height):
        self.height = height

    # This type of method is called accessor (or getter)
    def getWeight(self):
        return self.weight

    # This type of method is called mutator (or setter) 
    def setWeight(self,weight):
        self.weight = weight        


    # UnderBar methods have special significance in python
    def __str__(self):
        return 'Name: ' +self.name +' Age: ' + str(self.age) +' height: '+str(self.height)+' weight: '+str(self.weight)

    def __eq__(self,other):
        return self.name == other.name
````

Now the major difference comes in these two line of code:-

````
print "type(mitch): ", type(mitch)

print "mitch == sarina: ", mitch == sarina
````

See the first one will print `<class '__main__.Person'>`, so now it is not a `dict`, and second line makes the comparison as same as a inbuilt data type.

One more interesting thing which we should note is this code:-

````
print "Person.getAge(mitch): ", Person.getAge(mitch)
````

This will also print `mitch` age, but the catch here is we are invoking the `getAge()` method on a `Person` class and passing `mitch` as the `self` parameter.

A better implementation of Inheritance and Polymorphism is shown below:-

````
class Shapes(object):
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError
    def __eq__(self,other):
        return self.area() == other.area()
    def __lt__(self,other):
        return self.area > other.area()

class Rectangle(Shapes):
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2
    def area(self):
        return self.side1 * self.side2
    def perimeter(self):
        return 2 * self.side1 + 2 * self.side2
    def __str__(self):
        return 'Rectangle(' +str(self.side1) +', ' +str(self.side2) +')'

class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius ** 2)
    def perimeter(self):
        return 2.0 * 3.14159 * self.radius
    def __str__(self):
        return "Circle(" +str(self.radius) +")"

class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        Rectangle.__init__(self,side,side)
    def __str__(self):
        return "Square(" +str(self.side) +")"


s = Shapes()        
#print s.area() #raise NotImplementedError

r = Rectangle(2,4)
sq = Square(4)
c = Circle(10)

print "Rectangle area: ", r.area()
print "Square area: ", sq.area()
print "Circle area: ", c.area()

print "Rectangle(2,8) == Square(4): ", r == sq
print "Rectangle(2,8) < Square(4): ", r < sq

print "Circle(10) == Square(4): ", c == sq
print "Circle(10) < Square(4): ", c < sq

# Because of polymorphism and inheritance, we don't need to 
# be concerned with which Shapes we are calling area() on

listOfShapes = [c,sq,r]
for shapes in listOfShapes:
    print "type(shapes): ", type(shapes), "shapes.area(): ", shapes.area()


listOfShapes.sort() 
print "----------------"
for shapes in listOfShapes:
    print shapes, "shapes.area(): ", shapes.area()
````

The only thing which we have not studied till now and it is present in the code is shown below:-

````
class Shapes(object):
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError
````

This code forces the sub class to implement the `area()` and `perimeter()` method, else it will throw error.

Also we can do these:-

````
listOfShapes = [c,sq,r]
for shapes in listOfShapes:
    print "type(shapes): ", type(shapes), "shapes.area(): ", shapes.area()
````

Because of polymorphism we can call `area()` on any object, based on the methods available in the base class and it will invoke the correct `area()` method.