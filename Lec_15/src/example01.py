X = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
def stdDev(X):
	mean = sum(X)/float(len(X))
	total = 0.0
	for x in X:
		total += (x - mean)**2
	return (total/len(X)) ** 0.5

print "stdDev(X): ", stdDev(X)	