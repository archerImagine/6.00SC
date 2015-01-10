# Bisection recursion algo for sqrt of 2

def bisectionSqrt(x, epsilon = 0.01, low = None, high = None):
	""" 
		Performs a recursive bisection search to find the
		square root of x, within epsilon
	"""

	if low == None:
		low = 0.0
	if high == None:
		high = x

	midPoint = (high + low)/2.0
	# If the difference of the midpoint squared and x is
	# within the epsilon tolerance, OR is the midpoint is
	# greater than X, we stop and give answer
	if abs(midPoint**2 - x) < epsilon or midPoint > x:
		return midPoint
	else:
		# Otherwise check if the midPoint is too big or small
		if midPoint ** 2 < x:
			# If too small, recurse on the upper half
			return bisectionSqrt(x,epsilon,midPoint,high)
		else :
			# If too big, recurse on the lower half
			return bisectionSqrt(x,epsilon,low,midPoint)


print "bisectionSqrt(25): ", bisectionSqrt(25)