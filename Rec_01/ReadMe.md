# Recitation 1: Review Of Lecture 01 and 02

## Introduction

### What is a computer?

The most basic computer consists of these 4 components.  

* CPU
* Memory
* Input 
* Output

### What is a program?
A program is a sequential steps of execution of instruction, which are loaded from memory to be executed.  
Computer executes instruction in **binary** format i.e. every instruction is a sequence of 0's and 1's, but this is very difficult for humans to read.  

````
0001 1110 // mean add 1 to a variable x
````

So we have an abstraction on top of binary instruction which is somewhat readable to humans, like 

````
mov ax,1    //assign value 1 to a variable ax
add ax,5    //add 5 to what ever is stored in variable `ax`
````

Now this sequence is readable to humans, but still a bit difficult, so we have programming languages like **Python**, which provides us with a language which is much closer to human understanding, like

````
ax = 1  //assign 1 to a variable ax
ax = ax + 5 //add 5 to ax
````
Now if you see these code sequence which is much more readable than previous 2.

So all the programming languages allows us to express our thought in a language we understand than converts it to a language (binary) which a computer can understand and executes.

## Syntax & Semantics

### Syntax 

Every programming languages have a set of **syntax**, it is a way part of the language put together. 

ex:- 
````
variable + variable     //valid syntax in Python
variable variable +     //not valid in Python, but may be valid in other.
````

### Static Semantics

Static Semantics is syntactical valid statement which **means**  something.

ex:- 

`````
a = 5
b = 2
a/2     //valid operation
a/b     //valid operation

c = "foo"
a/c     //syntactically valid, but static semantic is off, because how to divide number with a string
`````

The **Syntax** and **Static Semantics**, are easier for a compiler or interpreter to check, as these are pretty explicit rules.

### Semantics

This is the part where the Syntax of the program is correct, the sequence of instructions have some meaning (Static Semantically correct) , but as a whole the programs does not work.

ex:- 
````
a = 5
b = 2
a/b         //correct, both syntactically and static semantically.

c = 0
a/c         //correct, both syntactically and static semantically, but does not give the required out put.
````

All program are very explicit, without ambiguity.

# Python Introduction.

Python is a general purpose language, used for  

* Web Development,
* UI development
* Test Automation etc.

Python is a interpreted language, which means, the code which we write is interpreted and executed directly, there is nothing in between like in compiled language.

Like all programming languages, Python have a sequence of **expression**. An expression consist of **Operand**, **Operator**, **Operand**, ex:-

````
myVar = 'A String'  //myVar is a variable, 
                    //`A String` is a string literal.
                    // = is a operator.
                    //so variable and literals are things i.e. Operand on which the operator `=` works on
````

Everything in Python is object.

## Type of Object in Python.

### int's 
`int` means integer, like.  
````
7,8,9,-1,2
````

The operation possible on **int's** are as given below.

| Operator | Meaning        |  
|:--------:| :--------------|
| `+`      | Addition       |  
| `-`      | Subtraction    |  
| `*`      | Multiply       |  
| `/`      | Division       |  
| `**`     | Exponentiation |  
| `%`      | Modulo         |  

In case of integer division, the decimal portion is truncated, not **floored** or **ceilinged**.

### float's 
Float are similar to real numbers, but not always, which will be discussed lated. Float's are numbers with decimal point.

````
2.5, 3.14, 0.0
````

Pythons creates the type of a variable based on the value stored in it. ex.  
````
a = 1   //type of a is int here.
b = 1.0 //type of a is float here.
````

The operation possible on **float's** are as given below.

| Operator | Meaning        |  
|:--------:| :--------------|
| `+`      | Addition       |  
| `-`      | Subtraction    |  
| `*`      | Multiply       |  
| `/`      | Division       |  
| `**`     | Exponentiation |  

### String's 
String is just a sequence of characters.

ex:- 

````
myVar = "Hello"
````

In python, we can specify a string using single quote `''` or double quote `""`. This is use fully when one string is embedded inside another. ex.  

````
myVar = "Hello, 'Maths' i do not understand you."
````

We can do `concatenationn` in python like..

ex:-

````
s1 = "Hello"
s2 = "World"

s1+s2   //"Hello World", concatenate.
````

### Boolean's

It is a type with 2 values, `True` and `False`.

### None Type.

It holds a place like a place holder, without any value.

The data type to be discussed later.
### List
### Tuple
### Dictionary 

## Comparison Operator.

Comparison operator are applicable to **Boolean** data type, each operator takes two operand and compare them based on the operator mentioned below.

| Operator |        Meaning        |
| :------: | :-------------------- |
|   `<`    | Less Than             |
|   `>`    | Greater Than          |
|   `<=`   | Less then equal to    |
|   `>=`   | Greater then equal to |
|   `!=`   | Not Equal             |
|   `==`   | Equal                 |
|          |                       |

example:-
`````
a = 2
b = 3
a < b   //True
a > b   //False
`````

## Logical Operator

| Operator |   Meaning   | No of Operator |
| :------: | :---------- | -------------- |
|   and    | Logical And |              2 |
|    or    | Logical or  |              2 |
|   not    | Logical Not |              1 |


### `and` Operator 

Below example shows the use of `and` operator. `and` **return true if an only if both operand are True** 

````
a = True
b = True
c = False

a and b     //True
a and c     //False
````
### `or` Operator

Below example shows the use of `or` operator. `or` returns `True` when anyone of the operator is `True`, `False` when both the operand are `False`.

````
a = True
b = True
c = False

a or b     //True
a or c     //True
````

### `not` Operator

Below example shows the use of `not` operator. `not` reverses the boolean value of the operand.

````
b = True
c = False

not b   //False
not c   //True
````


We can also combine the `not`, `and`, `or` operator to make complex comparison like shown below.

````
a = True
b = True
c = False

(a and b) or c  //True
````

**Comparison** operators take numeric value and output's Boolean value, which can then be tested with **Logical** Operator.

example:-

````
d = 3
e = 4
f = 5

(d < e) and (e < f)     //True
````

## Flow Control Statements.

Till now all the operators are able to perform single line operations, so we cannot deviate for the top down flow of program. We can use the Branching statement to change the flow of statements.

### Branching Statements.
#### `if`  `elif` `else` Statement

The basic syntax of these are given below.

````
if <condition>:
    Execute True block
elif <condition>:
    Execute this block when if block is false.
else :
    Execute this block when both the above block is false.
````

`elif` and `else` block in the above syntax is not necessary.  
Python represent block of code by indent, and not using any brackets.

#### Looping Statement.
These are the statements which are executed in loops i.e. iterate over multiple times.

There are two variant of the loops.

1. `for` loop
2. `while` loop

#### `for` loop

`for` loop is used when we have to iterate over a definite set of data as shown below.

````
for i in range(1,10)
    print i    //will print 1,2,3,4,5,6,7,8,9, execute 9 times with incrementing the value of i.
````


#### `while` loop

A `while` loop executes till a conditions remains `True`, So while loop is mostly used when we are not sure the no of iteration which will be required.

example:- 

````
while <condtion>:
    //Execute till the condition is True.
````


