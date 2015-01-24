def euclid(a,b):
	if b == 0:
		return a
	else:
		return euclid(b,a%b)

print euclid(21,9)

def extendedEuclid(a,b):
	if b == 0:
		return (a,1,0)
	else:
		(dNew,xNew,yNew) = extendedEuclid(b, a%b)
		(d,x,y) = (dNew,yNew,(xNew - ((a/b) * yNew)))
		print (d,x,y)
		return (d,x,y)

print extendedEuclid(18,30)		