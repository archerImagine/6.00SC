# MIT 6.00SC | Recitation 03 | Lists and their Elements, Sorting, and Recursion#

## [Tuple ](https://www.youtube.com/watch?v=Fixc8hVo_cY&list=PLB2BE3D6CA77BB8F7#t=41) ##

Consider the below example:-

````
# Tuple may have any type of elements in them
# Strings,ints,floats,other tuples,or other lists.

tupA = (1,'apple',6.00)
tupB = (tupA,'MIT',[4,5])

print "tupA is ", tupA, " with length ", len(tupA)
print "tupB is ", tupB, " with length ", len(tupB)

print "\nIndexing Operations: \n"

print "tupA[0] is : ", tupA[0]
print "tupA[2] is : ", tupA[2]
#print "tupA[3] is : ", tupA[3] #error because of index out of bounds.

print "tupB[0] is : ", tupB[0]
print "tupB[0][1] is : ", tupB[0][1]
print "tupB[2] is : ", tupB[2]
print "tupB[-1] is : ", tupB[-1]

print "\nSlicing Operations: \n"
print 'tupA[0:1] is: ', tupA[0:1]
print 'tupA[0:100] is: ', tupA[0:100]
print 'tupA[0:2] is: ', tupA[0:2]
print 'tupA[:2] is: ', tupA[:2]
print 'tupA[1:] is: ', tupA[1:]
print 'tupA[:] is: ', tupA[:]
print 'tupB[-1:-3] is: ', tupB[-1:-3]
 
print "\nIteration Over Tuple\n" 
for item in tupB:
    print item, "is of type: ", type(item)

#the above code is equivalent to
print "\nIteration Over TupB\n" 
for i in range(len(tupB)):
    print tupB[i], "is of type: ", type(tupB[i])
````

We will understand the above code, one by one, but before we start, we have a very good question to start.

### Food For Thought ###

**As we all know a tuple is immutable, and a list/Dictionary is mutable, so can a Tuple contain a list/Dictionary?**

The same question is answered here, kindly check, it answers for List, but the same logic can be given for Dictionary.

