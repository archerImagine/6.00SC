import datetime

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		#Create a person with name
		self.name = name
		try:
			firstBlank = name.rindex(' ')
			self.lastName = name[firstBlank+1:]
		except Exception, e:
			raise e
