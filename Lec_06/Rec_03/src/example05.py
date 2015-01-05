#Casting List and tuple

#Can easily change mutablity properties by Casting
#List --> tuple, or tuple --> list

test_tuple = (1,4,'apple','ziggle')
print "test_tuple is : ", test_tuple

#Cast the tuple to a list
tuple_into_list = list(test_tuple)
print "I cast it to a list now it is of type, ", type(tuple_into_list)
print "I cast it to a list now it is of type, ", type(test_tuple)

#change an element of the list
tuple_into_list[3] = "banana"

test_tuple = tuple(tuple_into_list)
print "Now test_tuple is : ", test_tuple
print "    which is of type ", type(test_tuple)