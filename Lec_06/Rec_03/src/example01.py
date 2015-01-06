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
print "tupB[len(tupB) - 1] is : ", tupB[len(tupB) - 1]

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