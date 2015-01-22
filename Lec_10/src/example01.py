numBuckets = 47 	#This is ugly, we will better it soon.

def create():
	global numBuckets
	hSet = []
	for i in range(numBuckets):
		hSet.append([])
	# print "[XYZ]: create() hSet: ", hSet, " type(hSet): ",type(hSet)
	return hSet

def hashElem(e):
		global numBuckets
		return e % numBuckets

def insert(hSet,i):
	hSet[hashElem(i)].append(i)
	# print "[XYZ]: insert() hSet: ", hSet, " type(hSet): ",type(hSet)

def remove(hSet,i):
	newBucket = []	
	for j in hSet[hashElem(i)]:
		if j != i:
			newBucket.append(j)
	hSet[hashElem(i)] = newBucket
	print "[XYZ]: remove() i: ", i," hashElem[i]: ", hashElem(i), " hSet[hashElem(i): ", hSet[hashElem(i)]

def member(hSet,i):
		return i in hSet[hashElem(i)]

def testOne():
	s = create()		
	for i in range(40):
		insert(s,i)
	print "[XYZ]: S: ", s
	insert(s,325)
	insert(s,325)
	insert(s,9898900067)
	print "[XYZ]: S: ", s
	print "[XYZ]: ,member(s,325): ",member(s,325)
	remove(s,325)
	print "[XYZ]: After Remove, member(s,325): ",member(s,325)
	print "[XYZ]: member(s,9898900067)",member(s,9898900067)

testOne()	