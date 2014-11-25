def withinEpsilon(x, y, epsilon):
    """x,y,epsilon ints or floats.  epsilon > 0.0
       returns True if x is within epsilon of y"""
    #return abs(x - y) <= epsilon

print withinEpsilon(2,3,1)
val = withinEpsilon(2,3,0.5)
print val    