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