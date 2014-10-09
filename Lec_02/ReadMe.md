# Lecture 02 | Core Elements of a Program
## [IDLE](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=69)

IDLE is the **IDE (Integrated Development Environment)** built for Python. So what does make a IDE:-
* Specialized Text Editor
* Provides Highlighting
* Auto Completion
* Smart Indent
* It also includes a **Shell** which is the environment that actually interprets the python code.
* Integrated Debugger, print statements are our friend.

## [Object](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=233)

Everything in python in `Object`, in fact Python code itself is an object. Each Object have a `type` which tells us
* Kind of object it is
* What can be done with the `object`

### Type of Objects 
There is a built in function called `type`, to find the "typeof" an object. There are two fundamental type of Object:- 
* **Scalar**:  These are indivisible, i.e. basic type which cannot be created from any other type.
* **Non Scalar**

#### [Scalar](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=323)
The following are the **scalar type**.

* [Integer](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=365)
Integers in Python are represented as `int`,  for every type we write, we call the value assigned to it as **literal**. 
ex:-   
````
3
````
So when we check the `type` of `3` as shown below.  
````
type(3)
````
it will give the output as  
````
<type 'int'>
````
So the type of literal `3` is `int`

* [Float](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=425)

Float's correspond to what we call **real numbers**.   
ex:- 
````
3.2
````
check the `type` of `3.2` as shown  
````
type(3.2)
````
it will give the output as   
````
<type 'float'>
````

So in python `3` is an `int` but `3.0` is a `float`.

**NOTE:- ** 
* Do not `float` same as real number, they are similar but not the same.

* [Boolean](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=532)

Boolean have only two values.
* `True`, so `type(True)` gives `<type 'bool'>`
* `False`

* [None](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=584)

There is also a value called `None`, whose `type` is `<type 'NoneType'>`. It is used when we want to fill the value of something temporarily.

#### Non Scalar

* [String](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=630)
Python does not have a fundamental type for characters called `char`, as available in other programming languages, In its place we have `str`.
ex:-
````
'a'
````
when we check the `type` of `'a'` we get  
````
<type 'str'>
````

Literal of type `str` can be written with either `' '` or `""`.

## [Expression](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=738)

* **Expression:-** Sequence of operator and operands objects. 

### Operators 

ex:- 
````
3 + 2
````
gives an output as `5`, Now consider these two example.  

````
3/2
````
`/` is the **divide operator**, gives the output as `1` but consider this example.

````
3.0/2.0
````
gives the output as `1.5`.

**NOTE:-**
* Divide operator `/` on integer returns a literal with passing it by a  **floor** operator, which is not allowed in Python version 3.0
* User floating point number to get result as same as real number division.

### [Overloading](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=861)

Now consider this example, 
````
'a' + 'b'
````
returns `"ab"`

By this we can deduce that the operator `+` is **overloaded**.  **Overloaded Operators** have a meaning that depends on the type of the operands.

### [Type Conversion ](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=961)

For the below code
````
'a' + 3
````
We get a **Static Semantic Error**, because it follows the grammar or syntax i.e. operand operator operand, but there is no meaning on adding a string with a int, the exact error we get is.

````
>>> 'a' + 3
Traceback (most recent call last):
  File "<string>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects

````
Type checking is actually very good for a programming languages, because it tells the programmer that he is trying to do something which will be error prone later.

The above code can also be changed to a valid syntax by doing this.

````
'a' + '3'   //here '3' is a string
````

also we can do this.

````
'a' + str(3)    //any type name can be used to convert on type to other, so integer 3 is converted to string '3'

int('3')        //string 3 is converted to integer 3
````
but this below code will give an static semantic error  

````
int('0.0')
````

error is 

````
>>> int('0.0')
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '0.0'
````
also this is a valid conversion.

````
int(2.1)        //will give a output 2
````

## [Commands](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=1462)
**Program or Scripts**: These are sequence of commands, each commands telling the interpreter to do something.  
ex:- 
````
print type(5.6)
````

### [Variables](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=1500)
### [Assignment](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=1495)
Consider this example, 

````
x = 3
````
The above expression is an **assignment** expression, and `x` is a **variable**. In Python, a variable is just a name for an object.

An **assignment** expression, binds a variable with a value/object.

## [Input](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=1682)
To receive input from a keyboard we use `raw_input`
There are two type of input statement in Python2, 

**NOTE:-** Be careful python shell does print the quotes around the strings in shell.

### Raw Input
`raw_input`, only one present in Python 3,  it outputs all the input as strings.
### Input 
`input` does not do any type conversion.

## [Straight line and branching programs](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=1888)

All the program seen till now are **Straight Line Program**, which is executing a sequence of commands one after another without making any deviations.

### [Conditional Statement](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=1997)
Conditional statements are used to make decision about the flow of a programs. using this words.  
* `if`
* `else`
* `elif` : else if


ex:-

````
if x%2 == 0:
    print "Even"
else:
    print "Odd"    
````
The operator `==` is used to do a comparison.

### [Nesting ](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=2167)
We can also nest one condition inside another condition as shown below...:- 

````
if x%2 == 0:
    print "Even"
else:
    if x % 3 != 0
        print "Hello"
    print "Odd"    
````
Here is what an `if` constructs does:-
* Checks the condition, if it is true executes the `if ` block,
* Else block is executed
* It will either execute the `if` block or the `else` block but never both.

### [Indentation ](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=2220)
The indentation is very important in python.  Because of this the visual structure is following the semantic structure. 

## [Looping constructs](https://www.youtube.com/watch?v=SLvTCHhu5SE&list=PLB2BE3D6CA77BB8F7#t=2729)

When we add loops to a programming language, these programing language belongs to a class of programming language called **Turing Complete**. The concept of Loops are called **iteration**.  
With loops, we can execute a same instructions multiple times.

Here is a simple loops.

````
while ans*ans*ans < abs(x):
    ans = ans + 1
````




## References
### Links
1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/)
2. [Lecture code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/MIT6_00SCS11_lec02.pdf)
3. [Lecture code (PY)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/lec02.py)

### Problem Sets
1. Problem Set 0: Introduction to Python and IDLE (Due)
    1. [Problem Set 0](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/MIT6_00SCS11_ps0.pdf)
2. Problem Set 1 (Assigned)
    1. [Problem Set 1 Due on Lecture 4](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/)

## Check Yourself
### What is a 'type'?

The type tells the classification of an object, so that we can determine what operation can be performed on them.

### What is an 'expression'?

An expression is a combination of operand operator, which computes to give a value.

### What is a type conversion?

When we have type `3` which is an `int`, we can convert its type to string using `str(3)` for operation or in an expression. So basically it converts one type to another.

### What is a keyword?

Keyword are string which have special meaning in a programming language.

### What is the difference between a straight line program and a branching program?

Straight line program have a single flow of control, where as a branching program have multiple flow of control depending on the no of branches.

### What is a conditional? 

A conditional statement is `if`, `elif` or `else`
