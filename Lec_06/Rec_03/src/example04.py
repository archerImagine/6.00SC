tupA = (1,'apple',6.00)

listA = [0.234,'apple',(1,2),77]
listB = [listA,'MIT',[3,1,4]]

#since tuple are immutable, cannot reassign
#tupA[0] = 3 #TypeError: 'tuple' object does not support item assignment

#list are mutable
print "listA: ", listA
print "listB: ", listB
listA[0] = 88

print "Now listA: ", listA
print "Now listB: ", listB

#Aliasing: giving two name to the same list - Printing the same list
listX = [1,4,5]
listY = listX
print "listX is: ", listX, "and listY is: ", listY
listX[0] = "banana"
print "listX is: ", listX, "and listY is: ", listY

#Aliasing happens when we define a list(like listA is included inside listB), 
#When we change listA[0], since listB was containg listA, it printed the 
#modified value.
print "Now listB: ", listB

#To Copy without Aliasing use a full slice
listX = [1,4,5]
listY = listX
listZ = listX[:] #full slice
print "listX is: ", listX, "and listY is: ", listY, " and listZ is : ", listZ
listX[0] = "banana"
print "listX is: ", listX, "and listY is: ", listY, " and listZ is : ", listZ