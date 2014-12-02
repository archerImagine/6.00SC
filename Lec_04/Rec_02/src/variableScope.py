allHope = "Here be dragons" 		#global variable

def allYoursVarsAreBelongToUs(variables):
	"""Steal all you variables.
		input: variables
		output: none"""
	myVariable = "Make your time"	#local variable
	print "paramter passed into the function: ", variables
	print "Global Variable: ", allHope
	print "Local Variable: ", myVariable

oldMemeIsOld = "Somebody set up the bomb"
allYoursVarsAreBelongToUs(oldMemeIsOld)

print "myVariable: ", myVariable