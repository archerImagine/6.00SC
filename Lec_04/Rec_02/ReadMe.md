# MIT 6.00SC | Recitation 02 | Loops, Tuples, String and Functions #
---

## [Loops](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=26) ##

These are the 2 types of loops already covered.

1. `for` loops
2. `while` loops

### [while](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=42) ###

The typical `while` loop has a syntax as given below:-

````
while <condtion>:
    <body>
````

In the above code, `<condition>` means some expression which evaluates to either `true` or `false`, when it evaluates to `false` the loop terminates. The `<body>` means block of code which executes when the condition of the loop is `true`.

The above sample will give some sample code, as mentioned below.

````
#Print even number from 2 to 10
a = 2

while (a < 10):
    a += 2
    print "a = ", a #a is not a good variable, use evenNumber instead
````

In the above code **what is the decrementing function?**, A decrementing function as already described earlier is a piece of code which moves the loop closer to termination. In the above code it is `a += 2` as we are moving closer to `10`.


### [for ](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=220) ###

The syntax of for loop:-

````
for iterating_var in sequence:
   statements(s)
````

In the above code, the `sequence ` should be something on which the loop can enumerate i.e. like an array, tuple etc. Enumerate means we can take one element at a time from the list and then do operation on them.

As sample implementation of a `for` loop will be

````
for i in (2,4,6,8,10):
    print "i = ", i
````

This `for` loop does the same thing as the `while` loop code above, but this way of representing is not efficient enough.

`for` loops iterate over enumerable items.


#### [Range](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=367) ####

The `range` function takes, 1,2 or 3 parameters and returns a list of integers.

An example of `range` taking just one parameters:-

````
print "range(100): ", range(100)
````

So the above code will give the integer from `0` to `100`.

An example of `range` taking just two parameters:-

````
print "range(1,100): ", range(1,100)
````

So this will print integers from `1` to `100`. so with 2 parameters, the first parameter gives the starting point of range (inclusive), and the second parameter gives the end point of range (exclusive).

The final variant of `range` is:-

````
print "range(1,100,2): ", range(1,100,2)
````

The first 2 arguments behave as given with 2 parameters, the 3rd argument if the step, i.e. the increment, so the above code prints all the odd number from `1` to `100`.

we can also go in reverse direction, with the step being negative as shown below.

````
print "range(100,1,-1): ", range(100,1,-1)
````

so this code prints number from `100` to `1` in the decrementing fashion.

**Help**: We can get help on any inbuilt function in python using `help(range)`

So this will print:-

````
>>> help(range)
Help on built-in function range in module __builtin__:

range(...)
    range(stop) -> list of integers
    range([start,] stop[, step]) -> list of integers

    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

````
This can be used on any function in python. Few important points for **help**

* the description  `range(stop) -> list of integers` the arrow mark represent that it returns a list of integers.
* the `[` in the arguments list tells that the arguments is optional. so in the above output it means in the `range` function, `start` and `step` are optional parameters.


So with the knowledge acquired on `range` function, the previous `for` loop can be further optimized as:-

````
for i in range(2,11,2):
    print "i = ", i
````

So with the help of `range` function we can avoid the long list of integers we were giving like `(2,4,6,8,10)`

We cannot create a `range` of `float`, as it will be truncated to integers. So it can give a waring or a error depending on the python version.

````
print range(1.0, 10.0)
````

The above code gives as error to me.

````
Traceback (most recent call last):
  File "rangeFloat.py", line 1, in <module>
    print range(1.0, 10.0)
TypeError: range() integer end argument expected, got float.
````

## [Tuple ](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=670)##

Tuple is a non-scalar data type that can hold many homogeneous or heterogeneous items. Non-Scalar can hold more than one element like string. The literal syntax of tuple is given below.

````
tupleOfNumber = (3.14,2,1,-100,240)
tupleOfString = ("What", "is","my","name?")
````

We can also mix data type in a tuple, like string and number together.

