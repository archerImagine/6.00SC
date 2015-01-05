
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
print "L[0][1] is ", L[0][1]	#prints Harvard

print "\nMetrics\n"
M = [[0,1],[1,2],[2,3],[3,4]]
print "M: ", M
print "M[2]: ", M[2]
print "M[2][0]: ", M[2][0]
print "M[2][1]: ", M[2][1]