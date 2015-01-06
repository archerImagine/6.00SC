tupA = (1,'apple',6.00)
listA = [0.234,'apple',(1,2),77]
listB = [0.234,'Banana',(1,2),77]
tupB = (listA,'MIT',[4,5])

print "tupA: ", tupA
print "listA: ", listA
print "tupB: ", tupB

print "\ntupB[0]:", tupB[0]
print "\ntupB[0][0]:", tupB[0][0]

tupB[0][0] = 0.1

print "\ntupB:", tupB
print "listA: ", listA

# tupB[0] = listB #gives error

myTemp = tupB[0]

listA.append('Harvard')
print "After appending to listA: ", listA
print "After appending to tupB: ", tupB

t = ('red', [10, 20, 30])
print "t: ", t

staff = {
	'Mitchell' 	: 'mizhi@mit.edu',
	'Ryan'		: 'rwx@mit.edu',
	'Sarina'	: 'Sarina@mit.edu'
}

tupC = (staff,'MIT',[4,5])
print "tupC: ", tupC