To access individual items of a tuple we can do indexing as shown below, and tuple indexing starts at `0`

````
print "tupleOfNumber[0]: ", tupleOfNumber[0]  #print 3.14
print "tupleOfString[0]: ", tupleOfString[0]  #print what
print "tupleOfString[-1]: ", tupleOfString[-1] #print name?
````

Negative index is also possible, which means from the end return the item at the index, so in the above example it prints the last element.

When you give a index which is outside the bound like in this example:-

````
print "tupleOfString[4]: ", tupleOfString[4]
````

it gives a error:-

````
tupleOfString[4]:
Traceback (most recent call last):
  File "tuple.py", line 10, in <module>
    print "tupleOfString[4]: ", tupleOfString[4]
IndexError: tuple index out of range
````

We can also get the length of the tuple so that we do not get into `tuple index out of range` error. The api to use is `len() `.


`````
print len(tupleOfString)    #print 4
`````

Like mentioned earlier, tuple can hold different data type, as shown below.

````
tupleOfMixed = (3.14, 'is', 'an imperfect', 'representation')
````

We can also have tuple which can contain other tuple, as shown below.

````
tupleOfTuple = (("astuff", "just"), 'got', 'real')
print "tupleOfTuple: ", tupleOfTuple            #prints (('astuff', 'just'), 'got', 'real')
print "tupleOfTuple[0]: ", tupleOfTuple[0]      # prints ('astuff', 'just')
print "len(tupleOfTuple): ", len(tupleOfTuple)  #print 3
````

The length of the above tuple is `3`

A tuple is immutable, i.e. we cannot modify existing tuple. Like this below code:-

````
tupleOfNumber[1] = 3
````

will give an error as:-

````
Traceback (most recent call last):
  File "tuple.py", line 22, in <module>
    tupleOfNumber[1] = 3
TypeError: 'tuple' object does not support item assignment
````

Tuple also support **slice** operation. Consider the below code;-

````
print "tupleOfNumber[1:3]: ", tupleOfNumber[1:3]    #print (2, 1)
print "tupleOfNumber[:2]: ", tupleOfNumber[:2]      #print (3.14, 2)
print "tupleOfNumber[1:]: ", tupleOfNumber[1:]      #print (2, 1, -100, 240)
print "tupleOfNumber[:-1]: ", tupleOfNumber[:-1]    #print (3.14, 2, 1, -100)
````

Lets dissect the above code:-

* `tupleOfNumber[1:3]` `1` is start index, `3` is end index seperated by `:`, it will give tuple index from `1` to `3-1` i.e = `2`.
* `tupleOfNumber[:2] ` implicit start is `0`
* `tupleOfNumber[1:]` implicit end is end of the tuple
* `tupleOfNumber[:-1]`  from 0 to (last element - 1)
* `tupleOfNumber[:]` complete string

We can also iterate over a tuple as shown below:-

````
for i in tupleOfNumber:
    print i
````

As discussed earlier, tuple are immutable, i.e. we cannot modify individual element of the tuple but we can modify a tuple by creating a new tuple with the same name as shown below.

````
print "Before Modification: ", tupleOfNumber
tupleOfNumber = tupleOfNumber + (100,24)
print "After Modification: ", tupleOfNumber
````

This line of code `tupleOfNumber = tupleOfNumber + (100,24) `, works because, it creates a new `tupleOfNumber` with data from old `tupleOfNumber` and add the `(100,24)` tuple.

Till now we created tuple with multiple entry, i.e. more than 1 elements. There is a catch when we create a tuple with 1 element.

Consider the below code:-

````
oopsie = (50)                   #() is used for grouping in this case.
print "oopsie: ", oopsie        #oopsie is not a tuple, just a number

onsie = (50,)                   #() in this case, it is used as a tuple, identified be the lone comma at the end.
print "onsie: ", onsie          #onsie is a tuple.
````

## [Strings](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=1667) ##