* [StackOverFlow | Why can tuples contain mutable items?](http://stackoverflow.com/questions/9755990/why-can-tuples-contain-mutable-items)

But to understand the above links, we might have to see this 

* [Facts and myths about Python names and values](http://nedbatchelder.com/text/names.html)

### Indexing Operation in Tuple ###

As seen in the above example, lets focus on the indexing Operations on that.

````
tupA = (1,'apple',6.00)
tupB = (tupA,'MIT',[4,5])   #this tuple contains a List,

print "tupA is ", tupA, " with length ", len(tupA)
print "tupB is ", tupB, " with length ", len(tupB)

print "\nIndexing Operations: \n"

print "tupA[0] is : ", tupA[0]  #Access the first Element., i.e. 1
print "tupA[2] is : ", tupA[2]  #Access the 3rd Element., i.e. 6.00
#print "tupA[3] is : ", tupA[3] #error because of index out of bounds. Means 4th element

print "tupB[0] is : ", tupB[0]
print "tupB[0][1] is : ", tupB[0][1]
print "tupB[2] is : ", tupB[2]
print "tupB[-1] is : ", tupB[-1]
````

One import piece of code in the above is.

````
print "tupB[-1] is : ", tupB[-1]
````

This is a short cut which we can use to get the last element of a tuple, list, Dictionary. In place of doing this.

````
print "tupB[len(tupB) - 1] is : ", tupB[len(tupB) - 1]
````

Another line of code to consider is:-

````
print "tupB[0][1] is : ", tupB[0][1]
````

So in the above code, we have the tuple as this.

````
tupB = (tupA,'MIT',[4,5])
````

Now the code `tupB[0]` references the `tupA` which is `(1,'apple',6.00)`, and then `tupB[0][1]` the `[1]` access the element `'apple'` in tuple A. So a Tuple within a tuple acts a 2D array.

### Slicing Operation in Tuple ###

We will check the code we mentioned first for the slicing Operations.

````
tupA = (1,'apple',6.00)
tupB = (tupA,'MIT',[4,5])

print "\nSlicing Operations: \n"
print 'tupA[0:1] is: ', tupA[0:1]
print 'tupA[0:100] is: ', tupA[0:100]
print 'tupA[0:2] is: ', tupA[0:2]
print 'tupA[:2] is: ', tupA[:2]
print 'tupA[1:] is: ', tupA[1:]
print 'tupA[:] is: ', tupA[:]
print 'tupB[-1:-3] is: ', tupB[-1:-3]
````

**Slicing Operation:-** It is an operation which will provide us with a part or sub sequence of the original tuple.

Slicing Operation can become a little confusing, so the basic of it can be explained with this example:-

````
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
````

The last notation `a[:]` have a special meaning in terms of List, which we will see once we come to it. 

To understand slice operation in more details you can check these links.

* [StackOverFlow | Explain Python's slice notation ](http://stackoverflow.com/questions/509211/explain-pythons-slice-notation)


### Iteration in a tuple ###

We can iterate over a tuple by using a simple `for in ` loop as shown below:-

````
for item in tupB:
    print item, "is of type: ", type(item)
````

You can also use the array index operation to iterate over a Tuple as shown below.

````
for i in range(len(tupB)):
    print tupB[i], "is of type: ", type(tupB[i])
````

## [List ](https://www.youtube.com/watch?v=Fixc8hVo_cY&list=PLB2BE3D6CA77BB8F7#t=310) ##

So we will start with a question, **What is the difference between a List and a Tuple?**

The one major difference is that, List is mutable, but a tuple is not, and since a List is mutable we have special functions in List to support mutability like `append`, `remove` etc.

To add a element to a list we can do this:-

````
listA = [0,1,2]
listA.append(3)
listA.pop()         #removes the last element of a list.
````

Some tricks with list are as below.

````
A = [0] * 10        #Creates a list with 10 element init to 0

A = [[]] * 10       #Creates a empty list of list.

````

This syntax `A = [[]] * 10` can be used to pass a empty list to a function, which can modify the list as it wants. 

The Slice, Iteration and Indexing operation on a List are same as tuple, so we can understand it from this example:-

````

listA = [0.234,'apple',(1,2),77]
listB = [listA,'MIT',[3,1,4]]

print "listA is ", listA, " with length ", len(listA)
print "listB is ", listB, " with length ", len(listB)

print "\nIndexing Operations: \n"
print "listA[0] is : ", listA[0]
print "listA[3] is : ", listA[3]
# print "listA[4] is : ", listA[4] #error, list index out of range
print "listB[0] is : ", listB[0]
print "listB[0][1] is : ", listB[0][1]
print "listB[-1] is : ", listB[-1]

print "\nSlicing Operations: \n"
print "listA[0:1] is : ", listA[0:1]
print "listA[0:100] is : ", listA[0:100]
print "listA[0:2] is : ", listA[0:2]
print "listA[:2] is : ", listA[:2]
print "listA[1:] is : ", listA[1:]
print "listA[:] is : ", listA[:]
print "listB[-1:-3] is : ", listB[-1:-3]

#Iteration through List
print "\nIteration through List\n"
for item in listA:
    print item, " is of type: ",type(item)

#Access inner list
print "\nAccessing Inner List\n"    
L =[['MIT','Harvard'],['University'],0]
print "In List", L
print "L[0][1] is ", L[0][1]    #prints Harvard

print "\nMetrics\n"
M = [[0,1],[1,2],[2,3],[3,4]]
print "M: ", M
print "M[2]: ", M[2]
print "M[2][0]: ", M[2][0]
print "M[2][1]: ", M[2][1]
````

On interesting thing which can be done using list is create a Matrix as shown below.

````
print "\nMetrics\n"
M = [[0,1],[1,2],[2,3],[3,4]]
print "M: ", M
print "M[2]: ", M[2]
print "M[2][0]: ", M[2][0]
print "M[2][1]: ", M[2][1]
````

### Operation on List ###

Since List are mutable, it has few methods which helps in this mutability. Kindly see the below example which we will discuss in detail.

````
LA = [6.00,'MIT',600,600]
print "LA: ", LA

LA.append('Harvard')
print "LA: LA.append('Harvard'): ", LA

LA.append(['Yale','Standford'])
print "LA: LA.append(['Yale','Standford']): ", LA

LA.pop()
print "LA: LA.pop(): ", LA

LA.pop(0)
print "LA: LA.pop(0)", LA

LA.extend(['Yale','Standford'])
print "LA: LA.extend(['Yale','Standford']): ", LA

LA.remove(600)
print "LA: LA.remove(600): ", LA

LA.remove(600)
print "LA: LA.remove(600): ", LA

#LA.remove(500) #error: ValueError: list.remove(x): x not in list

if 500 in LA:
    LA.remove(500)


LA.sort()   
print "LA: LA.sort(): ", LA
````

In the above example we have already discussed these methods:-

* `append()`
* `pop()`
* `remove(600)`

So one Method which we have not discussed is.

* `extend()`
    It take a argument a list, and it merges this list with the list on which it is called.

    ````
    LA = [6.00,'MIT',600,600]
    LA.extend(['Yale','Standford'])

    print "LA: LA.extend(['Yale','Standford']): ", LA #prints [6.0, 'MIT', 600, 600, 'Yale', 'Standford']

    ````

    You can extend a tuple, but it will create a new tuple by using `+` operator.


Interesting thing about is being mutable can be seen with this example:-

````
tupA = (1,'apple',6.00)

listA = [0.234,'apple',(1,2),77]
listB = [listA,'MIT',[3,1,4]]

#since tuple are immutable, cannot reassign
#tupA[0] = 3 #TypeError: 'tuple' object does not support item assignment

#list are mutable
print "listA: ", listA      #prints [0.234, 'apple', (1, 2), 77]
print "listB: ", listB      #prints [[0.234, 'apple', (1, 2), 77], 'MIT', [3, 1, 4]]
listA[0] = 88

print "Now listA: ", listA  #prints [88, 'apple', (1, 2), 77]
print "Now listB: ", listB  #prints [[88, 'apple', (1, 2), 77], 'MIT', [3, 1, 4]]
````    

As you can see since `listB` contains `listA`, when we modified `listA` by doing this `listA[0] = 88`, the change is reflected in both `listA` and `listB`. The reason being, `listB` has a reference to `listA` and not a copy of `listA`.

This same behavior can be seen with **aliasing** of list.

````
listX = [1,4,5]
listY = listX
print "listX is: ", listX, "and listY is: ", listY
listX[0] = "banana"
print "listX is: ", listX, "and listY is: ", listY
````

So the assignment `listY = listX` just copies the reference of `listX` into `listY`, and both point to same memory location, so a change to one list will affect the other. If we do not want this side effect, and want a copy of the list we have to use `:` slice operator as shown below:-  

````
listX = [1,4,5]
listY = listX
listZ = listX[:] #full slice
print "listX is: ", listX, "and listY is: ", listY, " and listZ is : ", listZ
listX[0] = "banana"
print "listX is: ", listX, "and listY is: ", listY, " and listZ is : ", listZ
````

so this `listX[:]` gives us the **full slice** of the list.

**Casting** helps us to change the behavior of list to tuple and vice versa, as shown below:-

````
#Casting List and tuple

#Can easily change mutablity properties by Casting
#List --> tuple, or tuple --> list

test_tuple = (1,4,'apple','ziggle')
print "test_tuple is : ", test_tuple

#Cast the tuple to a list
tuple_into_list = list(test_tuple)
print "I cast it to a list now it is of type, ", type(tuple_into_list)
print "I cast it to a list now it is of type, ", type(test_tuple)

#change an element of the list
tuple_into_list[3] = "banana"

test_tuple = tuple(tuple_into_list)
print "Now test_tuple is : ", test_tuple
print "    which is of type ", type(test_tuple)
````

## [Dictionary ](https://www.youtube.com/watch?v=Fixc8hVo_cY&list=PLB2BE3D6CA77BB8F7#t=1259) ##

Now the first question arises as why we require a Dictionary, when we have list, we can implement the behavior of Dictionary using a list, but some of the operation like searching etc are very inefficient in list, but when are of great quality in Dictionary, this is the reason for a separate type like Dictionary.

Consider the below example for Dictionary.

````
##Dictionaries

staff = {
    'Mitchell'  : 'mizhi@mit.edu',
    'Ryan'      : 'rwx@mit.edu',
    'Sarina'    : 'Sarina@mit.edu'
}

print "staff: ", staff, " len(staff): ", len(staff)

# Made a mistake, Fix Ryan's address
staff['Ryan'] = 'rwj@mid.edu'

#Add Heymian
staff['Heymian'] = 'heymian@mit.edu'

if 'Heymian' in staff:
    print "Heymian in Staff"

if 'Gartbee' not in staff:
        print 'Adding Gartbee to the staff list'
        staff['Gartbee'] = 'gartbee@mit.edu'

print 'rvj@mit.edu' in staff

print staff

# One way to order alphabetically
staff.keys().sort() #will not sort
print staff

#Oops we fired Sarina
del staff['Sarina']
print staff

# Go Through key,value pair

for TA,Email in staff.items(): # staff.items() returns a key,value pairs
    print "TA: ", TA, " his mailid ", Email
````

A Dictionary is a `<key,value>` pair, where `keys` must be immutable, and unique.

There is no order of storing in Dictionary. 

We can check the presence of a key in a Dictionary like this.

````
if 'Heymian' in staff:
    print "Heymian in Staff"
````

Same way we can check for absence of key in a Dictionary

````
if 'Gartbee' not in staff:
        print 'Adding Gartbee to the staff list'
        staff['Gartbee'] = 'gartbee@mit.edu'
````

To iterate over a Dictionary we can use this.

````
for TA,Email in staff.items(): # staff.items() returns a key,value pairs
    print "TA: ", TA, " his mailid ", Email
````

## [Recursion ](https://www.youtube.com/watch?v=Fixc8hVo_cY&list=PLB2BE3D6CA77BB8F7#t=1986) ##

Consider the below example:-

````
def Factorial(n):
    #if base case is true, what is the base case.
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)


#Test

print "Factorial(0): ", Factorial(0)        
print "Factorial(5): ", Factorial(5)    
````