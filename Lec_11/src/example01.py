class intSet(object):
	"""An intSet is a set of integers"""
	def __init__(self):
		"""Creates an empty set of integers"""
		self.numBuckets = 47
		self.vals = []
		for i in range(self.numBuckets):
			self.vals.append([])

	def hashE(self,e):
		"""Private Function: Should not be used outside of class"""
		return abs(e)%len(self.vals)

	def insert(self,e):
		"""Assumes e is an integer and inserts e into self"""
		for i in self.vals[self.hashE(e)]:
			if i == e:
				return
		self.vals[self.hashE(e)].append(e)
		

	def member(self,e):
		"""Assumes e is an integer,
			Returns True if e is in self, and False otherwise
		"""
		return e in self.vals[self.hashE(e)]

	def __str__(self):
		"""Returns a string representation of self"""
		elems = []
		for bucket in self.vals:
			for e in bucket:
				elems.append(e)
		elems.sort()
		result = ''
		for e in elems:
			result = result + str(e) +", "
		return '{' +result[:-1] +'}'


def testOne():
	s = intSet()
	for i in range(40):
		s.insert(i)	

	print "s.member(14): ", s.member(14)
	print "s.member(41): ", s.member(41)
	print "s: ", s
	print "s.vals: ", s.vals

testOne()
		