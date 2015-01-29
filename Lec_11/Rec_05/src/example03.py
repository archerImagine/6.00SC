class Shapes(object):
	def area(self):
		raise NotImplementedError
	def perimeter(self):
		raise NotImplementedError
	def __eq__(self,other):
		return self.area() == other.area()
	def __lt__(self,other):
		return self.area > other.area()

class Rectangle(Shapes):
	def __init__(self,side1,side2):
		self.side1 = side1
		self.side2 = side2
	def area(self):
		return self.side1 * self.side2
	def perimeter(self):
		return 2 * self.side1 + 2 * self.side2
	def __str__(self):
		return 'Rectangle(' +str(self.side1) +', ' +str(self.side2) +')'

class Circle(Shapes):
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		return 3.14159 * (self.radius ** 2)
	def perimeter(self):
		return 2.0 * 3.14159 * self.radius
	def __str__(self):
		return "Circle(" +str(self.radius) +")"

class Square(Rectangle):
	def __init__(self,side):
		self.side = side
		Rectangle.__init__(self,side,side)
	def __str__(self):
		return "Square(" +str(self.side) +")"


s = Shapes()		
#print s.area() #raise NotImplementedError

r = Rectangle(2,4)
sq = Square(4)
c = Circle(10)

print "Rectangle area: ", r.area()
print "Square area: ", sq.area()
print "Circle area: ", c.area()

print "Rectangle(2,8) == Square(4): ", r == sq
print "Rectangle(2,8) < Square(4): ", r < sq

print "Circle(10) == Square(4): ", c == sq
print "Circle(10) < Square(4): ", c < sq

# Because of polymorphism and inheritance, we don't need to 
# be concerned with which Shapes we are calling area() on

listOfShapes = [c,sq,r]
for shapes in listOfShapes:
	print "type(shapes): ", type(shapes), "shapes.area(): ", shapes.area()


listOfShapes.sort()	
print "----------------"
for shapes in listOfShapes:
	print shapes, "shapes.area(): ", shapes.area()