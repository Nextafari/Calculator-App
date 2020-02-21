class Dog(object):
	def __init__(self, name):
		self.name = name

	def what_are_you(self):
		print("my name is {} and I am a dog".format(self.name))


obj1 = Dog(name="Bingo")
obj1.what_are_you()

