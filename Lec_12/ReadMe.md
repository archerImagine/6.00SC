# MIT 6.00SC | Lecture 12 | Introduction to Simulation and Random Walks #


## [Generator Yield ](https://www.youtube.com/watch?v=C2BBAW78fYg&list=PLB2BE3D6CA77BB8F7#t=66) ##

We will start with the example in the previous lecture, see the code here;-

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

class G(MITPerson):
    pass        

class CourseList(object):
    def __init__(self, number):
        self.number = number
        self.students = []
    def addStudent(self, who):
        if not who.isStudent():
            raise TypeError('Not a student')
        if who in self.students:
            raise ValueError('Duplicate student')
        self.students.append(who)
    def remStudent(self, who):
        try:
            self.students.remove(who)
        except:
            print str(who) + ' not in ' + self.number
    def allStudents(self):
        for s in self.students:
            yield s
    def ugs(self):
        indx = 0
        while indx < len(self.students):
            if type(self.students[indx]) == UG:
                yield self.students[indx]
            indx += 1
````

As you can see, `MITPerson` class is a specialization of the base class `Person`. `Person` class have the property like:-

* Get Last Name
* Set the birthday
* Get the age
* 2 Overridden function `__lt__` which helps in comparison, and `__str__` which helps in string representation of the class.

The `MITPerson` class was a specialization of the `Person` class, with added benefits of having a unique `idNum`, which was a class level variable. This class has a method `isStudent()`, which checked if a student is `UG` or `G`.

We also had 2 more specialization classes `UG` for under graduate and `G` for graduate.

Now we can create a course list using this code:-

````
m1 = MITPerson('Barbara Beaver')            
ug1 = UG('Jane Doe')
ug2 = UG('John Doe')
g1 = G('Mitch Peabody')
g2 = G('Ryan Jackson')
g3 = G('Jenny Liu')     

SixHundred = CourseList('6.00')
SixHundred.addStudent(ug1)
SixHundred.addStudent(g1)
SixHundred.addStudent(ug2)
````

Now to get the students name in the course list we can do this:-

````
for student in SixHundred.students:
    print "student: ", student
````

But is this the right way to do this, because we are accessing instance variable directly.

So if we check the `CourseList` class, we have a method `allStudents()` which is implemented like this:-

````
def allStudents(self):
        for s in self.students:
            yield s

def ugs(self):
        indx = 0
        while indx < len(self.students):
            if type(self.students[indx]) == UG:
                yield self.students[indx]
            indx += 1            
````

Now if we see the above 2 methods, we can directly understand that we are not creating a list anywhere which we will return, in place we are using `yield `.

`yield ` is a **generator**, **Generator** is like a return, but the big difference is that, when we use `return ` so any computation which we have done before the return is just thrown out, so we will not save all the instance of student, instead we will be only able to return the first instance which matches, if we are not saving it in a list.

A **generator** is a function, which remembers the point in the body where it was, when it last returned and all local variables.

So `yield ` helps us in running a loop like this without creating the list.

````
print 'Students Squared'
for s in SixHundred.allStudents():
   for s1 in SixHundred.allStudents():
       print "s= ", s ," s1: ", s1  
````

### Further Study on Generator ###

* [What does the yield keyword do in Python?](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python )
* [Improve Your Python: 'yield' and Generators Explained ](http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)


## [Computational Model](https://www.youtube.com/watch?v=C2BBAW78fYg&list=PLB2BE3D6CA77BB8F7#t=976) ##

So now on, the focus will be using computers to solve computational problems. So if we see the history of computation, we used **Analytic Method** to solve it.

### [Analytic Method ](https://www.youtube.com/watch?v=C2BBAW78fYg&list=PLB2BE3D6CA77BB8F7#t=991) ###

Analytic method/ model helps to predict behavior of the system based on some initial conditions and a set of parameters. So this analytic method, helped in making Calculus, Probability theory.

This is a very nice way, but it does not work always. As the amount of information increased these Analytic model were insufficient. 

### [Simulation Model](https://www.youtube.com/watch?v=C2BBAW78fYg&list=PLB2BE3D6CA77BB8F7#t=1080) ###

There were things where making a model was not possible and these are the reason simulation was much more useful, like:-

* System which are not mathematical tractable, very difficult to make physical models.
    - EX: Weather forecasting 
* We are better of with successively refining series of simulation.
* Ofter easier to extract useful intermediate results.
* Computers helped in making this simulation easier.

The idea of simulation is to build a model with the following property.

* Gives useful information about behavior of the system.
    - Gives an approximation to reality
* Simulation models are descriptive not perceptive.
    - 

Simulation will not give exact answer everytime, and also it may not give the same result everytime we run it. So we can run the simulation enough no of time to help us understand/ predict the real behavior of the system.

## [Brownian Motion / Random Walk ](https://www.youtube.com/watch?v=C2BBAW78fYg&list=PLB2BE3D6CA77BB8F7#t=1489) ##

Start with this [Wiki ](http://en.wikipedia.org/wiki/Brownian_motion)

Brownian motion is a example of **Random Walk.**


## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-12-introduction-to-simulation-and-random-walks/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-12-introduction-to-simulation-and-random-walks/MIT6_00SCS11_lec12.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-12-introduction-to-simulation-and-random-walks/lec12.py)

### Problem Sets ###

1. Problem Set 5: RSS Feed Filter (Due)
    1. [Instructions (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-12-introduction-to-simulation-and-random-walks/MIT6_00SCS11_ps5.pdf)
    2.  [Code files (ZIP) ](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-12-introduction-to-simulation-and-random-walks/ps5.zip)
    3. [Solutions (ZIP)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-12-introduction-to-simulation-and-random-walks/ps5_sol.zip)
2. Problem Set 6 (Assigned)
    1. [Problem Set 6 Due on Lecture 14](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-14-sampling-and-monte-carlo-simulation)


### Check Yourself ###
### What is a generator? ###
### What is the difference between yield and return? ###
### What is a model? ###