Strings are very much like tuples, i.e. non-scalar type, immutable, you can enumerate over them. Consider the below code which shows these property.:-

````
name = "Mitch"
print "name: ", name
print "name[0]: ", name[0]

for i in name:
    print i
````

To show the immutable property:-

````
name[0]  = "A"
````

gives an error:-

````
Traceback (most recent call last):
  File "strings.py", line 8, in <module>
    name[0]  = "A"
TypeError: 'str' object does not support item assignment
````

It also supports **slice** operation as shown below.

````
print "name: ", name
print "name[1:3]: ", name[1:3]      #print it
print "name[:2]: ", name[:2]        #print Mi
print "name[1:]: ", name[1:]        #print itch
print "name[:-1]: ", name[:-1]      #print Mitc
````

Space is also a character in string.

We also get length of a string like this;-

````
print "len(name): ", len(name)      #print 5
````

Strings also supports some api's, the usage is as given below:-

````
print "name.upper(): ", name.upper()                        #print MITCH
print "name.lower(): ", name.lower()                        #print mitch
print "name.find('i'): ", name.find('i')                    #print 1
print "name.replace('M', 'P'): ", name.replace('M', 'P')    #print Pitch
````

* `upper()`: will change all the character to uppercase.
* `lower()`: will change all the character to lowercase.
* `find('i')`: it will find the character `i` index, return `-1` when pattern not found.
* `replace('M', 'P')` will find `M` and change it with `P`, it returns a new string not modify existing string.
    - `replace()` is case sensitive.
    - `replace()` takes 3 argument, the 3rd argument is the count, i.e. no of time the replace should happen.
* there are apis like `rfind`, which will search from right, in place from left.


To see all the Api's in the `string`, we can use `dir(str)`, gives output,

````
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
````

To get a nicer version of information use `help(str)`

## [break](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=2264) ##

A `break` statement, throws us out of the loops. Consider the below code:-

````
for i in range(1,5):
    for j in range(5,1,-1):
        print "1: " "i = ", i," j: ", j
        if(i == j):
            break
    print
````

The `break` will stop from inner `j` loop.

## [Functions](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=2569)##

A function is most simplistic form can be defined as a named object, which takes inputs(arguments), does some processing on the input (body of the function) and returns some output.

A sample code for a function could be:-

````
def cube(number):
    """Takes a number and returns the cube of that number.
        Input: number (float or int)
        output: number (float)"""
    return number**3

print "cube(5): ", cube(5)  
````
In the above code:-
* `def` is a keyword.
* `cube` is a function name.
* `number` is a argument.
* the `"""` is a doc string, which can be used to provide a specification of the function.
* the `return` statement is optional, if `return ` statement is not given, we get `None` as the return type as shown below.

````
def times2(number):
    """Takes a number and returns the doubles that number.
        Input: number (float or int)
        output: number (float)"""
    number = number * 2

print "times2(10): ", times2(10)    #prints None
````

### [Scope ](https://www.youtube.com/watch?v=nx6NnzIGrKE&list=PLB2BE3D6CA77BB8F7#t=2969) ###

We have two types of scope:-

* **Global** Scope
* **Local** Scope

Here is an example to understand:-

````
allHope = "Here be dragons"         #global variable

def allYoursVarsAreBelongToUs(variables):
    """Steal all you variables.
        input: variables
        output: none"""
    myVariable = "Make your time"   #local variable
    print "paramter passed into the function: ", variables
    print "Global Variable: ", allHope
    print "Local Variable: ", myVariable

oldMemeIsOld = "Somebody set up the bomb"
allYoursVarsAreBelongToUs(oldMemeIsOld)

print "myVariable: ", myVariable    #give error.
````

The last line gives following error.

````
NameError: name 'myVariable' is not defined
````

because the variable `myVariable` have local scope.

One thing to remeber is that functions are also objects in Python. So if you invoke code like this. So if a function is called without parentheses it will work as an object.

````
print cube  #prints <function cube at 0x10c4d6410>
````