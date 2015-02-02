import datetime

class Person(object):
	def __init__(self, name):
		#Create a person with name
		self.name = name
		try:
			firstBlank = name.rindex(' ')
			# print "__init__: firstBlank: ", firstBlank
			self.lastName = name[firstBlank+1:]
		except :
			self.lastName = name
		self.birthDay = None

	def getLastName(self):
		#returns self's last name
		return self.lastName
	def setBirthday(self,birthDate):
		#assumes that self's birthday is of type datetime.date
		#sets self's birthday to birthDate
		assert type(birthDate) == datetime.date
		self.birthDay = birthDate
	def getAge(self):
		#assumes that self's birthday is set
		#returns self's age in days
		assert self.birthDay != None
		return (datetime.date.today() - self.birthDay).days
	def __lt__(self,other):
		#returns True if self name is lexicographically greater
		#than other's name, and False Otherwise
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName
	def __str__(self):
		return self.name

class MITPerson(Person):
	nextIDNum = 0
	def __init__(self, name):
		#super(MITPerson, self).__init__()
		Person.__init__(self,name)
		self.idNum = MITPerson.nextIDNum
		MITPerson.nextIDNum += 1
	def getIdNum(self):
		return self.idNum
	def __lt__(self, other):
		return self.idNum < other.idNum
	def isStudent(self):
		return type(self)==UG or type(self)==G

class UG(MITPerson):
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None
    def setYear(self, year):
        if year > 5:
            raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year

class G(MITPerson):
    pass		

class CourseList(object):
    def __init__(self, number):
        self.number = number
        self.students = []
    def addStudent(self, who):
        if not who.isStudent():
            raise TypeError('Not a student')
        if who in self.students:
            raise ValueError('Duplicate student')
        self.students.append(who)
    def remStudent(self, who):
        try:
            self.students.remove(who)
        except:
            print str(who) + ' not in ' + self.number
    def allStudents(self):
        for s in self.students:
            yield s
    def ugs(self):
        indx = 0
        while indx < len(self.students):
            if type(self.students[indx]) == UG:
                yield self.students[indx]
            indx += 1

m1 = MITPerson('Barbara Beaver')            
ug1 = UG('Jane Doe')
ug2 = UG('John Doe')
g1 = G('Mitch Peabody')
g2 = G('Ryan Jackson')
g3 = G('Jenny Liu')     

print "M1: ", m1

SixHundred = CourseList('6.00')
SixHundred.addStudent(ug1)
SixHundred.addStudent(g1)
SixHundred.addStudent(ug2)

print "SixHundred: ", SixHundred
print "SixHundred.students: ", SixHundred.students

for student in SixHundred.students:
	print "student: ", student

print 'Students Squared'
for s in SixHundred.allStudents():
   for s1 in SixHundred.allStudents():
       print "s= ", s ," s1: ", s1	