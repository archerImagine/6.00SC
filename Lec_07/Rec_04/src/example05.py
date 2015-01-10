# Floating Point


# Floating Point can be inexact
# Know that 1/100 + 9/100 = 10/100 but ...

ten_hundredths = 10/100.0
one_hundredths = 1/100.0
nine_hundredths = 9/100.0

if ten_hundredths == (one_hundredths + nine_hundredths):
	print "Yes, (10/100.0) equals (1/100.0 + 9/100.0)"
else :
	print "No, (10/100.0) equals (1/100.0 + 9/100.0)"
	print "10/100.0 is : ", ten_hundredths, " ... which python represents as ", \
			repr(10/100.0)
	print "(1/100.0 + 9/100.0) is : ", (1/100.0 + 9/100.0), " ... which python represents as ", \
	repr((1/100.0 + 9/100.0))


# use epsilon to compare Floating point number, not ==

print "\n\nUsing with epsilon compare\n\n"

def compare(x,y,epsilon = 0.00001):
	""" 
		Takes two floating point numbers, x and y, and determines if
		they are within epsilon of one another.

		If no value of epsilon is supplied, the default value of 0.00001,
		is used.

		Returns true if they are else false.
	"""

	return abs(x - y) < epsilon

if compare((one_hundredths + nine_hundredths), ten_hundredths):
	print "Yes, (10/100.0) is within epsilon of (1/100.0 + 9/100.0)"
else:
	print "Yes, (10/100.0) is not within epsilon of (1/100.0 + 9/100.0)"


print "\n\n"
# Consider the below example, carefully.
# Even though floating point numbers are inexact, it is still consistent and mechanistic

nine_hundredths_plus_one_hundredths = nine_hundredths + one_hundredths
nine_hundredths_plus_one_hundredths -= one_hundredths

print "9/100.0 + 1/100.0 - 1/100.0 == 9/100.0", nine_hundredths_plus_one_hundredths == nine_hundredths