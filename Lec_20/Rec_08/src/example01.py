num = range(1,10)
print "type(num): ", type(num)
print "num: ", num

xnum = xrange(1,10)
print "type(xnum): ", type(xnum)
print "xnum: ", xnum

def myXrange(maxValue):
    i = 0
    while i < maxValue:
        yield i
        print "Inside Function: ", i
        i += 1

myNum = myXrange(10)
print "type(myNum): ", type(myNum)
print "myNum: ", myNum

for x in myXrange(10):
    print "OutSide Function: ", x
    