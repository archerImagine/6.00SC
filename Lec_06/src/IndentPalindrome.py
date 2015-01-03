def toChars(s):
	import string
	s = string.lower(s)
	ans = ''
	for c in s:
		if c in string.lowercase:
			ans = ans + c
	return ans

def isPal(s):
	if len(s) <= 1:
		return True
	else:
		return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
	"""Returns True if s is a palindrome and False otherwise"""
	return isPal(toChars(s))


print isPalindrome('Guttug')