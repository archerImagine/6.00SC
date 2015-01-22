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
		if type(e) == int:
			val = e
		if type(e) == str:
			val = 0
			shift = 0
			for c in e:
				# print("[XYZ]: 1) hashElem() shift: ", shift, " val ", val, " ord(c) ", ord(c), " c: ",c," e: ",e)
				val = val + shift * ord(c)
				# print("[XYZ]: 2) hashElem() shift: ", shift, " val ", val, " ord(c) ", ord(c)), " c: ",c," e: ",e, "\n\n"
				shift += 1
		return val % numBuckets
				

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
def testTwo():
	d = create()
	strs = ['ab','ba','32a','big dog','small bird']
	# strs = ["abc"]
	for s in strs:
		insert(d,s)
	for i in range(40):
		insert(d,i)

	print "[XYZ]: testTwo(): d: ", d
	print "member(d,'small bird'): ", member(d,"small bird")
	print "member(d,'big bird'): ", member(d,"big bird")
	remove(d,"small bird")
	print "[XYZ]: testTwo(): d: ", d

testTwo()	